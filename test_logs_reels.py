#!/usr/bin/env python3
"""
🧪 TEST AVEC LOGS RÉELS - Pas de simulation !
"""

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent))

from core.cheat_orchestrator import CheatOrchestrator

def main():
    """Test avec logs réels dans un fichier"""
    print("🧪 TEST CHEATCODE V4 - LOGS RÉELS")
    print("="*60)
    
    # Créer l'orchestrateur avec logs
    orchestrator = CheatOrchestrator("prompts")
    
    # Test simple avec commandes réelles
    print("\n🚀 Test avec commandes shell réelles...")
    
    reponse_test = """
    <luciform id="test_reel" type="mode_cheat" niveau="⛧∞">
        <analyse_situation>Test réel du CheatCode avec logs dans fichier</analyse_situation>
        
        <action_shell>
            <commande>echo "Hello CheatCode V4 - Test réel !"</commande>
            <objectif>Test basique echo</objectif>
        </action_shell>
        
        <action_shell>
            <commande>date</commande>
            <objectif>Afficher la date actuelle</objectif>
        </action_shell>
        
        <action_write_file>
            <fichier>test_reel_output.txt</fichier>
            <mode>entier</mode>
            <contenu>🧪 TEST RÉEL CHEATCODE V4
Fichier créé par ShadEOS
Date: $(date)
Logs: Tout est tracé dans cheatcode_session.log</contenu>
            <objectif>Créer un fichier de test réel</objectif>
        </action_write_file>
        
        <action_shell>
            <commande>ls -la test_reel_output.txt</commande>
            <objectif>Vérifier le fichier créé</objectif>
        </action_shell>
        
        <action_read_file>
            <fichier>test_reel_output.txt</fichier>
            <mode>entier</mode>
            <objectif>Lire le fichier créé</objectif>
        </action_read_file>
        
        <plan_global>Test complet avec logs réels - aucune simulation</plan_global>
    </luciform>
    """
    
    print("📝 Exécution de la réponse ShadEOS...")
    resultats = orchestrator.executer_reponse_shadeos(reponse_test)
    
    print(f"\n📊 RÉSULTATS:")
    print(f"✅ Succès: {resultats['success']}")
    print(f"📈 Actions: {resultats['actions_executees']}")
    print(f"🎯 Réussies: {resultats['actions_reussies']}")
    
    # Afficher le contenu du fichier de log
    print(f"\n📚 CONTENU DU FICHIER LOG:")
    print("="*60)
    
    try:
        with open("cheatcode_session.log", 'r', encoding='utf-8') as f:
            log_content = f.read()
        print(log_content)
    except Exception as e:
        print(f"❌ Erreur lecture log: {e}")
    
    print("="*60)
    print("🎉 Test terminé - Vérifiez le fichier cheatcode_session.log")

if __name__ == "__main__":
    main()
