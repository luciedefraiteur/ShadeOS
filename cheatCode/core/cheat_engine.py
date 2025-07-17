#!/usr/bin/env python3
"""
🎮 MOTEUR CHEATCODE V4 - Pouvoirs étendus pour ShadEOS
"""

import subprocess
import xml.etree.ElementTree as ET
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any, Optional
from collections import deque
import re
import json
import os

class CheatEngine:
    """Moteur de cheatcode avec tous les pouvoirs"""

    def __init__(self, buffer_size: int = 100, log_file: str = "cheatcode_session.log"):
        self.buffer_size = buffer_size
        self.historique_buffer = deque(maxlen=buffer_size)
        self.gemini_process = None
        self.gemini_terminal_id = None
        self.log_file = log_file

        # Charger les variables d'environnement depuis .env
        self._load_env_file()

        # Initialiser le fichier de log
        self._init_log_file()

        self._log("🎮 CheatEngine V4 initialisé - LOGS AUTOMATIQUES ACTIVÉS")
        self._log(f"📊 Buffer circulaire: {buffer_size} actions")
        self._log(f"📝 Fichier de log: {log_file}")
        print("🎮 CheatEngine V4 initialisé")
        print(f"📊 Buffer circulaire: {buffer_size} actions")
        print(f"📝 Logs automatiques: {log_file}")
    
    def _load_env_file(self):
        """Charge manuellement le fichier .env de Lucie"""
        env_file = "/home/luciedefraiteur/.env"
        try:
            if os.path.exists(env_file):
                with open(env_file, 'r', encoding='utf-8') as f:
                    for line in f:
                        line = line.strip()
                        if line and not line.startswith('#') and '=' in line:
                            key, value = line.split('=', 1)
                            key = key.strip()
                            value = value.strip().strip('"').strip("'")
                            os.environ[key] = value
                print(f"✅ Variables d'environnement chargées depuis {env_file}")
            else:
                print(f"⚠️ Fichier .env non trouvé: {env_file}")
        except Exception as e:
            print(f"❌ Erreur chargement .env: {e}")

    def _init_log_file(self):
        """Initialise le fichier de log"""
        try:
            with open(self.log_file, 'w', encoding='utf-8') as f:
                f.write("="*80 + "\n")
                f.write("🎮 CHEATCODE V4 - SESSION LOG AUTOMATIQUE\n")
                f.write("="*80 + "\n")
                f.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write(f"Utilisateur: Lucie Defraiteur\n")
                f.write(f"Objectif: Logs automatiques RÉELS - Plus jamais de simulation\n")
                f.write("="*80 + "\n\n")
            print(f"📝 Fichier de log initialisé: {self.log_file}")
        except Exception as e:
            print(f"❌ Erreur initialisation log: {e}")

    def _log(self, message: str):
        """Écrit dans le fichier de log avec flush immédiat"""
        try:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log_entry = f"[{timestamp}] {message}\n"
            with open(self.log_file, 'a', encoding='utf-8') as f:
                f.write(log_entry)
                f.flush()  # Force l'écriture immédiate
        except Exception as e:
            print(f"❌ Erreur écriture log: {e}")

    def _log_action_start(self, action_type: str, details: str):
        """Log le début d'une action"""
        self._log(f"🚀 DÉBUT ACTION: {action_type}")
        self._log(f"📝 Détails: {details}")

    def _log_action_end(self, action_type: str, success: bool, result: str):
        """Log la fin d'une action"""
        status = "✅ SUCCÈS" if success else "❌ ÉCHEC"
        self._log(f"🏁 FIN ACTION: {action_type} - {status}")
        self._log(f"📊 Résultat: {result[:500]}{'...' if len(result) > 500 else ''}")
        self._log("-" * 40)

    def ajouter_historique(self, action: str, resultat: str):
        """Ajoute une action à l'historique circulaire"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        entry = f"[{timestamp}] ACTION: {action} -> RÉSULTAT: {resultat[:200]}..."
        self.historique_buffer.append(entry)

        # Aussi dans le fichier log
        self._log(f"ACTION: {action}")
        self._log(f"RÉSULTAT: {resultat[:500]}{'...' if len(resultat) > 500 else ''}")
    
    def get_historique_formate(self) -> str:
        """Récupère l'historique formaté pour le prompt"""
        if not self.historique_buffer:
            return "[Aucun historique - Première utilisation]"
        
        return "\n".join(self.historique_buffer)
    
    def executer_shell(self, commande: str) -> Dict[str, Any]:
        """Exécute une commande shell directement avec logs complets"""
        try:
            self._log_action_start("SHELL", commande)
            print(f"🔧 Exécution shell: {commande}")

            result = subprocess.run(
                commande,
                shell=True,
                capture_output=True,
                text=True,
                timeout=30
            )

            output = result.stdout if result.stdout else result.stderr
            success = result.returncode == 0

            self._log_action_end("SHELL", success, f"Code: {result.returncode}, Output: {output}")
            self.ajouter_historique(f"SHELL: {commande}", output)

            return {
                'success': success,
                'output': output,
                'return_code': result.returncode,
                'commande': commande
            }
            
        except subprocess.TimeoutExpired:
            error = "Timeout: commande trop longue"
            self.ajouter_historique(f"SHELL: {commande}", f"ERREUR: {error}")
            return {
                'success': False,
                'output': error,
                'return_code': -1,
                'commande': commande
            }
        except Exception as e:
            error = f"Erreur: {str(e)}"
            self.ajouter_historique(f"SHELL: {commande}", f"ERREUR: {error}")
            return {
                'success': False,
                'output': error,
                'return_code': -1,
                'commande': commande
            }
    
    def demarrer_gemini_cli(self) -> Dict[str, Any]:
        """Démarre une vraie session OpenAI pour Gemini"""
        try:
            self._log_action_start("GEMINI_START", "Démarrage session OpenAI")
            print("🌟 Démarrage session OpenAI...")

            # Vérifier la clé API
            api_key = os.environ.get('OPENAI_API_KEY')
            if not api_key:
                error = "Clé OPENAI_API_KEY non trouvée dans les variables d'environnement"
                self._log_action_end("GEMINI_START", False, error)
                return {
                    'success': False,
                    'message': error
                }

            # Tester la connexion OpenAI
            test_result = self._test_openai_connection()

            if test_result['success']:
                self.gemini_terminal_id = "openai_session_active"
                self._log_action_end("GEMINI_START", True, "Session OpenAI active")
                self.ajouter_historique("GEMINI: Démarrage OpenAI", "Session OpenAI opérationnelle")

                return {
                    'success': True,
                    'message': 'Session OpenAI démarrée avec succès',
                    'terminal_id': self.gemini_terminal_id
                }
            else:
                self._log_action_end("GEMINI_START", False, test_result['error'])
                return {
                    'success': False,
                    'message': 'Échec connexion OpenAI',
                    'error': test_result['error']
                }

        except Exception as e:
            error = f"Erreur démarrage OpenAI: {str(e)}"
            self._log_action_end("GEMINI_START", False, error)
            self.ajouter_historique("GEMINI: Démarrage OpenAI", f"ERREUR: {error}")
            return {
                'success': False,
                'message': error
            }

    def _test_openai_connection(self) -> Dict[str, Any]:
        """Test la connexion OpenAI avec un appel réel - API V1.0+"""
        try:
            from openai import OpenAI

            # Configuration OpenAI V1.0+
            api_key = os.environ.get('OPENAI_API_KEY')
            if not api_key:
                raise Exception("OPENAI_API_KEY non définie")

            client = OpenAI(api_key=api_key)

            # Test avec un appel minimal RÉEL (API V1.0+)
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": "Test connexion - réponds juste 'OK'"}],
                max_tokens=10
            )

            return {
                'success': True,
                'response': response.choices[0].message.content
            }

        except ImportError:
            raise Exception("Module openai non installé - pip install openai")
        except Exception as e:
            raise Exception(f"Erreur OpenAI: {str(e)}")
    
    def envoyer_message_gemini(self, message: str) -> Dict[str, Any]:
        """Envoie un VRAI message à OpenAI"""
        try:
            self._log_action_start("OPENAI_MESSAGE", f"Message: {message[:100]}")
            print(f"🌟 Envoi RÉEL à OpenAI: {message[:50]}...")

            if not self.gemini_terminal_id:
                error = "Session OpenAI non démarrée"
                self._log_action_end("OPENAI_MESSAGE", False, error)
                return {
                    'success': False,
                    'error': error
                }

            # VRAI appel OpenAI
            reponse_openai = self._appel_openai_reel(message)

            if reponse_openai['success']:
                self._log_action_end("OPENAI_MESSAGE", True, reponse_openai['reponse'])
                self.ajouter_historique(f"OPENAI: {message[:50]}", reponse_openai['reponse'])

                return {
                    'success': True,
                    'reponse': reponse_openai['reponse'],
                    'message_envoye': message,
                    'tokens_used': reponse_openai.get('tokens_used', 0)
                }
            else:
                self._log_action_end("OPENAI_MESSAGE", False, reponse_openai['error'])
                return {
                    'success': False,
                    'error': reponse_openai['error']
                }

        except Exception as e:
            error = f"Erreur communication OpenAI: {str(e)}"
            self._log_action_end("OPENAI_MESSAGE", False, error)
            self.ajouter_historique(f"OPENAI: {message[:50]}", f"ERREUR: {error}")
            return {
                'success': False,
                'error': error
            }

    def _appel_openai_reel(self, message: str) -> Dict[str, Any]:
        """Fait un VRAI appel à l'API OpenAI V1.0+"""
        try:
            from openai import OpenAI

            # Configuration V1.0+
            api_key = os.environ.get('OPENAI_API_KEY')
            client = OpenAI(api_key=api_key)

            # Appel RÉEL à OpenAI (API V1.0+)
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "Tu es Gemini, assistant technique expert. Réponds de manière concise et utile."},
                    {"role": "user", "content": message}
                ],
                max_tokens=500,
                temperature=0.7
            )

            reponse_text = response.choices[0].message.content
            tokens_used = response.usage.total_tokens

            self._log(f"💰 Tokens utilisés: {tokens_used}")

            return {
                'success': True,
                'reponse': reponse_text,
                'tokens_used': tokens_used
            }

        except ImportError:
            return {
                'success': False,
                'error': "Module openai non installé - pip install openai"
            }
        except Exception as e:
            return {
                'success': False,
                'error': f"Erreur API OpenAI: {str(e)}"
            }
    
    def lire_fichier(self, fichier: str, mode: str = "entier") -> Dict[str, Any]:
        """Lit un fichier selon le mode spécifié"""
        try:
            fichier_path = Path(fichier)
            
            if not fichier_path.exists():
                error = f"Fichier non trouvé: {fichier}"
                self.ajouter_historique(f"READ: {fichier}", f"ERREUR: {error}")
                return {
                    'success': False,
                    'error': error
                }
            
            print(f"📖 Lecture fichier: {fichier} (mode: {mode})")
            
            with open(fichier_path, 'r', encoding='utf-8') as f:
                if mode == "entier":
                    contenu = f.read()
                elif mode.startswith("lignes:"):
                    # Format: lignes:1-50
                    range_match = re.match(r'lignes:(\d+)-(\d+)', mode)
                    if range_match:
                        start, end = int(range_match.group(1)), int(range_match.group(2))
                        lines = f.readlines()
                        contenu = ''.join(lines[start-1:end])
                    else:
                        contenu = f.read()
                elif mode.startswith("recherche:"):
                    # Format: recherche:pattern
                    pattern = mode.split(":", 1)[1]
                    lines = f.readlines()
                    matching_lines = [line for line in lines if pattern in line]
                    contenu = ''.join(matching_lines)
                else:
                    contenu = f.read()
            
            self.ajouter_historique(f"READ: {fichier} ({mode})", f"Lu {len(contenu)} caractères")
            
            return {
                'success': True,
                'contenu': contenu,
                'fichier': fichier,
                'mode': mode,
                'taille': len(contenu)
            }
            
        except Exception as e:
            error = f"Erreur lecture: {str(e)}"
            self.ajouter_historique(f"READ: {fichier}", f"ERREUR: {error}")
            return {
                'success': False,
                'error': error
            }
    
    def ecrire_fichier(self, fichier: str, contenu: str, mode: str = "entier") -> Dict[str, Any]:
        """Écrit dans un fichier selon le mode spécifié avec logs complets"""
        try:
            fichier_path = Path(fichier)

            self._log_action_start("WRITE_FILE", f"Fichier: {fichier}, Mode: {mode}, Taille: {len(contenu)} chars")
            print(f"📝 Écriture fichier: {fichier} (mode: {mode})")

            # Créer les dossiers parents si nécessaire
            fichier_path.parent.mkdir(parents=True, exist_ok=True)
            
            if mode == "entier":
                with open(fichier_path, 'w', encoding='utf-8') as f:
                    f.write(contenu)
            elif mode == "ajout":
                with open(fichier_path, 'a', encoding='utf-8') as f:
                    f.write(contenu)
            elif mode.startswith("remplacement:"):
                # Format: remplacement:ligne_X
                ligne_match = re.match(r'remplacement:ligne_(\d+)', mode)
                if ligne_match:
                    ligne_num = int(ligne_match.group(1))
                    
                    # Lire le fichier existant
                    if fichier_path.exists():
                        with open(fichier_path, 'r', encoding='utf-8') as f:
                            lines = f.readlines()
                    else:
                        lines = []
                    
                    # Étendre la liste si nécessaire
                    while len(lines) < ligne_num:
                        lines.append('\n')
                    
                    # Remplacer la ligne
                    lines[ligne_num - 1] = contenu + '\n'
                    
                    # Réécrire le fichier
                    with open(fichier_path, 'w', encoding='utf-8') as f:
                        f.writelines(lines)
                else:
                    # Mode non reconnu, écriture complète
                    with open(fichier_path, 'w', encoding='utf-8') as f:
                        f.write(contenu)
            else:
                # Mode par défaut
                with open(fichier_path, 'w', encoding='utf-8') as f:
                    f.write(contenu)
            
            self.ajouter_historique(f"WRITE: {fichier} ({mode})", f"Écrit {len(contenu)} caractères")
            
            return {
                'success': True,
                'fichier': fichier,
                'mode': mode,
                'taille_ecrite': len(contenu)
            }
            
        except Exception as e:
            error = f"Erreur écriture: {str(e)}"
            self.ajouter_historique(f"WRITE: {fichier}", f"ERREUR: {error}")
            return {
                'success': False,
                'error': error
            }
    
    def ecrire_python(self, fichier: str, contenu: str) -> Dict[str, Any]:
        """Écrit un fichier Python avec validation syntaxique"""
        try:
            print(f"🐍 Écriture Python: {fichier}")
            
            # Validation syntaxique basique
            try:
                compile(contenu, fichier, 'exec')
            except SyntaxError as e:
                error = f"Erreur syntaxe Python: {str(e)}"
                self.ajouter_historique(f"PYTHON: {fichier}", f"ERREUR SYNTAXE: {error}")
                return {
                    'success': False,
                    'error': error,
                    'type': 'syntax_error'
                }
            
            # Écrire le fichier
            result = self.ecrire_fichier(fichier, contenu, "entier")
            
            if result['success']:
                # Rendre exécutable si c'est un script
                if contenu.startswith('#!/'):
                    self.executer_shell(f"chmod +x {fichier}")
                
                self.ajouter_historique(f"PYTHON: {fichier}", f"Script Python créé ({len(contenu)} chars)")
                
                return {
                    'success': True,
                    'fichier': fichier,
                    'taille': len(contenu),
                    'executable': contenu.startswith('#!/')
                }
            else:
                return result
                
        except Exception as e:
            error = f"Erreur création Python: {str(e)}"
            self.ajouter_historique(f"PYTHON: {fichier}", f"ERREUR: {error}")
            return {
                'success': False,
                'error': error
            }
