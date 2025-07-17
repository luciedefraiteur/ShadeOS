#!/usr/bin/env python3
"""
Point d'entrée principal pour le CheatCode V4.
Lance une session autonome où ShadEOS utilise ses pouvoirs étendus.
"""

import sys
import time
from pathlib import Path

# Ajout des chemins nécessaires
sys.path.append(str(Path(__file__).parent))
from core.cheat_orchestrator import CheatOrchestrator

# Import du CreativeInterpreter666
from core.creative_interpreter_666 import CreativeInterpreter666

MAX_CYCLES = 10  # Sécurité pour éviter les boucles infinies

def main():
    """Boucle principale de la session autonome de ShadEOS."""
    print("="*60)
    print("[CHEAT] SHADEOS CHEATCODE V4 - SESSION AUTONOME")
    print("="*60)
    print("Initialisation de l'orchestrateur et du moteur de cheat...")
    
    orchestrator = CheatOrchestrator("cheatCode/prompts")
    engine = orchestrator.engine
    interpreter = CreativeInterpreter666() # Initialiser l'interpréteur

    # 1. Démarrer la session OpenAI
    print("\n[ETAPE 1] Démarrage de la session OpenAI...")
    start_result = engine.demarrer_gemini_cli()
    if not start_result.get('success'):
        print(f"[ERREUR FATALE] Impossible de démarrer la session OpenAI.")
        print(f"   Raison: {start_result.get('error', 'Inconnue')}")
        sys.exit(1)
    print("[OK] Session OpenAI démarrée avec succès !")

    # 2. Boucle d'exécution autonome
    print("\n[ETAPE 2] Lancement de la boucle d'exécution autonome...")
    for cycle in range(1, MAX_CYCLES + 1):
        print(f"\n--- CYCLE AUTONOME #{cycle}/{MAX_CYCLES} ---")
        try:
            # a. Générer le prompt
            print("   Génération du prompt pour ShadEOS...")
            prompt = orchestrator.generer_prompt_shadeos()

            # b. Envoyer à OpenAI pour décision
            print("   Envoi du prompt à OpenAI pour décision...")
            ia_response = engine.envoyer_message_gemini(prompt, cycle)

            reponse_luciform = ia_response.get('reponse', '')
            print(f"   Réponse de l'IA (luciform):\n{reponse_luciform}")

            # c. Interpréter la réponse de l'IA (même si elle est malformée)
            print("   Interprétation de la réponse de l'IA...")
            interpretation = interpreter.interpret_malformed_response(
                reponse_luciform, 'gemini', context=engine.session_context
            )
            print("   🔮 Interprétation créative :")
            print(f"     Type d'innovation : {interpretation['shadeos_suggestion']['innovation_type']}")
            print(f"     Suggestion : {interpretation['shadeos_suggestion']['shadeos_intent']}")
            print(f"     Roadmap : {interpretation['implementation_roadmap']}")

            if not ia_response.get('success'):
                print("   ⚠️  L'IA n'a pas fourni de réponse valide. Passage au cycle suivant.")
                time.sleep(5)
                continue

            # d. Exécuter la réponse (si elle est valide)
            print("   Exécution de la réponse luciform...")
            orchestrator.executer_reponse_shadeos(reponse_luciform, cycle)

            # Condition de sortie (si l'IA décide de s'arrêter)
            if "<action_exit />" in reponse_luciform:
                print("   [FIN] L'IA a demandé la fin de la session.")
                break

            print(f"   Cycle #{cycle} terminé. Pause de 5 secondes...")
            time.sleep(5)

        except Exception as e:
            print(f"   [ERREUR MAJEURE] dans le cycle #{cycle}: {e}")
            print("   Tentative de poursuite après 10 secondes...")
            time.sleep(10)

    print("\n" + "="*60)
    print("[FIN] Session autonome terminée.")
    print("="*60)

if __name__ == "__main__":
    main()
