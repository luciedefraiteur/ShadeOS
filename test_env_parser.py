#!/usr/bin/env python3
"""
🧪 TEST PARSER .env MANUEL
"""

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent))

from core.cheat_orchestrator import CheatOrchestrator

def main():
    """Test avec parser .env manuel"""
    print("🧪 TEST PARSER .env MANUEL")
    print("="*50)
    
    # Supprimer l'ancien log
    log_file = Path("cheatcode_session.log")
    if log_file.exists():
        log_file.unlink()
        print("🗑️ Ancien log supprimé")
    
    # Créer l'orchestrateur (va charger .env automatiquement)
    print("\n🚀 Initialisation avec chargement .env...")
    orchestrator = CheatOrchestrator("prompts")
    
    # Vérifier les variables chargées
    import os
    print(f"\n🔍 Variables après chargement:")
    for key in ['OPENAI_API_KEY', 'ANTHROPIC_API_KEY', 'GOOGLE_API_KEY']:
        value = os.environ.get(key)
        if value:
            print(f"✅ {key}: {value[:10]}...")
        else:
            print(f"❌ {key}: Non définie")
    
    # Test démarrage OpenAI
    print("\n🌟 Test démarrage OpenAI...")
    try:
        result = orchestrator.engine.demarrer_gemini_cli()
        print(f"✅ Résultat: {result}")
    except Exception as e:
        print(f"❌ Erreur: {e}")
    
    # Afficher le log
    print(f"\n📚 CONTENU DU LOG:")
    print("="*50)
    
    try:
        with open("cheatcode_session.log", 'r', encoding='utf-8') as f:
            log_content = f.read()
        print(log_content)
    except Exception as e:
        print(f"❌ Erreur lecture log: {e}")
    
    print("="*50)
    print("🎉 Test terminé")

if __name__ == "__main__":
    main()
