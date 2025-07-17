#!/usr/bin/env python3
"""
🧪 TEST OPENAI SIMPLE - Vérifier si ça fonctionne
"""

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent))

from core.cheat_orchestrator import CheatOrchestrator

def main():
    """Test simple avec OpenAI"""
    print("🧪 TEST OPENAI SIMPLE")
    print("="*50)
    
    # Supprimer l'ancien log
    log_file = Path("cheatcode_session.log")
    if log_file.exists():
        log_file.unlink()
        print("🗑️ Ancien log supprimé")
    
    # Créer l'orchestrateur
    print("\n🚀 Initialisation...")
    orchestrator = CheatOrchestrator("prompts")
    
    # Test démarrage OpenAI
    print("\n🌟 Test démarrage OpenAI...")
    try:
        result = orchestrator.engine.demarrer_gemini_cli()
        print(f"Résultat: {result}")
    except Exception as e:
        print(f"❌ Erreur attendue: {e}")
    
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
