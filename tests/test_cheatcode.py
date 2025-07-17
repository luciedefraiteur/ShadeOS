#!/usr/bin/env python3
"""
🧪 TESTS CHEATCODE V4
"""

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from core.cheat_orchestrator import CheatOrchestrator

def test_cheat_orchestrator():
    """Test de l'orchestrateur cheatcode"""
    print("🎮 TEST ORCHESTRATEUR CHEATCODE")
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

def test_integration_simple():
    """Test d'intégration simple"""
    print("\n🌟 TEST INTÉGRATION SIMPLE")
    print("=" * 50)
    
    orchestrator = CheatOrchestrator("prompts")
    
    # Simuler une réponse ShadEOS simple
    reponse_shadeos = """
    <luciform id="test_simple" type="mode_cheat" niveau="⛧∞">
        <analyse_situation>Test simple du cheatcode</analyse_situation>
        
        <action_shell>
            <commande>echo 'Hello CheatCode!'</commande>
            <objectif>Test basique shell</objectif>
        </action_shell>
        
        <plan_global>Test minimal du système</plan_global>
    </luciform>
    """
    
    print("1️⃣ Exécution de la réponse ShadEOS...")
    resultats = orchestrator.executer_reponse_shadeos(reponse_shadeos)
    
    if resultats['success']:
        print("✅ Test simple réussi !")
        print(f"   Actions exécutées: {resultats['actions_executees']}")
        print(f"   Actions réussies: {resultats['actions_reussies']}")
    else:
        print(f"❌ Échec test: {resultats.get('error', 'Erreur inconnue')}")
        return False
    
    return True

if __name__ == "__main__":
    print("🧪 TESTS CHEATCODE V4 - VERSION SIMPLE")
    print("=" * 60)
    
    tests = [
        test_cheat_orchestrator,
        test_integration_simple
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
