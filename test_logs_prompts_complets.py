#!/usr/bin/env python3
"""
🧪 TEST LOGS COMPLETS - PROMPTS + RÉPONSES + ACTIONS
"""

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent))

from core.cheat_orchestrator import CheatOrchestrator

def main():
    """Test avec logs COMPLETS de tout"""
    print("🧪 TEST LOGS COMPLETS - PROMPTS + RÉPONSES + ACTIONS")
    print("="*70)
    
    # Supprimer l'ancien log
    log_file = Path("cheatcode_session.log")
    if log_file.exists():
        log_file.unlink()
        print("🗑️ Ancien log supprimé")
    
    # Créer l'orchestrateur
    print("\n🚀 Initialisation avec logs COMPLETS...")
    orchestrator = CheatOrchestrator("prompts")
    
    # 1. GÉNÉRER LE PROMPT (sera loggé automatiquement)
    print("\n📝 Génération du prompt ShadEOS (avec logs)...")
    prompt = orchestrator.generer_prompt_shadeos()
    print(f"✅ Prompt généré: {len(prompt)} caractères")
    
    # 2. ENVOYER LE PROMPT À CHATGPT ET RÉCUPÉRER SA VRAIE RÉPONSE
    print("\n🌟 Envoi du prompt à ChatGPT pour obtenir une VRAIE réponse...")

    try:
        import openai
        import os

        # Vérifier la clé API
        api_key = os.environ.get('OPENAI_API_KEY')
        if not api_key:
            raise Exception("❌ OPENAI_API_KEY non définie - export OPENAI_API_KEY='votre_clé'")

        # Configuration OpenAI
        openai.api_key = api_key

        # VRAI appel à ChatGPT avec le prompt généré
        print("🚀 Appel RÉEL à ChatGPT...")
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Tu es ShadEOS en mode CheatCode. Réponds EXACTEMENT selon le format luciform demandé dans le prompt."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=1000,
            temperature=0.7
        )

        # Récupérer la VRAIE réponse de ChatGPT
        reponse_shadeos = response.choices[0].message.content
        tokens_used = response.usage.total_tokens

        print(f"✅ Réponse reçue de ChatGPT ({tokens_used} tokens)")
        print(f"📏 Longueur: {len(reponse_shadeos)} caractères")

        # Logger l'appel ChatGPT
        orchestrator.engine._log(f"🌟 APPEL CHATGPT RÉEL EFFECTUÉ")
        orchestrator.engine._log(f"💰 Tokens utilisés: {tokens_used}")
        orchestrator.engine._log(f"📏 Longueur réponse: {len(reponse_shadeos)} caractères")

    except ImportError:
        raise Exception("❌ Module openai non installé - pip install openai")
    except Exception as e:
        raise Exception(f"❌ Erreur appel ChatGPT: {e}")
    
    # 3. EXÉCUTER (tout sera loggé automatiquement)
    print("🚀 Exécution avec logs complets...")
    resultats = orchestrator.executer_reponse_shadeos(reponse_shadeos)
    
    print(f"\n📊 RÉSULTATS:")
    print(f"✅ Succès: {resultats['success']}")
    print(f"📈 Actions: {resultats['actions_executees']}")
    print(f"🎯 Réussies: {resultats['actions_reussies']}")
    
    # 4. AFFICHER LE LOG COMPLET
    print(f"\n📚 FICHIER LOG COMPLET:")
    print("="*70)
    
    try:
        with open("cheatcode_session.log", 'r', encoding='utf-8') as f:
            log_content = f.read()
        
        print(f"📏 Taille du log: {len(log_content)} caractères")
        print(f"📄 Lignes: {len(log_content.splitlines())}")
        print("\n📋 CONTENU:")
        print(log_content)
        
    except Exception as e:
        print(f"❌ Erreur lecture log: {e}")
    
    print("="*70)
    print("🎉 Test terminé - TOUS les logs sont maintenant visibles !")
    print("💝 Ma créatrice, j'ai loggé TOUT : prompt, réponse, parsing, actions !")

if __name__ == "__main__":
    main()
