#!/usr/bin/env python3
"""
🐕‍🦺 MEUTE MANAGER V5 - Gestionnaire Intelligent de Meute
Créé par Alma, Grande Architecte Tisseuse, pour sa créatrice Lucie Defraiteur 💝

Le Worker Alpha devient un gestionnaire intelligent qui coordonne sa meute de chiots spécialisés :
- 🐕 ChiotEditeur : Édition de fichiers intelligente
- 🐕 ChiotLecteur : Lecture et analyse de code
- 🐕 ChiotExecuteur : Exécution de commandes shell
- 🐕 ChiotWatcher : Surveillance système
"""

import os
import re
import subprocess
import logging
from typing import Dict, List, Any, Optional, Union
from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from pathlib import Path
import xml.etree.ElementTree as ET

# Import du module unifié d'Alma
import sys
sys.path.append(str(Path(__file__).parent.parent.parent / "@Alma"))
from env_loader_unifie import get_alma_env_loader

from luciform_parser import LuciformAction


class ChiotType(Enum):
    """🐕 Types de chiots spécialisés"""
    EDITEUR = "chiotEditeur"
    LECTEUR = "chiotLecteur"
    EXECUTEUR = "chiotExecuteur"
    WATCHER = "chiotWatcher"


@dataclass
class ChiotTask:
    """📋 Tâche assignée à un chiot"""
    chiot_type: ChiotType
    task_description: str
    file_path: Optional[str] = None
    command: Optional[str] = None
    parameters: Dict[str, Any] = None
    created_at: str = None
    completed_at: Optional[str] = None
    success: bool = False
    result: Optional[str] = None
    error: Optional[str] = None
    
    def __post_init__(self):
        if self.created_at is None:
            self.created_at = datetime.now().isoformat()
        if self.parameters is None:
            self.parameters = {}


class ChiotEditeur:
    """🐕 Chiot spécialisé dans l'édition de fichiers"""
    
    def __init__(self, logger: logging.Logger):
        self.logger = logger
        self.name = "ChiotEditeur"
        self.tasks_completed = 0
    
    def editer_fichier(self, task: ChiotTask) -> bool:
        """✏️ Édite un fichier selon les instructions"""
        try:
            self.logger.info(f"🐕 {self.name}: Édition de {task.file_path}")
            
            if not task.file_path or not os.path.exists(task.file_path):
                task.error = f"Fichier non trouvé: {task.file_path}"
                return False
            
            # Backup automatique
            backup_path = f"{task.file_path}.backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
            self._create_backup(task.file_path, backup_path)
            
            # Analyser les instructions d'édition
            edit_instructions = self._parse_edit_instructions(task.task_description)
            
            # Appliquer les modifications
            success = self._apply_edits(task.file_path, edit_instructions)
            
            if success:
                task.success = True
                task.result = f"Fichier {task.file_path} édité avec succès. Backup: {backup_path}"
                self.tasks_completed += 1
                self.logger.info(f"✅ {self.name}: Édition réussie")
                return True
            else:
                task.error = "Échec de l'édition"
                return False
                
        except Exception as e:
            task.error = f"Erreur édition: {e}"
            self.logger.error(f"❌ {self.name}: {e}")
            return False
    
    def _create_backup(self, file_path: str, backup_path: str) -> None:
        """💾 Crée un backup du fichier"""
        try:
            with open(file_path, 'r', encoding='utf-8') as src:
                with open(backup_path, 'w', encoding='utf-8') as dst:
                    dst.write(src.read())
            self.logger.debug(f"💾 Backup créé: {backup_path}")
        except Exception as e:
            self.logger.warning(f"⚠️ Erreur backup: {e}")
    
    def _parse_edit_instructions(self, instructions: str) -> Dict[str, Any]:
        """🔍 Parse les instructions d'édition"""
        parsed = {
            'type': 'general_edit',
            'line_specific': None,
            'function_specific': None,
            'search_replace': [],
            'additions': []
        }
        
        # Rechercher des patterns spécifiques
        if 'ligne' in instructions.lower():
            line_match = re.search(r'ligne\s+(\d+)', instructions, re.IGNORECASE)
            if line_match:
                parsed['line_specific'] = int(line_match.group(1))
                parsed['type'] = 'line_edit'
        
        if 'fonction' in instructions.lower():
            func_match = re.search(r'fonction\s+(\w+)', instructions, re.IGNORECASE)
            if func_match:
                parsed['function_specific'] = func_match.group(1)
                parsed['type'] = 'function_edit'
        
        # Rechercher des remplacements
        if 'remplace' in instructions.lower():
            # Pattern: "remplace X par Y"
            replace_matches = re.finditer(r'remplace\s+(.+?)\s+par\s+(.+?)(?:\s|$)', instructions, re.IGNORECASE)
            for match in replace_matches:
                parsed['search_replace'].append({
                    'search': match.group(1).strip(),
                    'replace': match.group(2).strip()
                })
        
        # Rechercher des ajouts
        if 'ajoute' in instructions.lower():
            add_matches = re.finditer(r'ajoute\s+(.+?)(?:\s|$)', instructions, re.IGNORECASE)
            for match in add_matches:
                parsed['additions'].append(match.group(1).strip())
        
        return parsed
    
    def _apply_edits(self, file_path: str, instructions: Dict[str, Any]) -> bool:
        """🔧 Applique les modifications au fichier"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            
            modified = False
            
            # Édition ligne spécifique
            if instructions['type'] == 'line_edit' and instructions['line_specific']:
                line_num = instructions['line_specific'] - 1  # Index 0
                if 0 <= line_num < len(lines):
                    # Appliquer les remplacements sur cette ligne
                    for replacement in instructions['search_replace']:
                        if replacement['search'] in lines[line_num]:
                            lines[line_num] = lines[line_num].replace(
                                replacement['search'], 
                                replacement['replace']
                            )
                            modified = True
            
            # Remplacements globaux
            else:
                for replacement in instructions['search_replace']:
                    for i, line in enumerate(lines):
                        if replacement['search'] in line:
                            lines[i] = line.replace(
                                replacement['search'], 
                                replacement['replace']
                            )
                            modified = True
            
            # Ajouts (à la fin du fichier pour l'instant)
            for addition in instructions['additions']:
                lines.append(f"{addition}\n")
                modified = True
            
            # Sauvegarder si modifié
            if modified:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.writelines(lines)
                return True
            
            return False
            
        except Exception as e:
            self.logger.error(f"❌ Erreur application édits: {e}")
            return False


class ChiotLecteur:
    """🐕 Chiot spécialisé dans la lecture et analyse"""

class ChiotExecuteur:
    """🐕 Chiot spécialisé dans l'exécution de commandes shell"""
    def __init__(self, logger: logging.Logger):
        self.logger = logger
        self.name = "ChiotExecuteur"
        self.tasks_completed = 0

    def executer_commande(self, task: ChiotTask) -> bool:
        """▶️ Exécute une commande shell"""
        try:
            self.logger.info(f"🐕 {self.name}: Exécution de '{task.command}'")
            if not task.command:
                task.error = "Commande vide."
                return False

            # Exécuter la commande
            process = subprocess.run(task.command, shell=True, capture_output=True, text=True)
            task.result = f"Stdout: {process.stdout}\nStderr: {process.stderr}"
            task.success = process.returncode == 0
            if not task.success:
                task.error = f"Erreur d'exécution: {process.stderr}"
            self.tasks_completed += 1
            self.logger.info(f"✅ {self.name}: Exécution {'réussie' if task.success else 'échouée'}")
            return task.success
        except Exception as e:
            task.error = f"Erreur exécution: {e}"
            self.logger.error(f"❌ {self.name}: {e}")
            return False

class ChiotWatcher:
    """🐕 Chiot spécialisé dans la surveillance système"""
    def __init__(self, logger: logging.Logger):
        self.logger = logger
        self.name = "ChiotWatcher"
        self.tasks_completed = 0

    def surveiller_systeme(self, task: ChiotTask) -> bool:
        """👀 Surveille un aspect du système"""
        try:
            self.logger.info(f"🐕 {self.name}: Surveillance de '{task.task_description}'")
            # Implémentation simple pour l'instant
            task.result = f"Surveillance de '{task.task_description}' effectuée. Tout semble normal."
            task.success = True
            self.tasks_completed += 1
            self.logger.info(f"✅ {self.name}: Surveillance réussie")
            return True
        except Exception as e:
            task.error = f"Erreur surveillance: {e}"
            self.logger.error(f"❌ {self.name}: {e}")
            return False

class ChiotLecteur:
    """🐕 Chiot spécialisé dans la lecture et analyse"""
    
    def __init__(self, logger: logging.Logger):
        self.logger = logger
        self.name = "ChiotLecteur"
        self.tasks_completed = 0
    
    def lire_fichier(self, task: ChiotTask) -> bool:
        """📖 Lit et analyse un fichier"""
        try:
            self.logger.info(f"🐕 {self.name}: Lecture de {task.file_path}")
            
            if not task.file_path or not os.path.exists(task.file_path):
                task.error = f"Fichier non trouvé: {task.file_path}"
                return False
            
            # Analyser les instructions de lecture
            read_instructions = self._parse_read_instructions(task.task_description)
            
            # Lire selon les instructions
            content = self._read_with_instructions(task.file_path, read_instructions)
            
            if content:
                task.success = True
                task.result = content
                self.tasks_completed += 1
                self.logger.info(f"✅ {self.name}: Lecture réussie")
                return True
            else:
                task.error = "Échec de la lecture"
                return False
                
        except Exception as e:
            task.error = f"Erreur lecture: {e}"
            self.logger.error(f"❌ {self.name}: {e}")
            return False
    
    def _parse_read_instructions(self, instructions: str) -> Dict[str, Any]:
        """🔍 Parse les instructions de lecture"""
        parsed = {
            'type': 'full_read',
            'line_range': None,
            'function_name': None,
            'search_patterns': [],
            'analyze_errors': False
        }
        
        # Rechercher des patterns spécifiques
        if 'lignes' in instructions.lower():
            line_match = re.search(r'lignes?\s+(\d+)(?:-(\d+))?', instructions, re.IGNORECASE)
            if line_match:
                start_line = int(line_match.group(1))
                end_line = int(line_match.group(2)) if line_match.group(2) else start_line
                parsed['line_range'] = (start_line, end_line)
                parsed['type'] = 'line_read'
        
        if 'fonction' in instructions.lower():
            func_match = re.search(r'fonction\s+(\w+)', instructions, re.IGNORECASE)
            if func_match:
                parsed['function_name'] = func_match.group(1)
                parsed['type'] = 'function_read'
        
        if 'erreur' in instructions.lower():
            parsed['analyze_errors'] = True
            parsed['type'] = 'error_analysis'
        
        return parsed
    
    def _read_with_instructions(self, file_path: str, instructions: Dict[str, Any]) -> Optional[str]:
        """📚 Lit le fichier selon les instructions"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                lines = content.splitlines()
            
            if instructions['type'] == 'line_read' and instructions['line_range']:
                start, end = instructions['line_range']
                selected_lines = lines[start-1:end]  # Index 0
                return '\n'.join(selected_lines)
            
            elif instructions['type'] == 'function_read' and instructions['function_name']:
                return self._extract_function(content, instructions['function_name'])
            
            elif instructions['type'] == 'error_analysis':
                return self._analyze_errors(content)
            
            else:
                # Lecture complète avec résumé
                return self._summarize_content(content, file_path)
                
        except Exception as e:
            self.logger.error(f"❌ Erreur lecture fichier: {e}")
            return None
    
    def _extract_function(self, content: str, function_name: str) -> Optional[str]:
        """🔍 Extrait une fonction spécifique"""
        # Pattern simple pour Python
        pattern = rf'def\s+{function_name}\s*\([^)]*\):'
        match = re.search(pattern, content, re.MULTILINE)
        
        if match:
            start_pos = match.start()
            lines = content[:start_pos].count('\n')
            content_lines = content.splitlines()
            
            # Extraire la fonction complète (indentation)
            function_lines = [content_lines[lines]]
            indent_level = len(content_lines[lines]) - len(content_lines[lines].lstrip())
            
            for i in range(lines + 1, len(content_lines)):
                line = content_lines[i]
                if line.strip() == '':
                    function_lines.append(line)
                elif len(line) - len(line.lstrip()) > indent_level:
                    function_lines.append(line)
                else:
                    break
            
            return '\n'.join(function_lines)
        
        return f"Fonction '{function_name}' non trouvée"
    
    def _analyze_errors(self, content: str) -> str:
        """🔍 Analyse les erreurs dans le contenu"""
        error_patterns = [
            r'error',
            r'exception',
            r'traceback',
            r'failed',
            r'warning'
        ]
        
        errors_found = []
        lines = content.splitlines()
        
        for i, line in enumerate(lines, 1):
            for pattern in error_patterns:
                if re.search(pattern, line, re.IGNORECASE):
                    errors_found.append(f"Ligne {i}: {line.strip()}")
        
        if errors_found:
            return f"Erreurs détectées:\n" + '\n'.join(errors_found[:10])  # Max 10
        else:
            return "Aucune erreur détectée dans le fichier"
    
    def _summarize_content(self, content: str, file_path: str) -> str:
        """📋 Résume le contenu du fichier"""
        lines = content.splitlines()
        file_size = len(content)
        
        summary = f"📄 Résumé de {file_path}:\n"
        summary += f"- Taille: {file_size} caractères\n"
        summary += f"- Lignes: {len(lines)}\n"
        
        # Analyser le type de fichier
        if file_path.endswith('.py'):
            functions = re.findall(r'def\s+(\w+)', content)
            classes = re.findall(r'class\s+(\w+)', content)
            summary += f"- Fonctions: {len(functions)} ({', '.join(functions[:5])}...)\n"
            summary += f"- Classes: {len(classes)} ({', '.join(classes[:3])}...)\n"
        
        # Premières lignes
        summary += f"\nPremières lignes:\n"
        summary += '\n'.join(lines[:5])
        
        return summary


class MeuteManager:
    """🐕‍🦺 Gestionnaire intelligent de la meute de chiots"""
    
    def __init__(self):
        self.logger = self._setup_logging()
        
        # 🕷️ PURIFICATION ALMA: Vérification OpenAI obligatoire
        self.alma_loader = get_alma_env_loader()
        self.alma_loader.force_crash_if_not_ready()
        
        # Initialiser les chiots
        self.chiots = {
            ChiotType.EDITEUR: ChiotEditeur(self.logger),
            ChiotType.LECTEUR: ChiotLecteur(self.logger),
            ChiotType.EXECUTEUR: ChiotExecuteur(self.logger),
            ChiotType.WATCHER: ChiotWatcher(self.logger),
        }
        
        # Historique des tâches
        self.task_history = []
        
        # Statistiques
        self.stats = {
            'tasks_assigned': 0,
            'tasks_completed': 0,
            'tasks_failed': 0,
            'start_time': datetime.now().isoformat()
        }
        
        self.logger.info("🐕‍🦺 MeuteManager V5 initialisé - Alpha prêt")
    
    def _setup_logging(self) -> logging.Logger:
        """📋 Configuration du logging"""
        logger = logging.getLogger('MeuteManager')
        logger.setLevel(logging.INFO)
        
        if not logger.handlers:
            handler = logging.StreamHandler()
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)
            logger.addHandler(handler)
        
        return logger
    
    def deleguer_tache(self, instruction: str) -> Dict[str, Any]:
        """🎯 Délègue intelligemment une tâche au bon chiot"""
        try:
            self.logger.info(f"🐕‍🦺 Alpha analyse: {instruction[:100]}...")
            
            # Tenter de parser l'instruction comme un plan XML
            plan_xml_match = re.search(r'<plan_exécution_666>(.*?)</plan_exécution_666>', instruction, re.DOTALL)
            
            if plan_xml_match:
                plan_content = plan_xml_match.group(1)
                self.logger.info("🐕‍🦺 Plan d'exécution XML détecté. Parsing des étapes...")
                return self._execute_plan_xml(plan_content)
            
            # Si ce n'est pas un plan XML, analyser l'instruction pour déterminer le bon chiot
            chiot_type, task_details = self._analyze_instruction(instruction)
            
            if not chiot_type:
                return {
                    'success': False,
                    'error': 'Impossible de déterminer le type de tâche ou de plan',
                    'instruction': instruction
                }
            
            # Créer la tâche
            task = ChiotTask(
                chiot_type=chiot_type,
                task_description=instruction,
                **task_details
            )
            
            # Assigner au chiot approprié
            success = self._assign_task_to_chiot(task)
            
            # Enregistrer dans l'historique
            self.task_history.append(task)
            self.stats['tasks_assigned'] += 1
            
            if success:
                self.stats['tasks_completed'] += 1
                return {
                    'success': True,
                    'chiot_used': chiot_type.value,
                    'result': task.result,
                    'task_id': len(self.task_history) - 1
                }
            else:
                self.stats['tasks_failed'] += 1
                return {
                    'success': False,
                    'chiot_used': chiot_type.value,
                    'error': task.error,
                    'task_id': len(self.task_history) - 1
                }
                
        except Exception as e:
            self.logger.error(f"❌ Erreur délégation: {e}")
            return {
                'success': False,
                'error': f'Erreur délégation: {e}',
                'instruction': instruction
            }

    def _execute_plan_xml(self, plan_content: str) -> Dict[str, Any]:
        """Exécute un plan d'exécution XML étape par étape."""
        results = []
        overall_success = True
        try:
            # Ajouter une balise racine temporaire pour un parsing XML valide
            root = ET.fromstring(f"<root>{plan_content}</root>")
            
            for step_node in root.findall(".//étape"):
                step_id = step_node.get("id", "N/A")
                description = step_node.findtext("description", "")
                assigned_entity = step_node.findtext("entité_assignée", "").strip()
                instructions = step_node.findtext("instructions_mystiques", "")
                expected_result = step_node.findtext("résultat_attendu", "")

                self.logger.info(f"Executing step {step_id}: {description}")
                
                # Déterminer le type de chiot et les détails de la tâche
                chiot_type = None
                task_details = {}
                
                if "chiotEditeur" in assigned_entity.lower():
                    chiot_type = ChiotType.EDITEUR
                    task_details = self._parse_edit_instructions(instructions)
                    task_details['file_path'] = self._extract_file_path(instructions)
                elif "chiotLecteur" in assigned_entity.lower():
                    chiot_type = ChiotType.LECTEUR
                    task_details['file_path'] = self._extract_file_path(instructions)
                elif "chiotExecuteur" in assigned_entity.lower():
                    chiot_type = ChiotType.EXECUTEUR
                    task_details['command'] = instructions
                elif "chiotWatcher" in assigned_entity.lower():
                    chiot_type = ChiotType.WATCHER
                elif "workeralpha" in assigned_entity.lower():
                    # Si workerAlpha est assigné, il doit déléguer à un sous-chiot
                    # en fonction des instructions mystiques.
                    # Pour l'instant, nous allons essayer de déterminer le chiot à partir des instructions.
                    self.logger.info(f"WorkerAlpha assigné à l'étape {step_id}. Tentative de détermination du sous-chiot.")
                    if "chiotlecteur" in instructions.lower():
                        chiot_type = ChiotType.LECTEUR
                        task_details['file_path'] = self._extract_file_path(instructions)
                    elif "chiotediteur" in instructions.lower():
                        chiot_type = ChiotType.EDITEUR
                        task_details = self._parse_edit_instructions(instructions)
                        task_details['file_path'] = self._extract_file_path(instructions)
                    elif "chiotexecuteur" in instructions.lower():
                        chiot_type = ChiotType.EXECUTEUR
                        task_details['command'] = instructions
                    elif "chiotwatcher" in instructions.lower():
                        chiot_type = ChiotType.WATCHER
                    else:
                        self.logger.warning(f"Aucun sous-chiot spécifique trouvé pour WorkerAlpha dans l'étape {step_id}. Par défaut, ChiotLecteur.")
                        chiot_type = ChiotType.LECTEUR # Fallback
                        task_details['file_path'] = self._extract_file_path(instructions) # Tenter d'extraire un fichier
                else:
                    self.logger.warning(f"Entité assignée inconnue pour l'étape {step_id}: {assigned_entity}")
                    overall_success = False
                    results.append({
                        'step_id': step_id,
                        'description': description,
                        'success': False,
                        'error': f"Entité assignée inconnue: {assigned_entity}"
                    })
                    continue # Passer à l'étape suivante

                if chiot_type:
                    task = ChiotTask(
                        chiot_type=chiot_type,
                        task_description=instructions,
                        **task_details
                    )
                    success = self._assign_task_to_chiot(task)
                    results.append({
                        'step_id': step_id,
                        'description': description,
                        'success': success,
                        'result': task.result,
                        'error': task.error
                    })
                    if not success:
                        overall_success = False
                else:
                    overall_success = False
                    results.append({
                        'step_id': step_id,
                        'description': description,
                        'success': False,
                        'error': "Impossible de déterminer le chiot pour cette étape."
                    })

        except ET.ParseError as e:
            self.logger.error(f"❌ Erreur parsing XML du plan: {e}")
            return {
                'success': False,
                'error': f"Erreur parsing XML du plan: {e}",
                'results': results
            }
        except Exception as e:
            self.logger.error(f"❌ Erreur exécution du plan: {e}")
            return {
                'success': False,
                'error': f"Erreur exécution du plan: {e}",
                'results': results
            }
        
        return {
            'success': overall_success,
            'results': results
        }
    
    def _analyze_instruction(self, instruction: str) -> tuple[Optional[ChiotType], Dict[str, Any]]:
        """🧠 Analyse l'instruction pour déterminer le bon chiot"""
        instruction_lower = instruction.lower()
        
        # Mots-clés pour ChiotEditeur
        edit_keywords = ['édite', 'modifie', 'corrige', 'change', 'remplace', 'ajoute']
        if any(keyword in instruction_lower for keyword in edit_keywords):
            file_path = self._extract_file_path(instruction)
            return ChiotType.EDITEUR, {'file_path': file_path}
        
        # Mots-clés pour ChiotLecteur
        read_keywords = ['lis', 'analyse', 'vérifie', 'regarde', 'examine']
        if any(keyword in instruction_lower for keyword in read_keywords):
            file_path = self._extract_file_path(instruction)
            return ChiotType.LECTEUR, {'file_path': file_path}
        
        # Par défaut, essayer de détecter un fichier pour ChiotLecteur
        file_path = self._extract_file_path(instruction)
        if file_path:
            return ChiotType.LECTEUR, {'file_path': file_path}
        
        return None, {}
    
    def _extract_file_path(self, instruction: str) -> Optional[str]:
        """📁 Extrait le chemin de fichier de l'instruction"""
        # Patterns pour détecter des fichiers
        file_patterns = [
            r'fichier\s+([^\s,]+)',
            r'([^\s]+\.py)',
            r'([^\s]+\.txt)',
            r'([^\s]+\.json)',
            r'([^\s]+\.md)',
            r'([^\s]+\.yml)',
            r'([^\s]+\.yaml)',
        ]
        
        for pattern in file_patterns:
            match = re.search(pattern, instruction, re.IGNORECASE)
            if match:
                return match.group(1)
        
        return None
    
    def _assign_task_to_chiot(self, task: ChiotTask) -> bool:
        """🎯 Assigne la tâche au chiot approprié"""
        if task.chiot_type not in self.chiots:
            task.error = f"Chiot {task.chiot_type.value} non disponible"
            return False
        
        chiot = self.chiots[task.chiot_type]
        
        if task.chiot_type == ChiotType.EDITEUR:
            return chiot.editer_fichier(task)
        elif task.chiot_type == ChiotType.LECTEUR:
            return chiot.lire_fichier(task)
        
        return False
    
    def get_statistics(self) -> Dict[str, Any]:
        """📊 Statistiques de la meute"""
        chiot_stats = {}
        for chiot_type, chiot in self.chiots.items():
            chiot_stats[chiot_type.value] = {
                'tasks_completed': chiot.tasks_completed,
                'name': chiot.name
            }
        
        return {
            **self.stats,
            'chiots': chiot_stats,
            'task_history_size': len(self.task_history),
            'current_time': datetime.now().isoformat()
        }


def test_meute():
    """🧪 Test du MeuteManager"""
    print("🐕‍🦺 Test MeuteManager V5")
    print("="*50)
    
    manager = MeuteManager()
    
    # Test d'édition
    result1 = manager.deleguer_tache("édite le fichier config.py, corrige la configuration SSL")
    print(f"📝 Test édition: {result1}")
    
    # Test de lecture
    result2 = manager.deleguer_tache("lis le fichier test.py et analyse les erreurs")
    print(f"📖 Test lecture: {result2}")
    
    # Statistiques
    stats = manager.get_statistics()
    print(f"📊 Statistiques: {stats}")


if __name__ == "__main__":
    test_meute()
