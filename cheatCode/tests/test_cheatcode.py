#!/usr/bin/env python3
"""
🧪 TESTS CHEATCODE V4
"""

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from core.cheat_orchestrator import CheatOrchestrator
from core.cheat_parser import CheatParser
from core.cheat_engine import CheatEngine

def test_cheat_engine():
    """Test du moteur cheatcode"""
    print("🧪 TEST MOTEUR CHEATCODE")
    print("=" * 50)
    
    engine = CheatEngine(buffer_size=5)
    
    # Test shell
    result = engine.executer_shell("echo 'Hello CheatCode!'")
    print(f"✅ Shell: {result['success']}")
    print(f"   Output: {result['output'].strip()}")
    
    # Test écriture fichier
    result = engine.ecrire_fichier("test_cheat.txt", "Contenu de test", "entier")
    print(f"✅ Écriture: {result['success']}")
    
    # Test lecture fichier
    result = engine.lire_fichier("test_cheat.txt", "entier")
    print(f"✅ Lecture: {result['success']}")
    print(f"   Contenu: {result.get('contenu', '')}")
    
    # Test Python
    code_python = '''#!/usr/bin/env python3
print("Hello from CheatCode Python!")
'''
    result = engine.ecrire_python("test_cheat.py", code_python)
    print(f"✅ Python: {result['success']}")
    
    # Test historique
    historique = engine.get_historique_formate()
    print(f"✅ Historique: {len(historique.split('\\n'))} entrées")
    
    return True

def test_cheat_parser():
    """Test du parser cheatcode"""
    print("\n🔮 TEST PARSER CHEATCODE")
    print("=" * 50)
    
    parser = CheatParser()
    
    # Test parsing réponse complète
    reponse_test = """
    <luciform id="test_cheat" type="mode_cheat" niveau="⛧∞">
        <analyse_situation>Je veux analyser le projet et créer un script</analyse_situation>
        
        <action_shell>
            <commande>ls -la</commande>
            <objectif>Voir les fichiers du projet</objectif>
        </action_shell>
        
        <action_write_python>
            <fichier>analyse.py</fichier>
            <contenu>
print("Analyse du projet")
import os
print(f"Répertoire: {os.getcwd()}")
            </contenu>
            <objectif>Créer un script d'analyse</objectif>
        </action_write_python>
        
        <action_gemini>
            <message_pour_gemini>Analyse ce projet Python</message_pour_gemini>
            <objectif>Obtenir une vue d'expert</objectif>
        </action_gemini>
        
        <plan_global>Analyser le projet et créer des outils d'aide</plan_global>
    </luciform>
    """
    
    resultats = parser.parse_reponse_cheatcode(reponse_test)
    
    if 'error' not in resultats:
        print(f"✅ Parsing réussi")
        print(f"   Analyse: {resultats['analyse_situation']}")
        print(f"   Plan: {resultats['plan_global']}")
        print(f"   Actions: {len(resultats['actions'])}")
        
        for i, action in enumerate(resultats['actions']):
            print(f"   Action {i+1}: {action['type']} - {action.get('objectif', 'Pas d\\'objectif')}")
        
        # Test validation
        validation = parser.valider_actions(resultats['actions'])
        print(f"✅ Validation: {validation['valid']}")
        print(f"   Stats: {validation['stats']}")
        
        if validation['errors']:
            print(f"   Erreurs: {validation['errors']}")
        if validation['warnings']:
            print(f"   Warnings: {validation['warnings']}")
    else:
        print(f"❌ Erreur parsing: {resultats['error']}")
        return False
    
    return True

def test_cheat_orchestrator():
    """Test de l'orchestrateur cheatcode"""
    print("\n🎮 TEST ORCHESTRATEUR CHEATCODE")
    print("=" * 50)
    
    orchestrator = CheatOrchestrator("prompts")
    
    # Test génération prompt
    prompt = orchestrator.generer_prompt_shadeos()
    print(f"✅ Prompt généré: {len(prompt)} caractères")
    
    if "SHADEOS CHEATCODE" in prompt:
        print("   ✅ Contient le titre cheatcode")
    
    if "historique_buffer" in prompt:
        print("   ✅ Contient l'historique")
    
    # Test statistiques
    stats = orchestrator.get_statistiques()
    print(f"✅ Statistiques: {stats}")
    
    return True

def test_integration_complete():
    """Test d'intégration complète"""
    print("\n🌟 TEST INTÉGRATION CHEATCODE COMPLÈTE")
    print("=" * 50)
    
    orchestrator = CheatOrchestrator("prompts")
    
    # Simuler une réponse ShadEOS
    reponse_shadeos = """
    <luciform id="integration_test" type="mode_cheat" niveau="⛧∞">
        <analyse_situation>Test d'intégration du cheatcode - je veux créer un fichier de test et l'analyser</analyse_situation>
        
        <action_write_file>
            <fichier>integration_test.txt</fichier>
            <mode>entier</mode>
            <contenu>Fichier de test pour l'intégration CheatCode V4
Créé par ShadEOS en mode cheat
Timestamp: test</contenu>
            <objectif>Créer un fichier de test</objectif>
        </action_write_file>
        
        <action_shell>
            <commande>wc -l integration_test.txt</commande>
            <objectif>Compter les lignes du fichier créé</objectif>
        </action_shell>
        
        <action_read_file>
            <fichier>integration_test.txt</fichier>
            <mode>entier</mode>
            <objectif>Vérifier le contenu du fichier</objectif>
        </action_read_file>
        
        <plan_global>Test complet du système cheatcode avec création, analyse et lecture de fichier</plan_global>
    </luciform>
    """
    
    print("1️⃣ Exécution de la réponse ShadEOS...")
    resultats = orchestrator.executer_reponse_shadeos(reponse_shadeos)
    
    if resultats['success']:
        print("✅ Intégration réussie !")
        print(f"   Actions exécutées: {resultats['actions_executees']}")
        print(f"   Actions réussies: {resultats['actions_reussies']}")
        print(f"   Plan: {resultats['plan_global']}")
    else:
        print(f"❌ Échec intégration: {resultats.get('error', 'Erreur inconnue')}")
        return False
    
    print("\n2️⃣ Vérification de l'historique...")
    stats_finales = orchestrator.get_statistiques()
    print(f"   Historique: {stats_finales['historique_taille']} entrées")
    
    print("\n3️⃣ Test sauvegarde/chargement...")
    if orchestrator.sauvegarder_session("test_session.json"):
        print("   ✅ Sauvegarde réussie")
        
        # Créer un nouvel orchestrateur et charger
        orchestrator2 = CheatOrchestrator("prompts")
        if orchestrator2.charger_session("test_session.json"):
            print("   ✅ Chargement réussi")
        else:
            print("   ❌ Échec chargement")
            return False
    else:
        print("   ❌ Échec sauvegarde")
        return False
    
    return True

if __name__ == "__main__":
    print("🧪 TESTS CHEATCODE V4")
    print("=" * 60)
    
    tests = [
        test_cheat_engine,
        test_cheat_parser,
        test_cheat_orchestrator,
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
        print("✅ CheatCode V4 fonctionnel !")
        print("\n🎮 PRÊT POUR L'UTILISATION:")
        print("   1. Générer prompt avec orchestrator.generer_prompt_shadeos()")
        print("   2. Envoyer à ShadEOS (ChatGPT/Claude)")
        print("   3. Exécuter réponse avec orchestrator.executer_reponse_shadeos()")
    else:
        print("⚠️ Certains tests ont échoué")
