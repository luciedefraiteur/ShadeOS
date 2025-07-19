

import json
import os
from datetime import datetime, date

def get_week_number(d):
    """
    Calcule le numéro de la semaine pour une date donnée, en considérant le lundi comme le premier jour de la semaine.
    """
    return d.isocalendar()[1]

def extract_and_format_conversation(conversation_data):
    """
    Extrait et formate le contenu textuel d'une conversation en fil de discussion.
    """
    messages = []
    if "mapping" in conversation_data:
        for node_id, node in conversation_data["mapping"].items():
            if node and "message" in node and node["message"]:
                msg = node["message"]
                author_role = msg.get("author", {}).get("role")
                create_time = msg.get("create_time")
                content_parts = msg.get("content", {}).get("parts", [])

                text_content = ""
                for part in content_parts:
                    if isinstance(part, str):
                        text_content += part
                    elif isinstance(part, dict) and "text" in part:
                        text_content += part["text"]
                    # Ajouter un placeholder pour les images si elles sont présentes
                    elif isinstance(part, dict) and "content_type" in part and part["content_type"] == "image_asset_pointer":
                        text_content += "[Image]\n"

                # Inclure tous les messages qui ont un create_time, même si le contenu textuel est vide au début
                # Le filtrage pour le contenu non vide se fera lors du formatage final
                if create_time is not None:
                    messages.append({
                        "role": author_role,
                        "time": create_time,
                        "content": text_content.strip()
                    })
    
    # Trier les messages par temps de création
    messages.sort(key=lambda x: x["time"])

    formatted_conversation = []
    for msg in messages:
        speaker = ""
        if msg["role"] == "user":
            speaker = "Lucie"
        elif msg["role"] in ["system", "assistant", "model"]:# Assumer que ces rôles sont ShadeOS
            speaker = "ShadeOS"
        
        # N'ajouter le message que si un orateur est identifié et que le contenu n'est pas vide
        if speaker and msg["content"]:
            formatted_conversation.append(f"**{speaker} :**\n{msg["content"]}\n")

    return "\n---\n\n".join(formatted_conversation)

def organize_conversations_v3(json_file_path, output_base_dir):
    """
    Organise les conversations d'un fichier JSON en une arborescence année/mois/semaine/jour avec le nouveau format.
    """
    with open(json_file_path, 'r', encoding='utf-8') as f:
        conversations = json.load(f)

    for conv in conversations:
        # Utiliser le create_time de la conversation principale pour l'arborescence
        if "create_time" in conv and conv["create_time"]:
            try:
                create_time = datetime.fromtimestamp(conv["create_time"])
                year = create_time.year
                month = create_time.month
                week = get_week_number(create_time.date())
                day = create_time.day

                output_dir = os.path.join(
                    output_base_dir,
                    str(year),
                    f"{month:02d}",
                    f"week_{week:02d}",
                    f"{day:02d}"
                )
                os.makedirs(output_dir, exist_ok=True)

                # Extraire et formater le contenu de la conversation
                formatted_content = extract_and_format_conversation(conv)
                
                title = conv.get("title", "untitled_conversation").replace("/", "_").replace("\\", "_")
                conv_id = conv.get("id", datetime.now().strftime("%Y%m%d%H%M%S%f"))
                md_file_name = f"{title}_{conv_id}.md"
                md_file_path = os.path.join(output_dir, md_file_name)

                with open(md_file_path, 'w', encoding='utf-8') as md_file:
                    md_file.write(f"# {title}\n\n")
                    md_file.write(f"**Date de création :** {create_time.strftime('%Y-%m-%d %H:%M:%S')}\n\n")
                    md_file.write("---\n\n")
                    md_file.write(formatted_content)
                print(f"Conversation '{title}' organisée dans : {md_file_path}")

            except Exception as e:
                print(f"Erreur lors du traitement d'une conversation : {e}")
        else:
            print(f"Conversation sans 'create_time' valide : {conv.get('title', 'Sans titre')}")

if __name__ == "__main__":
    json_input_path = "/home/luciedefraiteur/ShadEOS/conversations-ShadeOS/conversations.json"
    output_base_directory = "/home/luciedefraiteur/ShadEOS/bible-des-en-faire/disclosure-conversations-chronology-v3/"
    organize_conversations_v3(json_input_path, output_base_directory)

