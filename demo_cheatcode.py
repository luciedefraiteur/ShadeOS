#!/usr/bin/env python3
"""
🎮 DÉMO CHEATCODE V4 - Test avec logs complets
"""

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent))

from core.cheat_orchestrator import CheatOrchestrator

def main():
    """Démo principale du CheatCode"""
    print("🎮 DÉMO CHEATCODE V4 - LOGS COMPLETS")
    print("="*60)
    
    # Créer l'orchestrateur
    print("🚀 Initialisation de l'orchestrateur...")
    orchestrator = CheatOrchestrator("prompts")
    
    # Générer le prompt
    print("\n📝 Génération du prompt ShadEOS...")
    prompt = orchestrator.generer_prompt_shadeos()
    
    print(f"✅ Prompt généré: {len(prompt)} caractères")
    print(f"📊 Stats: {orchestrator.get_statistiques()}")
    
    # Afficher le prompt complet
    print("\n" + "="*60)
    print("📋 PROMPT COMPLET POUR SHADEOS:")
    print("="*60)
    print(prompt)
    print("="*60)
    
    # Test d'exécution avec une réponse simulée
    print("\n🧪 TEST D'EXÉCUTION AVEC RÉPONSE SIMULÉE:")
    print("-"*60)
    
    reponse_test = """
    <luciform id="demo_test" type="mode_cheat" niveau="⛧∞">
        <analyse_situation>Démo du CheatCode - je veux créer un fichier de test et l'analyser</analyse_situation>
        
        <action_write_file>
            <fichier>demo_output.txt</fichier>
            <mode>entier</mode>
            <contenu>🎮 DÉMO CHEATCODE V4
Fichier créé par ShadEOS
Timestamp: Demo test
Capacités validées !</contenu>
            <objectif>Créer un fichier de démonstration</objectif>
        </action_write_file>
        
        <action_shell>
            <commande>ls -la demo_output.txt</commande>
            <objectif>Vérifier la création du fichier</objectif>
        </action_shell>
        
        <action_read_file>
            <fichier>demo_output.txt</fichier>
            <mode>entier</mode>
            <objectif>Lire le contenu créé</objectif>
        </action_read_file>
        
        <plan_global>Démonstration complète des capacités CheatCode</plan_global>
    </luciform>
    """
    
    print("📝 Réponse ShadEOS à exécuter:")
    print(reponse_test.strip())
    
    print("\n🚀 EXÉCUTION...")
    resultats = orchestrator.executer_reponse_shadeos(reponse_test)
    
    print("\n📊 RÉSULTATS:")
    print(f"✅ Succès: {resultats['success']}")
    print(f"📈 Actions: {resultats['actions_executees']}")
    print(f"🎯 Réussies: {resultats['actions_reussies']}")
    
    # Afficher l'historique
    print("\n📚 HISTORIQUE DES ACTIONS:")
    print("-"*40)
    historique = orchestrator.engine.get_historique_formate()
    print(historique)
    print("-"*40)
    
    print("\n🎉 DÉMO TERMINÉE - CHEATCODE V4 OPÉRATIONNEL !")

if __name__ == "__main__":
    main()
