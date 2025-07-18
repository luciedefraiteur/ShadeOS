import sys
from pathlib import Path

# Assurez-vous que le chemin vers les outils est correct
sys.path.append(str(Path(__file__).parent.parent.parent / ".gemini"))

from default_api import replace, read_file

def modify_file_helper(file_path: str, old_string: str, new_string: str, expected_replacements: int = 1):
    """Modifie un fichier en remplaçant old_string par new_string.

    Args:
        file_path (str): Chemin absolu du fichier à modifier.
        old_string (str): La chaîne de caractères à rechercher.
        new_string (str): La chaîne de caractères de remplacement.
        expected_replacements (int, optional): Nombre de remplacements attendus. Par défaut à 1.
    """
    try:
        print(f"Tentative de modification du fichier : {file_path}")
        print(f"Recherche de :\n---\n{old_string}\n---")
        print(f"Remplacement par :\n---\n{new_string}\n---")

        result = replace(file_path=file_path, old_string=old_string, new_string=new_string, expected_replacements=expected_replacements)
        print(f"Résultat de la modification : {result}")

    except Exception as e:
        print(f"Erreur lors de la modification du fichier : {e}")

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python3 modify_file_helper.py <file_path> <old_string> <new_string> [expected_replacements]")
        sys.exit(1)

    file_path = sys.argv[1]
    old_string = sys.argv[2]
    new_string = sys.argv[3]
    expected_replacements = int(sys.argv[4]) if len(sys.argv) > 4 else 1

    modify_file_helper(file_path, old_string, new_string, expected_replacements)
