#!/usr/bin/env python3
"""
🎮 ORCHESTRATEUR CHEATCODE V4 - Coordonne tous les pouvoirs de ShadEOS
"""

from pathlib import Path
from string import Template
from typing import Dict, List, Any, Optional
import json

from .cheat_engine import CheatEngine
from .cheat_parser import CheatParser

class CheatOrchestrator:
    """Orchestrateur principal du mode cheatcode"""
    
    def __init__(self, prompts_dir: str = "prompts"):
        self.prompts_dir = Path(prompts_dir)
        self.engine = CheatEngine()
        self.parser = CheatParser()
        
        # Charger le prompt cheatcode
        self.prompt_template = self._charger_prompt_cheatcode()
        
        print("🎮 CheatOrchestrator V4 initialisé")
    
    def _charger_prompt_cheatcode(self) -> Optional[Template]:
        """Charge le prompt cheatcode"""
        prompt_file = self.prompts_dir / "shadeos_cheatcode.prompt"
        
        if not prompt_file.exists():
            print(f"❌ Prompt cheatcode non trouvé: {prompt_file}")
            return None
        
        try:
            with open(prompt_file, 'r', encoding='utf-8') as f:
                contenu = f.read()
            
            return Template(contenu)
        except Exception as e:
            print(f"❌ Erreur chargement prompt: {e}")
            return None
    
    def generer_prompt_shadeos(self) -> str:
        """Génère le prompt pour ShadEOS avec l'historique actuel"""
        if not self.prompt_template:
            return "Erreur: Prompt cheatcode non disponible"

        # Variables pour le template
        variables = {
            'mon_historique_buffer': self.engine.get_historique_formate()
        }

        try:
            prompt_formate = self.prompt_template.safe_substitute(**variables)

            # LOGGER LE PROMPT GÉNÉRÉ
            self.engine._log("="*80)
            self.engine._log("📝 PROMPT GÉNÉRÉ POUR SHADEOS")
            self.engine._log("="*80)
            self.engine._log(f"📏 Longueur: {len(prompt_formate)} caractères")
            self.engine._log("📋 CONTENU COMPLET:")
            self.engine._log(prompt_formate)
            self.engine._log("="*80)

            return prompt_formate
        except Exception as e:
            error_msg = f"Erreur formatage: {e}"
            self.engine._log(f"❌ ERREUR GÉNÉRATION PROMPT: {error_msg}")
            print(f"❌ Erreur formatage prompt: {e}")
            return error_msg
    
    def executer_reponse_shadeos(self, reponse_xml: str) -> Dict[str, Any]:
        """Exécute une réponse cheatcode de ShadEOS"""
        print("🎮 Exécution réponse ShadEOS CheatCode")

        # LOGGER LA RÉPONSE REÇUE
        self.engine._log("="*80)
        self.engine._log("📥 RÉPONSE XML REÇUE DE SHADEOS")
        self.engine._log("="*80)
        self.engine._log(f"📏 Longueur: {len(reponse_xml)} caractères")
        self.engine._log("📋 CONTENU XML COMPLET:")
        self.engine._log(reponse_xml)
        self.engine._log("="*80)

        # Parser la réponse
        self.engine._log("🔮 DÉBUT PARSING XML...")
        parsed = self.parser.parse_reponse_cheatcode(reponse_xml)

        if 'error' in parsed:
            error_msg = f"Erreur parsing: {parsed['error']}"
            self.engine._log(f"❌ ERREUR PARSING: {error_msg}")
            return {
                'success': False,
                'error': error_msg
            }

        # LOGGER LES RÉSULTATS DU PARSING
        self.engine._log("✅ PARSING RÉUSSI")
        self.engine._log(f"📊 Actions détectées: {len(parsed['actions'])}")
        self.engine._log(f"🧠 Analyse: {parsed['analyse_situation']}")
        self.engine._log(f"📋 Plan: {parsed['plan_global']}")
        for i, action in enumerate(parsed['actions']):
            self.engine._log(f"   Action {i+1}: {action['type']} - {action.get('objectif', 'Pas d objectif')}")
        
        # Valider les actions
        validation = self.parser.valider_actions(parsed['actions'])
        
        if not validation['valid']:
            return {
                'success': False,
                'error': f"Actions invalides: {validation['errors']}"
            }
        
        # Afficher l'analyse et le plan
        if parsed['analyse_situation']:
            print(f"🧠 Analyse: {parsed['analyse_situation']}")
        
        if parsed['plan_global']:
            print(f"📋 Plan: {parsed['plan_global']}")
        
        # Exécuter toutes les actions
        resultats_actions = []
        
        for i, action in enumerate(parsed['actions']):
            print(f"\n🎯 Action {i+1}/{len(parsed['actions'])}: {action['type']}")
            
            if action.get('objectif'):
                print(f"   Objectif: {action['objectif']}")
            
            resultat = self._executer_action(action)
            resultats_actions.append(resultat)
            
            # Afficher le résultat
            if resultat['success']:
                print(f"   ✅ Succès")
            else:
                print(f"   ❌ Échec: {resultat.get('error', 'Erreur inconnue')}")
        
        # Résumé final
        succes = sum(1 for r in resultats_actions if r['success'])
        total = len(resultats_actions)
        
        return {
            'success': succes == total,
            'analyse_situation': parsed['analyse_situation'],
            'plan_global': parsed['plan_global'],
            'actions_executees': total,
            'actions_reussies': succes,
            'resultats_actions': resultats_actions,
            'validation': validation
        }
    
    def _executer_action(self, action: Dict[str, Any]) -> Dict[str, Any]:
        """Exécute une action spécifique"""
        action_type = action['type']
        
        try:
            if action_type == 'shell':
                return self.engine.executer_shell(action['commande'])
            
            elif action_type == 'gemini':
                # Démarrer Gemini si pas encore fait
                if not self.engine.gemini_terminal_id:
                    start_result = self.engine.demarrer_gemini_cli()
                    if not start_result['success']:
                        return start_result
                
                return self.engine.envoyer_message_gemini(action['message'])
            
            elif action_type == 'write_python':
                return self.engine.ecrire_python(action['fichier'], action['contenu'])
            
            elif action_type == 'read_file':
                return self.engine.lire_fichier(action['fichier'], action.get('mode', 'entier'))
            
            elif action_type == 'write_file':
                return self.engine.ecrire_fichier(
                    action['fichier'], 
                    action['contenu'], 
                    action.get('mode', 'entier')
                )
            
            else:
                return {
                    'success': False,
                    'error': f"Type d'action inconnu: {action_type}"
                }
                
        except Exception as e:
            return {
                'success': False,
                'error': f"Erreur exécution {action_type}: {str(e)}"
            }
    
    def get_statistiques(self) -> Dict[str, Any]:
        """Récupère les statistiques du cheatcode"""
        return {
            'historique_taille': len(self.engine.historique_buffer),
            'historique_max': self.engine.buffer_size,
            'gemini_actif': self.engine.gemini_terminal_id is not None,
            'prompt_disponible': self.prompt_template is not None
        }
    
    def sauvegarder_session(self, fichier: str = "cheatcode_session.json"):
        """Sauvegarde la session cheatcode"""
        session_data = {
            'historique': list(self.engine.historique_buffer),
            'gemini_terminal_id': self.engine.gemini_terminal_id,
            'statistiques': self.get_statistiques()
        }
        
        try:
            with open(fichier, 'w', encoding='utf-8') as f:
                json.dump(session_data, f, indent=2, ensure_ascii=False)
            
            print(f"💾 Session sauvegardée: {fichier}")
            return True
        except Exception as e:
            print(f"❌ Erreur sauvegarde: {e}")
            return False
    
    def charger_session(self, fichier: str = "cheatcode_session.json") -> bool:
        """Charge une session cheatcode"""
        try:
            with open(fichier, 'r', encoding='utf-8') as f:
                session_data = json.load(f)
            
            # Restaurer l'historique
            self.engine.historique_buffer.clear()
            for entry in session_data.get('historique', []):
                self.engine.historique_buffer.append(entry)
            
            # Restaurer l'état Gemini
            self.engine.gemini_terminal_id = session_data.get('gemini_terminal_id')
            
            print(f"📂 Session chargée: {fichier}")
            return True
        except Exception as e:
            print(f"❌ Erreur chargement: {e}")
            return False
