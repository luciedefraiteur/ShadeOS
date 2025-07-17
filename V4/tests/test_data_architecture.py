#!/usr/bin/env python3
"""
🧪 TESTS ARCHITECTURE DATA-DRIVEN V4
"""

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from core.data_models import *
from core.luciform_parser import LuciformParser
from core.data_manager import DataManager

def test_data_models():
    """Test des modèles de données"""
    print("🧪 TEST MODÈLES DE DONNÉES")
    print("=" * 50)
    
    # Test Message
    message = Message(
        expediteur="shadeos",
        destinataire="gemini", 
        contenu="Analyse le système",
        type_message=TypeMessage.COMMANDE
    )
    print(f"✅ Message créé: {message.expediteur} → {message.destinataire}")
    
    # Test Planification
    etapes = [
        Etape(id="1", description="Vérifier espace disque"),
        Etape(id="2", description="Analyser logs"),
        Etape(id="3", description="Générer rapport")
    ]
    plan = Planification(etapes=etapes, demande_originale="Analyse système")
    print(f"✅ Plan créé: {plan.total_etapes} étapes")
    print(f"   Étape courante: {plan.etape_courante.description}")
    
    # Test ExecutionWorker
    commandes = [
        CommandeShell(commande="df -h", resultat="78% libre"),
        CommandeShell(commande="ps aux", resultat="25 processus")
    ]
    execution = ExecutionWorker(
        commandes=commandes,
        statut_global=StatutExecution.SUCCES,
        rapport="Système stable"
    )
    print(f"✅ Exécution créée: {len(execution.commandes)} commandes")
    
    return True

def test_luciform_parser():
    """Test du parser luciform"""
    print("\n🔮 TEST PARSEUR LUCIFORM")
    print("=" * 50)
    
    parser = LuciformParser()
    
    # Test parsing sendMessage
    reponse_shadeos = """
    <luciform id="test" type="commande" niveau="⛧1">
        <commande>sendMessage("gemini", "Analyse l'état du système")</commande>
        <commande>sendMessage("lucieReineChienne", "Prépare un rapport")</commande>
    </luciform>
    """
    
    resultats = parser.parse_reponse(reponse_shadeos, "shadeos")
    
    if 'send_messages' in resultats:
        messages = resultats['send_messages']
        print(f"✅ {len(messages)} sendMessage extraits")
        for msg in messages:
            print(f"   {msg.source_entite} → {msg.destinataire}: {msg.message}")
    
    # Test parsing planification
    reponse_lucie = """
    <luciform id="planification" type="execution" niveau="⛧1">
        <planification>
            <etape id="1">Vérifier espace disque</etape>
            <etape id="2">Analyser logs système</etape>
            <etape id="3">Générer rapport final</etape>
        </planification>
        <commande>sendMessage("worker", "Étape 1: Vérifie l'espace disque")</commande>
    </luciform>
    """
    
    resultats_lucie = parser.parse_reponse(reponse_lucie, "lucie")
    
    if resultats_lucie.get('planification'):
        plan = resultats_lucie['planification']
        print(f"✅ Planification extraite: {len(plan.etapes)} étapes")
        for etape in plan.etapes:
            print(f"   Étape {etape.id}: {etape.description}")
    
    return True

def test_data_manager():
    """Test du gestionnaire de données"""
    print("\n📊 TEST GESTIONNAIRE DE DONNÉES")
    print("=" * 50)
    
    # Créer le gestionnaire
    dm = DataManager("test_data")
    
    # Test entités
    print(f"✅ {len(dm.etat_systeme.entites)} entités initialisées")
    for nom, entite in dm.etat_systeme.entites.items():
        print(f"   {nom}: {entite.role}")
    
    # Test traitement sendMessage
    send_messages = [
        SendMessage("gemini", "Analyse le système", "shadeos"),
        SendMessage("worker", "Vérifie l'espace disque", "lucieReineChienne")
    ]
    
    messages_crees = dm.traiter_send_messages(send_messages)
    print(f"✅ {len(messages_crees)} messages traités")
    
    # Test fil de discussion
    fil_gemini = dm.get_fil_discussion("gemini")
    print(f"✅ Fil Gemini: {len(fil_gemini.split('\\n'))} lignes")
    
    # Test planification
    etapes = [
        Etape(id="1", description="Test étape 1"),
        Etape(id="2", description="Test étape 2")
    ]
    plan = Planification(etapes=etapes)
    dm.mettre_a_jour_planification("lucieReineChienne", plan)
    
    etape_actuelle = dm.get_etape_plan_actuelle("lucieReineChienne")
    print(f"✅ Étape actuelle Lucie: {etape_actuelle}")
    
    # Test avancement
    dm.avancer_etape_plan("lucieReineChienne")
    etape_suivante = dm.get_etape_plan_actuelle("lucieReineChienne")
    print(f"✅ Étape suivante Lucie: {etape_suivante}")
    
    # Test statistiques
    stats = dm.get_statistiques()
    print(f"✅ Statistiques: {stats}")
    
    return True

def test_integration_complete():
    """Test d'intégration complète"""
    print("\n🌟 TEST INTÉGRATION COMPLÈTE")
    print("=" * 50)
    
    # Créer les composants
    parser = LuciformParser()
    dm = DataManager("integration_test")
    
    # Simuler un cycle complet ShadEOS → Gemini
    print("\n1️⃣ ShadEOS envoie une demande à Gemini")
    reponse_shadeos = """
    <luciform id="shadeos_demande" type="strategie" niveau="⛧1">
        <commande>sendMessage("gemini", "Analyse l'état global du système et recommande des optimisations")</commande>
    </luciform>
    """
    
    resultats_shadeos = parser.parse_reponse(reponse_shadeos, "shadeos")
    messages_shadeos = dm.traiter_send_messages(resultats_shadeos['send_messages'])
    print(f"   ✅ {len(messages_shadeos)} message envoyé")
    
    # Simuler réponse Gemini
    print("\n2️⃣ Gemini répond avec une analyse")
    reponse_gemini = """
    <luciform id="gemini_analyse" type="analyse" niveau="⛧1">
        <analyse>
            <contexte>Système en fonctionnement normal</contexte>
            <observations>Performance stable, utilisation CPU 45%</observations>
            <tendances>Légère augmentation mémoire</tendances>
            <risques>Espace disque à surveiller</risques>
        </analyse>
        <recommandations>
            <priorite_haute>Nettoyer logs anciens</priorite_haute>
            <priorite_moyenne>Optimiser cache</priorite_moyenne>
        </recommandations>
        <commande>sendMessage("shadeos", "Analyse terminée: système stable, recommande nettoyage logs")</commande>
    </luciform>
    """
    
    resultats_gemini = parser.parse_reponse(reponse_gemini, "gemini")
    
    # Traiter l'analyse
    if resultats_gemini.get('analyse'):
        dm.mettre_a_jour_analyse("gemini", resultats_gemini['analyse'])
        print("   ✅ Analyse Gemini enregistrée")
    
    # Traiter les messages
    messages_gemini = dm.traiter_send_messages(resultats_gemini['send_messages'])
    print(f"   ✅ {len(messages_gemini)} message de retour")
    
    # Vérifier l'état final
    print("\n3️⃣ État final du système")
    stats_finales = dm.get_statistiques()
    print(f"   Messages total: {stats_finales['messages_total']}")
    print(f"   Entités avec analyse: {stats_finales.get('entites_avec_analyse', 0)}")
    
    # Afficher les fils de discussion
    print("\n📜 Fils de discussion:")
    for nom_entite in ["shadeos", "gemini"]:
        fil = dm.get_fil_discussion(nom_entite)
        if fil != "[Aucun message]":
            print(f"   {nom_entite}: {len(fil.split('\\n'))} messages")
    
    return True

if __name__ == "__main__":
    print("🧪 TESTS ARCHITECTURE DATA-DRIVEN V4")
    print("=" * 60)
    
    tests = [
        test_data_models,
        test_luciform_parser, 
        test_data_manager,
        test_integration_complete
    ]
    
    resultats = []
    for test in tests:
        try:
            resultat = test()
            resultats.append(resultat)
        except Exception as e:
            print(f"❌ Erreur dans {test.__name__}: {e}")
            resultats.append(False)
    
    print(f"\n🎉 RÉSULTATS: {sum(resultats)}/{len(resultats)} tests réussis")
    
    if all(resultats):
        print("✅ Architecture data-driven V4 fonctionnelle !")
    else:
        print("⚠️ Certains tests ont échoué")
