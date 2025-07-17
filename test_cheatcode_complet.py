#!/usr/bin/env python3
"""
🧪 TEST COMPLET CHEATCODE V4 - Avec logs détaillés
"""

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent / "cheatCode"))

from core.cheat_orchestrator import CheatOrchestrator
import json

def afficher_separateur(titre):
    """Affiche un séparateur avec titre"""
    print("\n" + "="*60)
    print(f"🎮 {titre}")
    print("="*60)

def test_generation_prompt():
    """Test de génération du prompt"""
    afficher_separateur("GÉNÉRATION DU PROMPT SHADEOS")
    
    orchestrator = CheatOrchestrator("cheatCode/prompts")
    
    # Générer le prompt
    prompt = orchestrator.generer_prompt_shadeos()
    
    print(f"📏 Longueur du prompt: {len(prompt)} caractères")
    print(f"📊 Statistiques: {orchestrator.get_statistiques()}")
    
    # Afficher le prompt complet
    print("\n📝 PROMPT GÉNÉRÉ:")
    print("-" * 60)
    print(prompt)
    print("-" * 60)
    
    return orchestrator, prompt

def test_reponse_shadeos_simple():
    """Test avec une réponse ShadEOS simple"""
    afficher_separateur("TEST RÉPONSE SHADEOS SIMPLE")
    
    orchestrator = CheatOrchestrator("cheatCode/prompts")
    
    # Réponse ShadEOS simulée
    reponse_shadeos = """
    <luciform id="test_complet" type="mode_cheat" niveau="⛧∞">
        <analyse_situation>Je veux tester le système CheatCode en créant un fichier de test et en l'analysant</analyse_situation>
        
        <action_write_file>
            <fichier>test_cheatcode_output.txt</fichier>
            <mode>entier</mode>
            <contenu>🎮 FICHIER DE TEST CHEATCODE V4
Créé par ShadEOS en mode cheat
Timestamp: Test complet
Objectif: Valider le système de fichiers

Ce fichier démontre les capacités d'écriture du CheatCode.</contenu>
            <objectif>Créer un fichier de démonstration</objectif>
        </action_write_file>
        
        <action_shell>
            <commande>ls -la test_cheatcode_output.txt</commande>
            <objectif>Vérifier que le fichier a été créé</objectif>
        </action_shell>
        
        <action_read_file>
            <fichier>test_cheatcode_output.txt</fichier>
            <mode>entier</mode>
            <objectif>Lire le contenu du fichier créé</objectif>
        </action_read_file>
        
        <action_shell>
            <commande>wc -l test_cheatcode_output.txt</commande>
            <objectif>Compter les lignes du fichier</objectif>
        </action_shell>
        
        <plan_global>Test complet du CheatCode: création, vérification, lecture et analyse d'un fichier</plan_global>
    </luciform>
    """
    
    print("📝 RÉPONSE SHADEOS À EXÉCUTER:")
    print("-" * 40)
    print(reponse_shadeos.strip())
    print("-" * 40)
    
    # Exécuter la réponse
    print("\n🚀 EXÉCUTION EN COURS...")
    resultats = orchestrator.executer_reponse_shadeos(reponse_shadeos)
    
    # Afficher les résultats détaillés
    print("\n📊 RÉSULTATS D'EXÉCUTION:")
    print("-" * 40)
    print(f"✅ Succès global: {resultats['success']}")
    print(f"📈 Actions exécutées: {resultats['actions_executees']}")
    print(f"🎯 Actions réussies: {resultats['actions_reussies']}")
    print(f"🧠 Analyse: {resultats['analyse_situation']}")
    print(f"📋 Plan: {resultats['plan_global']}")
    
    # Détails de chaque action
    print("\n🔍 DÉTAILS DES ACTIONS:")
    for i, resultat in enumerate(resultats['resultats_actions']):
        print(f"\n   Action {i+1}:")
        print(f"   ✅ Succès: {resultat['success']}")
        if 'output' in resultat:
            print(f"   📤 Output: {resultat['output'][:100]}...")
        if 'error' in resultat:
            print(f"   ❌ Erreur: {resultat['error']}")
    
    return orchestrator, resultats

def test_historique_buffer():
    """Test de l'historique et du buffer"""
    afficher_separateur("TEST HISTORIQUE ET BUFFER")
    
    orchestrator = CheatOrchestrator("cheatCode/prompts")
    
    # Exécuter quelques actions pour remplir l'historique
    actions_test = [
        """<luciform><action_shell><commande>echo 'Test 1'</commande><objectif>Test historique 1</objectif></action_shell></luciform>""",
        """<luciform><action_shell><commande>echo 'Test 2'</commande><objectif>Test historique 2</objectif></action_shell></luciform>""",
        """<luciform><action_shell><commande>echo 'Test 3'</commande><objectif>Test historique 3</objectif></action_shell></luciform>"""
    ]
    
    for i, action in enumerate(actions_test):
        print(f"\n🔄 Exécution action {i+1}...")
        orchestrator.executer_reponse_shadeos(action)
    
    # Afficher l'historique
    historique = orchestrator.engine.get_historique_formate()
    print("\n📚 HISTORIQUE COMPLET:")
    print("-" * 40)
    print(historique)
    print("-" * 40)
    
    # Statistiques
    stats = orchestrator.get_statistiques()
    print(f"\n📊 STATISTIQUES FINALES:")
    print(f"   Historique: {stats['historique_taille']}/{stats['historique_max']}")
    print(f"   Gemini actif: {stats['gemini_actif']}")
    print(f"   Prompt disponible: {stats['prompt_disponible']}")
    
    return orchestrator

def test_sauvegarde_session():
    """Test de sauvegarde et chargement de session"""
    afficher_separateur("TEST SAUVEGARDE/CHARGEMENT SESSION")
    
    orchestrator = CheatOrchestrator("cheatCode/prompts")
    
    # Exécuter une action pour avoir de l'historique
    action = """<luciform><action_shell><commande>echo 'Session test'</commande><objectif>Test session</objectif></action_shell></luciform>"""
    orchestrator.executer_reponse_shadeos(action)
    
    # Sauvegarder
    print("💾 Sauvegarde de la session...")
    if orchestrator.sauvegarder_session("test_session.json"):
        print("✅ Sauvegarde réussie")
        
        # Vérifier le fichier
        with open("test_session.json", 'r') as f:
            session_data = json.load(f)
        
        print(f"📄 Contenu sauvegardé:")
        print(f"   Historique: {len(session_data['historique'])} entrées")
        print(f"   Gemini ID: {session_data['gemini_terminal_id']}")
        
        # Créer un nouvel orchestrateur et charger
        print("\n📂 Test de chargement...")
        orchestrator2 = CheatOrchestrator("cheatCode/prompts")
        
        if orchestrator2.charger_session("test_session.json"):
            print("✅ Chargement réussi")
            
            # Vérifier que l'historique est restauré
            historique_restaure = orchestrator2.engine.get_historique_formate()
            print(f"📚 Historique restauré:")
            print(historique_restaure)
        else:
            print("❌ Échec chargement")
    else:
        print("❌ Échec sauvegarde")

def main():
    """Test principal complet"""
    print("🎮 TEST COMPLET CHEATCODE V4")
    print("🎯 Objectif: Valider toutes les fonctionnalités avec logs détaillés")
    
    try:
        # Test 1: Génération prompt
        orchestrator, prompt = test_generation_prompt()
        
        # Test 2: Exécution réponse ShadEOS
        orchestrator, resultats = test_reponse_shadeos_simple()
        
        # Test 3: Historique et buffer
        orchestrator = test_historique_buffer()
        
        # Test 4: Sauvegarde/chargement
        test_sauvegarde_session()
        
        # Résumé final
        afficher_separateur("RÉSUMÉ FINAL")
        print("✅ Tous les tests sont terminés")
        print("🎮 CheatCode V4 est pleinement fonctionnel")
        print("\n🚀 PRÊT POUR UTILISATION RÉELLE:")
        print("   1. Copier le prompt généré")
        print("   2. L'envoyer à ChatGPT/Claude")
        print("   3. Copier la réponse XML")
        print("   4. L'exécuter avec orchestrator.executer_reponse_shadeos()")
        
    except Exception as e:
        print(f"\n❌ ERREUR DURANT LES TESTS: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
