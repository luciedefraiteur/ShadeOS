import os
import sys
from pathlib import Path
import json

sys.path.append(str(Path(__file__).parent.parent / "@Alma"))
from env_loader_unifie import get_alma_env_loader

def ask_openai_about_report():
    report_path = Path(__file__).parent.parent / "RAPPORT_GEMINI.md"
    if not report_path.exists():
        print(f"Erreur: Le rapport {report_path} n'existe pas.")
        return

    try:
        with open(report_path, 'r', encoding='utf-8') as f:
            report_content = f.read()

        alma_loader = get_alma_env_loader()
        alma_loader.force_crash_if_not_ready()

        messages = [
            {
                "role": "system",
                "content": "Tu es un expert en architecture logicielle et en IA autonome. Analyse le rapport suivant et fournis des conseils et des suggestions pour améliorer l'autonomie de ShadEOS V666. Concentre-toi sur des solutions concrètes et des étapes d'implémentation."
            },
            {
                "role": "user",
                "content": report_content
            }
        ]

        print("Envoi du rapport à OpenAI pour analyse...")
        result = alma_loader.call_openai_real(
            messages=messages,
            model="gpt-4o",  # Utilisation d'un modèle plus avancé pour une meilleure analyse
            max_tokens=2000,
            temperature=0.7
        )

        print("\nRéponse d'OpenAI :\n")
        print(result['response'])
        print(f"\nTokens utilisés : {result['tokens_used']}")

    except Exception as e:
        print(f"Erreur lors de l'envoi du rapport à OpenAI : {e}")

if __name__ == "__main__":
    ask_openai_about_report()
