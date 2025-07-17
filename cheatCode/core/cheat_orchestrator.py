#!/usr/bin/env python3
"""
 orchestrateur qui charge le prompt, l'envoie à une IA, reçoit la réponse, la parse, et utilise le CheatEngine pour exécuter les actions.
"""

import sys
from pathlib import Path
import xml.etree.ElementTree as ET
from typing import Dict, List, Any
import json # Ajout de l'importation du module json

# Ajout du chemin pour importer CheatEngine
sys.path.append(str(Path(__file__).parent))
from cheat_engine import CheatEngine

class CheatOrchestrator:
    """Orchestre le CheatCode en liant le prompt, l'IA et le moteur d'exécution."""

    def __init__(self, prompts_dir: str, log_file: str = "cheatcode_session.log"):
        self.prompts_dir = Path(prompts_dir)
        self.engine = CheatEngine(log_file=log_file)
        self.prompt_template = self._charger_prompt_template()
        print("[CHEAT] CheatOrchestrator initialisé")

    def _charger_prompt_template(self) -> str:
        """Charge le template de prompt depuis le fichier."""
        try:
            prompt_path = self.prompts_dir / "shadeos_cheatcode.prompt"
            with open(prompt_path, 'r', encoding='utf-8') as f:
                return f.read()
        except FileNotFoundError:
            print(f"[ERREUR] Prompt non trouvé à {prompt_path}")
            return ""

    def generer_prompt_shadeos(self) -> str:
        """Génère le prompt complet pour ShadEOS en injectant le contexte de session."""
        contexte_found_files = "\n".join(self.engine.session_context.get("found_files", []))
        contexte_read_contents = json.dumps(self.engine.session_context.get("read_contents", {}), indent=2, ensure_ascii=False)
        
        prompt = self.prompt_template.replace("$mon_contexte_session_found_files", contexte_found_files)
        prompt = prompt.replace("$mon_contexte_session_read_contents", contexte_read_contents)
        return prompt

    def executer_reponse_shadeos(self, reponse_xml: str, cycle: int) -> Dict[str, Any]:
        """Parse et exécute les actions d'une réponse luciform."""
        print("\n[CHEAT] Exécution de la réponse de ShadEOS...")
        try:
            root = ET.fromstring(reponse_xml)
            actions = self._parser_actions(root)
            
            actions_executees = 0
            actions_reussies = 0
            
            for action_type, params in actions:
                actions_executees += 1
                resultat = self._executer_action(action_type, params, cycle)
                if resultat.get('success', False):
                    actions_reussies += 1
            
            print(f"[FIN] Exécution terminée: {actions_reussies}/{actions_executees} actions réussies.")
            return {
                'success': actions_reussies == actions_executees,
                'actions_executees': actions_executees,
                'actions_reussies': actions_reussies
            }

        except ET.ParseError as e:
            print(f"[ERREUR] Erreur de parsing XML: {e}")
            return {'success': False, 'error': f"XML malformé: {e}"}
        except Exception as e:
            print(f"[ERREUR] Erreur inattendue pendant l'exécution: {e}")
            return {'success': False, 'error': f"Erreur d'exécution: {e}"}

    def _parser_actions(self, root: ET.Element) -> List[tuple[str, Dict[str, str]]]:
        """Parse les éléments d'action depuis l'arbre XML."""
        actions = []
        action_map = {
            'action_gemini': 'GEMINI',
            'action_shell': 'SHELL',
            'action_write_python': 'WRITE_PYTHON',
            'action_read_file': 'READ_FILE',
            'action_write_file': 'WRITE_FILE'
        }

        for xml_tag, action_type in action_map.items():
            for action_node in root.findall(f'.//{xml_tag}'):
                params = {child.tag: child.text.strip() for child in action_node}
                actions.append((action_type, params))
        
        return actions

    def _executer_action(self, action_type: str, params: Dict[str, str], cycle: int) -> Dict[str, Any]:
        """Appelle la méthode correspondante du CheatEngine."""
        print(f"  -> Exécution de l'action: {action_type}")
        if action_type == 'GEMINI':
            return self.engine.envoyer_message_gemini(params.get('message_pour_gemini', ''), cycle)
        elif action_type == 'SHELL':
            return self.engine.executer_shell(params.get('commande', ''), cycle)
        elif action_type == 'WRITE_PYTHON':
            return self.engine.ecrire_python(params.get('fichier', ''), params.get('contenu', ''), cycle)
        elif action_type == 'READ_FILE':
            return self.engine.lire_fichier(params.get('fichier', ''), cycle, params.get('mode', 'entier'))
        elif action_type == 'WRITE_FILE':
            return self.engine.ecrire_fichier(params.get('fichier', ''), params.get('contenu', ''), cycle, params.get('mode', 'entier'))
        else:
            print(f"[ATTENTION] Action inconnue: {action_type}")
            return {'success': False, 'error': 'Action inconnue'}

    def get_statistiques(self) -> Dict[str, Any]:
        """Récupère des statistiques simples."""
        return {
            'historique_taille': len(self.engine.historique_buffer),
            'prompt_taille': len(self.prompt_template)
        }

if __name__ == '__main__':
    print("[TEST] Test de CheatOrchestrator")
    orchestrator = CheatOrchestrator("cheatCode/prompts")
    prompt = orchestrator.generer_prompt_shadeos()
    print(f"Prompt généré avec succès (longueur: {len(prompt)})")
    reponse_simulee = """
    <luciform>
      <action_shell>
        <commande>echo "Test Orchestrator OK"</commande>
        <objectif>Valider le fonctionnement</objectif>
      </action_shell>
    </luciform>
    """
    orchestrator.executer_reponse_shadeos(reponse_simulee, 0)