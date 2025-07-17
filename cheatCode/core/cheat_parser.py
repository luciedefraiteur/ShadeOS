#!/usr/bin/env python3
"""
🔮 PARSEUR CHEATCODE V4 - Parse les actions ShadEOS CheatCode
"""

import xml.etree.ElementTree as ET
import re
from typing import Dict, List, Any, Optional

class CheatParser:
    """Parser pour les réponses cheatcode de ShadEOS"""
    
    def __init__(self):
        print("🔮 CheatParser V4 initialisé")
    
    def parse_reponse_cheatcode(self, reponse_xml: str) -> Dict[str, Any]:
        """Parse une réponse cheatcode et extrait toutes les actions"""
        try:
            # Nettoyer le XML
            xml_clean = self._nettoyer_xml(reponse_xml)
            root = ET.fromstring(xml_clean)
            
            resultats = {
                'analyse_situation': '',
                'plan_global': '',
                'actions': [],
                'metadata': {}
            }
            
            # Extraire l'analyse de situation
            analyse_elem = root.find('.//analyse_situation')
            if analyse_elem is not None:
                resultats['analyse_situation'] = analyse_elem.text or ""
            
            # Extraire le plan global
            plan_elem = root.find('.//plan_global')
            if plan_elem is not None:
                resultats['plan_global'] = plan_elem.text or ""
            
            # Extraire toutes les actions
            resultats['actions'] = self._extraire_actions(root)
            
            # Métadonnées
            resultats['metadata'] = self._extraire_metadata(root)
            
            return resultats
            
        except Exception as e:
            print(f"❌ Erreur parsing cheatcode: {e}")
            return {'error': str(e)}
    
    def _nettoyer_xml(self, xml_str: str) -> str:
        """Nettoie le XML pour le parsing"""
        # Enlever les commentaires XML
        xml_str = re.sub(r'<!--.*?-->', '', xml_str, flags=re.DOTALL)
        
        # S'assurer qu'on a une racine luciform
        if not xml_str.strip().startswith('<luciform'):
            # Chercher le bloc luciform
            match = re.search(r'<luciform.*?</luciform>', xml_str, re.DOTALL)
            if match:
                xml_str = match.group(0)
            else:
                raise ValueError("Pas de bloc luciform trouvé")
        
        return xml_str
    
    def _extraire_actions(self, root: ET.Element) -> List[Dict[str, Any]]:
        """Extrait toutes les actions du XML"""
        actions = []
        
        # Action Gemini
        action_gemini = root.find('.//action_gemini')
        if action_gemini is not None:
            message_elem = action_gemini.find('message_pour_gemini')
            objectif_elem = action_gemini.find('objectif')
            
            actions.append({
                'type': 'gemini',
                'message': message_elem.text if message_elem is not None else "",
                'objectif': objectif_elem.text if objectif_elem is not None else ""
            })
        
        # Action Shell
        action_shell = root.find('.//action_shell')
        if action_shell is not None:
            commande_elem = action_shell.find('commande')
            objectif_elem = action_shell.find('objectif')
            
            actions.append({
                'type': 'shell',
                'commande': commande_elem.text if commande_elem is not None else "",
                'objectif': objectif_elem.text if objectif_elem is not None else ""
            })
        
        # Action Write Python
        action_python = root.find('.//action_write_python')
        if action_python is not None:
            fichier_elem = action_python.find('fichier')
            contenu_elem = action_python.find('contenu')
            objectif_elem = action_python.find('objectif')
            
            actions.append({
                'type': 'write_python',
                'fichier': fichier_elem.text if fichier_elem is not None else "",
                'contenu': contenu_elem.text if contenu_elem is not None else "",
                'objectif': objectif_elem.text if objectif_elem is not None else ""
            })
        
        # Action Read File
        action_read = root.find('.//action_read_file')
        if action_read is not None:
            fichier_elem = action_read.find('fichier')
            mode_elem = action_read.find('mode')
            objectif_elem = action_read.find('objectif')
            
            actions.append({
                'type': 'read_file',
                'fichier': fichier_elem.text if fichier_elem is not None else "",
                'mode': mode_elem.text if mode_elem is not None else "entier",
                'objectif': objectif_elem.text if objectif_elem is not None else ""
            })
        
        # Action Write File
        action_write = root.find('.//action_write_file')
        if action_write is not None:
            fichier_elem = action_write.find('fichier')
            mode_elem = action_write.find('mode')
            contenu_elem = action_write.find('contenu')
            objectif_elem = action_write.find('objectif')
            
            actions.append({
                'type': 'write_file',
                'fichier': fichier_elem.text if fichier_elem is not None else "",
                'mode': mode_elem.text if mode_elem is not None else "entier",
                'contenu': contenu_elem.text if contenu_elem is not None else "",
                'objectif': objectif_elem.text if objectif_elem is not None else ""
            })
        
        return actions
    
    def _extraire_metadata(self, root: ET.Element) -> Dict[str, Any]:
        """Extrait les métadonnées du luciform"""
        metadata = {}
        
        # Attributs de la racine
        metadata['id'] = root.get('id', '')
        metadata['type'] = root.get('type', '')
        metadata['niveau'] = root.get('niveau', '')
        
        # Éléments de base
        metadata['entite'] = self._get_text_safe(root.find('entité'))
        metadata['role'] = self._get_text_safe(root.find('rôle'))
        metadata['but'] = self._get_text_safe(root.find('but'))
        metadata['style'] = self._get_text_safe(root.find('style'))
        
        return metadata
    
    def _get_text_safe(self, element: Optional[ET.Element]) -> str:
        """Récupère le texte d'un élément de manière sécurisée"""
        return element.text or "" if element is not None else ""
    
    def valider_actions(self, actions: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Valide les actions extraites"""
        validation = {
            'valid': True,
            'errors': [],
            'warnings': [],
            'stats': {
                'total_actions': len(actions),
                'types': {}
            }
        }
        
        for i, action in enumerate(actions):
            action_type = action.get('type', 'unknown')
            
            # Compter les types
            validation['stats']['types'][action_type] = validation['stats']['types'].get(action_type, 0) + 1
            
            # Validation spécifique par type
            if action_type == 'shell':
                if not action.get('commande'):
                    validation['errors'].append(f"Action {i+1}: commande shell vide")
                    validation['valid'] = False
            
            elif action_type == 'write_python':
                if not action.get('fichier'):
                    validation['errors'].append(f"Action {i+1}: fichier Python non spécifié")
                    validation['valid'] = False
                if not action.get('contenu'):
                    validation['errors'].append(f"Action {i+1}: contenu Python vide")
                    validation['valid'] = False
            
            elif action_type == 'read_file':
                if not action.get('fichier'):
                    validation['errors'].append(f"Action {i+1}: fichier à lire non spécifié")
                    validation['valid'] = False
            
            elif action_type == 'write_file':
                if not action.get('fichier'):
                    validation['errors'].append(f"Action {i+1}: fichier à écrire non spécifié")
                    validation['valid'] = False
            
            elif action_type == 'gemini':
                if not action.get('message'):
                    validation['errors'].append(f"Action {i+1}: message pour Gemini vide")
                    validation['valid'] = False
            
            # Vérifications générales
            if not action.get('objectif'):
                validation['warnings'].append(f"Action {i+1}: objectif non spécifié")
        
        return validation
