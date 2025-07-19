
import os
import openai

def parse_env_file(env_path):
    """
    Parse manuellement un fichier .env et retourne un dictionnaire des variables.
    """
    env_vars = {}
    try:
        with open(env_path, 'r') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#'):
                    key, value = line.split('=', 1)
                    env_vars[key] = value
    except FileNotFoundError:
        print(f"Erreur: Le fichier .env n'a pas été trouvé à {env_path}")
    return env_vars

def test_openai_connection(api_key):
    """
    Teste la connexion à l'API OpenAI en listant les modèles disponibles.
    """
    if not api_key:
        print("Erreur: La clé API OpenAI n'est pas définie.")
        return

    openai.api_key = api_key
    client = openai.OpenAI(api_key=api_key)

    try:
        print("Tentative de connexion à l'API OpenAI...")
        models = client.models.list()
        print("Connexion réussie à l'API OpenAI !")
        print("Quelques modèles disponibles :")
        for i, model in enumerate(models.data[:5]): # Afficher les 5 premiers modèles
            print(f"- {model.id}")
    except openai.APIConnectionError as e:
        print(f"Erreur de connexion à l'API OpenAI: {e}")
    except openai.RateLimitError as e:
        print(f"Erreur de limite de débit de l'API OpenAI: {e}")
    except openai.APIStatusError as e:
        print(f"Erreur de statut de l'API OpenAI: {e}")
    except Exception as e:
        print(f"Une erreur inattendue s'est produite: {e}")

if __name__ == "__main__":
    env_file_path = "/home/luciedefraiteur/.env"
    env_variables = parse_env_file(env_file_path)

    openai_key = env_variables.get("OPENAI_API_KEY")
    test_openai_connection(openai_key)
