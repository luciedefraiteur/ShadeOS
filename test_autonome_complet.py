#!/usr/bin/env python3
"""
🎮 TEST AUTONOME COMPLET - SHADEOS LIVRÉ À LUI-MÊME
"""

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent))

from core.cheat_orchestrator import CheatOrchestrator

def main():
    """Test autonome complet - ShadEOS fait ce qu'il veut"""
    print("🎮 TEST AUTONOME COMPLET - SHADEOS LIVRÉ À LUI-MÊME")
    print("="*70)
    print("🎯 Objectif: Voir ce que ShadEOS fait quand il a tous les pouvoirs")
    print("💝 Pour: Lucie Defraiteur, sa créatrice adorée")
    print("="*70)
    
    # Supprimer l'ancien log
    log_file = Path("cheatcode_session.log")
    if log_file.exists():
        log_file.unlink()
        print("🗑️ Ancien log supprimé")
    
    # Créer l'orchestrateur
    print("\n🚀 Initialisation CheatCode V4...")
    orchestrator = CheatOrchestrator("prompts")
    
    # Générer le prompt pour ShadEOS
    print("\n📝 Génération du prompt pour ShadEOS...")
    prompt = orchestrator.generer_prompt_shadeos()
    print(f"✅ Prompt généré: {len(prompt)} caractères")
    
    # Envoyer le prompt à OpenAI pour obtenir la réponse de ShadEOS
    print("\n🌟 Envoi du prompt à OpenAI (ShadEOS)...")
    print("💭 ShadEOS va décider quoi faire avec tous ses pouvoirs...")
    
    try:
        from openai import OpenAI
        import os
        
        # Configuration OpenAI
        api_key = os.environ.get('OPENAI_API_KEY')
        client = OpenAI(api_key=api_key)
        
        # Appel RÉEL à OpenAI avec le prompt CheatCode
        print("🚀 Appel RÉEL à OpenAI...")
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Tu es ShadEOS en mode CheatCode. Tu as tous les pouvoirs listés dans le prompt. Utilise-les pour accomplir quelque chose d'utile pour Lucie Defraiteur. Réponds EXACTEMENT selon le format luciform XML demandé."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=1500,
            temperature=0.8
        )
        
        # Récupérer la VRAIE réponse de ShadEOS
        reponse_shadeos = response.choices[0].message.content
        tokens_used = response.usage.total_tokens
        
        print(f"✅ Réponse reçue de ShadEOS ({tokens_used} tokens)")
        print(f"📏 Longueur: {len(reponse_shadeos)} caractères")
        
        print(f"\n📋 RÉPONSE DE SHADEOS:")
        print("="*70)
        print(reponse_shadeos)
        print("="*70)
        
        # Exécuter la réponse de ShadEOS
        print(f"\n🚀 EXÉCUTION DES ACTIONS DE SHADEOS...")
        print("⚡ ShadEOS prend le contrôle...")
        
        resultats = orchestrator.executer_reponse_shadeos(reponse_shadeos)
        
        print(f"\n📊 RÉSULTATS DE L'EXÉCUTION:")
        print(f"✅ Succès global: {resultats['success']}")
        print(f"📈 Actions exécutées: {resultats['actions_executees']}")
        print(f"🎯 Actions réussies: {resultats['actions_reussies']}")
        print(f"🧠 Analyse ShadEOS: {resultats.get('analyse_situation', 'N/A')}")
        print(f"📋 Plan ShadEOS: {resultats.get('plan_global', 'N/A')}")
        
        # Afficher les détails de chaque action
        print(f"\n🔍 DÉTAILS DES ACTIONS EXÉCUTÉES:")
        for i, resultat in enumerate(resultats.get('resultats_actions', [])):
            print(f"\n   Action {i+1}:")
            print(f"   ✅ Succès: {resultat.get('success', False)}")
            if 'output' in resultat:
                output_preview = resultat['output'][:200] + "..." if len(resultat['output']) > 200 else resultat['output']
                print(f"   📤 Output: {output_preview}")
            if 'error' in resultat:
                print(f"   ❌ Erreur: {resultat['error']}")
        
        print(f"\n💰 Coût: {tokens_used} tokens OpenAI utilisés")
        
    except Exception as e:
        print(f"❌ Erreur durant l'appel OpenAI: {e}")
        return
    
    # Afficher le log complet
    print(f"\n📚 LOG COMPLET DE LA SESSION:")
    print("="*70)
    
    try:
        with open("cheatcode_session.log", 'r', encoding='utf-8') as f:
            log_content = f.read()
        print(log_content)
    except Exception as e:
        print(f"❌ Erreur lecture log: {e}")
    
    print("="*70)
    print("🎉 TEST AUTONOME TERMINÉ")
    print("💝 ShadEOS a agi en totale autonomie avec tous ses pouvoirs !")
    print("📋 Vérifiez les fichiers créés et les actions exécutées")

if __name__ == "__main__":
    main()
