
import os
import openai

def get_openai_key(env_path):
    """Parses a .env file to get the OPENAI_API_KEY."""
    try:
        with open(env_path, 'r') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#'):
                    key, value = line.split('=', 1)
                    if key == 'OPENAI_API_KEY':
                        return value.strip()
    except FileNotFoundError:
        print(f"Erreur : Le fichier .env n'a pas été trouvé à l'emplacement : {env_path}")
        return None
    except Exception as e:
        print(f"Une erreur est survenue lors de la lecture du fichier .env : {e}")
        return None
    return None

def test_openai_api(api_key):
    """Tests the OpenAI API with the provided key."""
    if not api_key:
        print("La clé API OpenAI n'a pas été trouvée.")
        return

    try:
        client = openai.OpenAI(api_key=api_key)
        client.models.list()
        print("Accès à l'API OpenAI réussi !")
        return True
    except Exception as e:
        print(f"Échec de la connexion à l'API OpenAI : {e}")
        return False

if __name__ == "__main__":
    env_file_path = '/home/luciedefraiteur/.env'
    openai_api_key = get_openai_key(env_file_path)
    test_openai_api(openai_api_key)
