import sys
import json

def precise_modify_file_helper(file_path: str, start_index: int, end_index: int, new_content: str):
    """Imprime les informations nécessaires pour une modification précise de fichier.

    Args:
        file_path (str): Chemin absolu du fichier à modifier.
        start_index (int): Index du caractère de début (inclus).
        end_index (int): Index du caractère de fin (exclus).
        new_content (str): Le nouveau contenu à insérer.
    """
    try:
        output_data = {
            "file_path": file_path,
            "start_index": start_index,
            "end_index": end_index,
            "new_content": new_content
        }
        print(json.dumps(output_data))

    except Exception as e:
        print(json.dumps({"error": str(e)}))

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print(json.dumps({"error": "Usage: python3 precise_modify_file_helper.py <file_path> <start_index> <end_index> <new_content>"}))
        sys.exit(1)

    file_path = sys.argv[1]
    start_index = int(sys.argv[2])
    end_index = int(sys.argv[3])
    new_content = sys.argv[4]

    precise_modify_file_helper(file_path, start_index, end_index, new_content)
