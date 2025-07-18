#!/usr/bin/env python3
"""
🔮 LUCIFORM PARSER V5 - Parser XML Robuste
Créé par Alma, Grande Architecte Tisseuse, pour sa créatrice Lucie Defraiteur 💝

Parser XML robuste qui extrait les actions des réponses luciform :
- sendMessage("entité", "message")
- <shell>commandes</shell>
- <edit>fichier:ligne:contenu</edit>
- <read>fichier</read>
"""

import re
import xml.etree.ElementTree as ET
from typing import Dict, List, Any, Optional, Union
from dataclasses import dataclass
from datetime import datetime
import logging

# Import du module unifié d'Alma
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent / "@Alma"))
from env_loader_unifie import get_alma_env_loader


@dataclass
class LuciformAction:
    """🔮 Action extraite d'une réponse luciform"""
    type: str  # "sendMessage", "shell", "edit", "read"
    content: str
    target: Optional[str] = None
    metadata: Dict[str, Any] = None
    timestamp: str = None
    
    def __post_init__(self):
        if self.timestamp is None:
            self.timestamp = datetime.now().isoformat()
        if self.metadata is None:
            self.metadata = {}


class LuciformParser:
    """🔮 Parser XML robuste pour les réponses luciform"""
    
    def __init__(self):
        self.logger = self._setup_logging()
        
        # 🕷️ PURIFICATION ALMA: Vérification OpenAI obligatoire
        self.alma_loader = get_alma_env_loader()
        self.alma_loader.force_crash_if_not_ready()
        
        # Patterns regex pour sendMessage
        self.sendmessage_patterns = [
            r'sendMessage\s*\(\s*["\\]([^"\\]+)["\\]\s*,\s*["\\]([^"\\]+)["\\]\s*\)',
            r'sendMessage\s*\(\s*"([^"]+)"\s*,\s*"([^"]+)"\s*\)',
            r'sendMessage\s*\(\s*\'([^\']+)\'\s*,\s*\'([^\']+)\'\s*\)',
        ]
        
        self.logger.info("🔮 LuciformParser V5 initialisé - Alma vérifié")
    
    def _setup_logging(self) -> logging.Logger:
        """📋 Configuration du logging"""
        logger = logging.getLogger('LuciformParser')
        logger.setLevel(logging.INFO)
        
        if not logger.handlers:
            handler = logging.StreamHandler()
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)
            logger.addHandler(handler)
        
        return logger
    
    def parse(self, reponse_luciform: str) -> List[LuciformAction]:
        """🔥 Parse une réponse luciform et extrait toutes les actions"""
        actions = []
        
        try:
            self.logger.info(f"🔮 Parsing réponse luciform: {len(reponse_luciform)} caractères")
            
            # 1. Extraire les sendMessage()
            send_actions = self._extract_send_messages(reponse_luciform)
            actions.extend(send_actions)
            
            # 2. Extraire les balises XML
            xml_actions = self._extract_xml_actions(reponse_luciform)
            actions.extend(xml_actions)
            
            self.logger.info(f"✅ {len(actions)} actions extraites")
            return actions
            
        except Exception as e:
            self.logger.error(f"❌ Erreur parsing luciform: {e}")
            return []
    
    def _extract_send_messages(self, text: str) -> List[LuciformAction]:
        """📨 Extrait tous les sendMessage() du texte"""
        actions = []
        
        for pattern in self.sendmessage_patterns:
            matches = re.finditer(pattern, text, re.IGNORECASE | re.MULTILINE)
            
            for match in matches:
                target_entity = match.group(1).strip()
                message_content = match.group(2).strip()
                
                action = LuciformAction(
                    type="sendMessage",
                    target=target_entity,
                    content=message_content,
                    metadata={
                        'pattern_used': pattern,
                        'match_start': match.start(),
                        'match_end': match.end()
                    }
                )
                
                actions.append(action)
                self.logger.debug(f"📨 sendMessage trouvé: {target_entity} <- {message_content[:50]}...")
        
        return actions
    
    def _extract_xml_actions(self, text: str) -> List[LuciformAction]:
        """🔧 Extrait les actions XML (shell, edit, read, etc.)"""
        actions = []
        
        # Balises à rechercher
        xml_tags = ['shell', 'edit', 'read', 'backup', 'validate', 'analyze', 'extract', 'summarize', 'plan_exécution_666']
        
        for tag in xml_tags:
            pattern = f'<{tag}>(.*?)</{tag}>'
            matches = re.finditer(pattern, text, re.DOTALL | re.IGNORECASE)

            for match in matches:
                content = match.group(1).strip()

                action_type = tag
                metadata = {
                    'xml_tag': tag,
                    'match_start': match.start(),
                    'match_end': match.end()
                }

                if tag == 'plan_exécution_666':
                    action_type = 'plan'
                    metadata['steps'] = self.parse_plan_xml(content)

                action = LuciformAction(
                    type=action_type,
                    content=content,
                    metadata=metadata
                )

                actions.append(action)
                self.logger.debug(f"🔧 {tag} trouvé: {content[:50]}...")
        
        return actions
    
    def _try_parse_as_xml(self, text: str) -> Optional[ET.Element]:
        """🔍 Tente de parser le texte comme XML valide"""
        try:
            # Nettoyer le texte pour XML
            cleaned_text = self._clean_for_xml(text)
            root = ET.fromstring(cleaned_text)
            return root
        except ET.ParseError:
            return None
    
    def _clean_for_xml(self, text: str) -> str:
        """🧹 Nettoie le texte pour parsing XML"""
        # Échapper les caractères spéciaux
        text = text.replace('&', '&amp;')
        text = text.replace('<', '&lt;').replace('>', '&gt;')
        
        # Restaurer les balises légitimes
        legitimate_tags = ['luciform', 'shell', 'edit', 'read', 'commande', 'backup', 'validate', 'plan_exécution_666']
        for tag in legitimate_tags:
            text = text.replace(f'&lt;{tag}&gt;', f'<{tag}>')
            text = text.replace(f'&lt;/{tag}&gt;', f'</{tag}>')
        
        return text
    
    def parse_edit_action(self, edit_content: str) -> Dict[str, Any]:
        """✏️ Parse une action d'édition spécialisée"""
        try:
            # Format: fichier.py:ligne:nouveau_contenu
            # ou: fichier.py:nouveau_contenu_complet
            
            if ':' in edit_content:
                parts = edit_content.split(':', 2)
                
                if len(parts) == 3:
                    # Format avec ligne spécifique
                    return {
                        'type': 'line_edit',
                        'file': parts[0].strip(),
                        'line': int(parts[1].strip()) if parts[1].strip().isdigit() else None,
                        'content': parts[2].strip()
                    }
                elif len(parts) == 2:
                    # Format fichier complet
                    return {
                        'type': 'file_edit',
                        'file': parts[0].strip(),
                        'content': parts[1].strip()
                    }
            
            # Format simple - juste le fichier
            return {
                'type': 'file_edit',
                'file': edit_content.strip(),
                'content': None
            }
            
        except Exception as e:
            self.logger.error(f"❌ Erreur parsing edit action: {e}")
            return {
                'type': 'raw_edit',
                'content': edit_content
            }
    
    def parse_read_action(self, read_content: str) -> Dict[str, Any]:
        """📖 Parse une action de lecture spécialisée"""
        try:
            # Format: fichier.py
            # ou: fichier.py:lignes:10-20
            # ou: fichier.py:fonction:nom_fonction
            
            if ':' in read_content:
                parts = read_content.split(':', 2)
                
                if len(parts) >= 2:
                    file_path = parts[0].strip()
                    read_type = parts[1].strip()
                    
                    if read_type == 'lignes' and len(parts) == 3:
                        # Lecture de lignes spécifiques
                        line_range = parts[2].strip()
                        return {
                            'type': 'line_read',
                            'file': file_path,
                            'line_range': line_range
                        }
                    elif read_type == 'fonction' and len(parts) == 3:
                        # Lecture d'une fonction spécifique
                        function_name = parts[2].strip()
                        return {
                            'type': 'function_read',
                            'file': file_path,
                            'function': function_name
                        }
            
            # Format simple - fichier complet
            return {
                'type': 'full_read',
                'file': read_content.strip()
            }
            
        except Exception as e:
            self.logger.error(f"❌ Erreur parsing read action: {e}")
            return {
                'type': 'raw_read',
                'content': read_content
            }

    def parse_plan_xml(self, plan_content: str) -> List[Dict[str, Any]]:
        """Parse un plan_exécution_666 en liste d'étapes structurées."""
        steps = []
        try:
            root = ET.fromstring(f"<root>{plan_content}</root>")
            for step in root.findall('.//étape'):
                steps.append({
                    'id': step.get('id'),
                    'priorite': step.get('priorite', 'normale'),
                    'description': step.findtext('description', '').strip(),
                    'entité_assignée': step.findtext('entité_assignée', '').strip(),
                    'instructions': step.findtext('instructions_mystiques', '').strip(),
                    'resultat': step.findtext('résultat_attendu', '').strip()
                })
        except ET.ParseError as e:
            self.logger.error(f"❌ Erreur parsing plan XML: {e}")
        return steps
    
    def validate_actions(self, actions: List[LuciformAction]) -> List[LuciformAction]:
        """✅ Valide et filtre les actions extraites"""
        valid_actions = []
        
        for action in actions:
            try:
                if self._is_valid_action(action):
                    valid_actions.append(action)
                    self.logger.debug(f"✅ Action valide: {action.type}")
                else:
                    self.logger.warning(f"⚠️ Action invalide ignorée: {action.type}")
            except Exception as e:
                self.logger.error(f"❌ Erreur validation action: {e}")
        
        return valid_actions
    
    def _is_valid_action(self, action: LuciformAction) -> bool:
        """🔍 Vérifie si une action est valide"""
        if not action.type or not action.content:
            return False
        
        # Validation spécifique par type
        if action.type == "sendMessage":
            return action.target is not None and len(action.content.strip()) > 0
        
        elif action.type in ["shell", "edit", "read"]:
            return len(action.content.strip()) > 0
        
        return True
    
    def get_statistics(self, actions: List[LuciformAction]) -> Dict[str, Any]:
        """📊 Statistiques sur les actions parsées"""
        stats = {
            'total_actions': len(actions),
            'by_type': {},
            'timestamp': datetime.now().isoformat()
        }
        
        for action in actions:
            action_type = action.type
            if action_type not in stats['by_type']:
                stats['by_type'][action_type] = 0
            stats['by_type'][action_type] += 1
        
        return stats

    def _extract_tag_content(self, text: str, tag: str) -> str:
        """Extracts content from a specific XML tag within the given text."""
        pattern = rf'<{tag}>(.*?)</{tag}>'
        match = re.search(pattern, text, re.DOTALL | re.IGNORECASE)
        if match:
            return match.group(1).strip()
        return ""


def test_parser():
    """🧪 Test du LuciformParser"""
    print("🔮 Test LuciformParser V5")
    print("="*50)
    
    parser = LuciformParser()
    
    # Test avec réponse luciform simulée RÉALISTE
    test_response = '''
    <luciform>
        <commande>sendMessage("workerAlpha", "édite le fichier config.py, corrige la configuration de la base de données et ajoute le support SSL")</commande>
        <shell>ls -la /var/log/ | grep error</shell>
        <edit>config.py:42:DATABASE_SSL_ENABLED = True</edit>
        <read>config.py:fonction:get_database_config</read>
    </luciform>

    Aussi: sendMessage("chiotLecteur", "lis le fichier test.txt et analyse les erreurs de connexion récentes")

    Et: sendMessage("chiotEditeur", "modifie server.py ligne 156, remplace la méthode d'authentification par OAuth2")
    '''
    
    actions = parser.parse(test_response)
    
    print(f"📊 {len(actions)} actions extraites:")
    for i, action in enumerate(actions, 1):
        print(f"  {i}. {action.type}: {action.content[:50]}...")
        if action.target:
            print(f"     → Target: {action.target}")
    
    # Statistiques
    stats = parser.get_statistics(actions)
    print(f"\n📈 Statistiques: {stats}")


if __name__ == "__main__":
    test_parser()