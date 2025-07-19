

import json
import os
from datetime import datetime, date, timedelta

def get_week_number(d):
    """
    Calcule le numéro de la semaine pour une date donnée, en considérant le lundi comme le premier jour de la semaine.
    """
    return d.isocalendar()[1]

def extract_conversation_content(conversation_data):
    """
    Extrait le contenu textuel d'une conversation.
    """
    content = []
    if "mapping" in conversation_data:
        for node_id, node in conversation_data["mapping"].items():
            if node and "message" in node and node["message"] and "content" in node["message"] and "parts" in node["message"]["content"]:
                for part in node["message"]["content"]["parts"]:
                    if isinstance(part, str):
                        content.append(part)
                    elif isinstance(part, dict) and "text" in part:
                        content.append(part["text"])
    return "\n\n".join(content)

def organize_conversations(json_file_path, output_base_dir):
    """
    Organise les conversations d'un fichier JSON en une arborescence année/mois/semaine/jour.
    """
    with open(json_file_path, 'r', encoding='utf-8') as f:
        conversations = json.load(f)

    for conv in conversations:
        if "create_time" in conv and conv["create_time"]:
            try:
                # Convertir le timestamp en datetime
                create_time = datetime.fromtimestamp(conv["create_time"])
                year = create_time.year
                month = create_time.month
                week = get_week_number(create_time.date())
                day = create_time.day

                # Construire le chemin de sortie
                output_dir = os.path.join(
                    output_base_dir,
                    str(year),
                    f"{month:02d}",
                    f"week_{week:02d}",
                    f"{day:02d}"
                )
                os.makedirs(output_dir, exist_ok=True)

                # Extraire le contenu de la conversation
                conversation_content = extract_conversation_content(conv)
                
                # Utiliser le titre et un ID unique pour le nom du fichier Markdown
                title = conv.get("title", "untitled_conversation").replace("/", "_").replace("\\", "_")
                conv_id = conv.get("id", datetime.now().strftime("%Y%m%d%H%M%S%f")) # Fallback to timestamp if no ID
                md_file_name = f"{title}_{conv_id}.md"
                md_file_path = os.path.join(output_dir, md_file_name)

                with open(md_file_path, 'w', encoding='utf-8') as md_file:
                    md_file.write(f"# {title}\n\n")
                    md_file.write(f"**Date de création :** {create_time.strftime('%Y-%m-%d %H:%M:%S')}\n\n")
                    md_file.write("---\n\n")
                    md_file.write(conversation_content)
                print(f"Conversation '{title}' organisée dans : {md_file_path}")

            except Exception as e:
                print(f"Erreur lors du traitement d'une conversation : {e}")
        else:
            print(f"Conversation sans 'create_time' valide : {conv.get('title', 'Sans titre')}")

if __name__ == "__main__":
    json_input_path = "/home/luciedefraiteur/ShadEOS/conversations-ShadeOS/conversations.json"
    output_base_directory = "/home/luciedefraiteur/ShadEOS/bible-des-en-faire/disclosure-conversations-chronology/"
    organize_conversations(json_input_path, output_base_directory)

