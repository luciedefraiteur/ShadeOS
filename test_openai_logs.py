#!/usr/bin/env python3
"""
🧪 TEST COMPLET - OPENAI RÉEL + LOGS AUTOMATIQUES
"""

import sys
import os
from pathlib import Path
sys.path.append(str(Path(__file__).parent))

from core.cheat_orchestrator import CheatOrchestrator

def verifier_openai():
    """Vérifie si OpenAI est disponible"""
    try:
        import openai
        api_key = os.environ.get('OPENAI_API_KEY')
        if not api_key:
            print("❌ Variable OPENAI_API_KEY non définie")
            print("💡 Définissez-la avec: export OPENAI_API_KEY='votre_clé'")
            return False
        print(f"✅ Clé OpenAI trouvée: {api_key[:10]}...")
        return True
    except ImportError:
        print("❌ Module openai non installé")
        print("💡 Installez-le avec: pip install openai")
        return False

def main():
    """Test complet avec OpenAI réel et logs automatiques"""
    print("🧪 TEST COMPLET - OPENAI RÉEL + LOGS AUTOMATIQUES")
    print("="*70)
    
    # Vérifier OpenAI
    if not verifier_openai():
        print("\n⚠️ OpenAI non disponible - Test avec logs seulement")
        test_sans_openai = True
    else:
        test_sans_openai = False
    
    # Créer l'orchestrateur
    print("\n🚀 Initialisation avec logs automatiques...")
    orchestrator = CheatOrchestrator("prompts")
    
    # Test avec logs automatiques
    print("\n📝 Test avec actions réelles et logs automatiques...")
    
    if test_sans_openai:
        # Test sans OpenAI mais avec logs complets
        reponse_test = """
        <luciform id="test_logs" type="mode_cheat" niveau="⛧∞">
            <analyse_situation>Test des logs automatiques sans OpenAI</analyse_situation>
            
            <action_shell>
                <commande>echo "Test logs automatiques - $(date)"</commande>
                <objectif>Test shell avec timestamp</objectif>
            </action_shell>
            
            <action_write_file>
                <fichier>test_logs_output.txt</fichier>
                <mode>entier</mode>
                <contenu>🧪 TEST LOGS AUTOMATIQUES
Fichier créé par CheatCode V4
Date: $(date)
Logs: Tous les détails sont dans cheatcode_session.log
Status: Logs automatiques ACTIVÉS</contenu>
                <objectif>Créer fichier avec logs automatiques</objectif>
            </action_write_file>
            
            <action_shell>
                <commande>ls -la test_logs_output.txt</commande>
                <objectif>Vérifier le fichier créé</objectif>
            </action_shell>
            
            <action_read_file>
                <fichier>test_logs_output.txt</fichier>
                <mode>entier</mode>
                <objectif>Lire le fichier créé</objectif>
            </action_read_file>
            
            <plan_global>Test complet des logs automatiques</plan_global>
        </luciform>
        """
    else:
        # Test avec OpenAI réel
        reponse_test = """
        <luciform id="test_openai_logs" type="mode_cheat" niveau="⛧∞">
            <analyse_situation>Test complet avec OpenAI RÉEL et logs automatiques</analyse_situation>
            
            <action_gemini>
                <message_pour_gemini>Analyse ce projet CheatCode V4 et donne 3 recommandations d'amélioration</message_pour_gemini>
                <objectif>Test RÉEL d'OpenAI</objectif>
            </action_gemini>
            
            <action_shell>
                <commande>echo "Test avec OpenAI réel - $(date)"</commande>
                <objectif>Test shell avec OpenAI</objectif>
            </action_shell>
            
            <action_write_file>
                <fichier>test_openai_logs.txt</fichier>
                <mode>entier</mode>
                <contenu>🌟 TEST OPENAI + LOGS AUTOMATIQUES
Fichier créé par CheatCode V4
Date: $(date)
OpenAI: ACTIVÉ et testé
Logs: Complets dans cheatcode_session.log</contenu>
                <objectif>Créer fichier avec OpenAI</objectif>
            </action_write_file>
            
            <plan_global>Test complet OpenAI + logs automatiques</plan_global>
        </luciform>
        """
    
    print("📝 Exécution de la réponse ShadEOS...")
    resultats = orchestrator.executer_reponse_shadeos(reponse_test)
    
    print(f"\n📊 RÉSULTATS:")
    print(f"✅ Succès: {resultats['success']}")
    print(f"📈 Actions: {resultats['actions_executees']}")
    print(f"🎯 Réussies: {resultats['actions_reussies']}")
    
    # Afficher le contenu du fichier de log
    print(f"\n📚 CONTENU DU FICHIER LOG AUTOMATIQUE:")
    print("="*70)
    
    try:
        with open("cheatcode_session.log", 'r', encoding='utf-8') as f:
            log_content = f.read()
        print(log_content)
    except Exception as e:
        print(f"❌ Erreur lecture log: {e}")
    
    print("="*70)
    
    # Vérifier les fichiers créés
    print(f"\n📁 FICHIERS CRÉÉS:")
    for fichier in ["test_logs_output.txt", "test_openai_logs.txt", "cheatcode_session.log"]:
        if Path(fichier).exists():
            taille = Path(fichier).stat().st_size
            print(f"✅ {fichier}: {taille} octets")
        else:
            print(f"❌ {fichier}: non trouvé")
    
    print(f"\n🎉 Test terminé - Vérifiez cheatcode_session.log pour tous les détails")
    
    if not test_sans_openai:
        print("💰 Note: Ce test a utilisé de vrais tokens OpenAI")

if __name__ == "__main__":
    main()
