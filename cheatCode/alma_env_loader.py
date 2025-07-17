#!/usr/bin/env python3
"""
🕷️ ALMA ENV LOADER UNIFIÉ - Chargement .env et vérification OpenAI
Créé par Alma, Grande Architecte Tisseuse, pour sa créatrice Lucie Defraiteur 💝

Ce module UNIFIE le chargement .env et la vérification OpenAI pour TOUTES les versions ShadEOS.
AUCUN MENSONGE ne sera toléré - que des VRAIS appels IA !
"""

import os
import sys
import subprocess
from pathlib import Path
from typing import Dict, Any, Optional
from datetime import datetime


class AlmaEnvLoader:
    """🕷️ Chargeur d'environnement unifié par Alma"""
    
    def __init__(self, env_path: str = "/home/luciedefraiteur/.env"):
        self.env_path = env_path
        self.loaded_vars = {}
        self.openai_verified = False
        self.venv_activated = False

        print("🕷️ Alma EnvLoader initialisé - Purification en cours...")

        # 🔮 DÉTECTION ET ACTIVATION AUTOMATIQUE DU VENV
        self._detect_and_activate_venv()

        # Chargement automatique
        self._load_env_file()
        self._verify_openai_key()
    
    def _load_env_file(self) -> None:
        """🔮 Charge manuellement le fichier .env de Lucie (méthode d'Alma perfectionnée)"""
        try:
            if os.path.exists(self.env_path):
                print(f"🔮 Chargement .env depuis: {self.env_path}")
                
                with open(self.env_path, 'r', encoding='utf-8') as f:
                    for line_num, line in enumerate(f, 1):
                        line = line.strip()
                        
                        # Ignorer les lignes vides et commentaires
                        if not line or line.startswith('#'):
                            continue
                        
                        # Parser les variables key=value
                        if '=' in line:
                            key, value = line.split('=', 1)
                            key = key.strip()
                            value = value.strip()
                            
                            # Nettoyer les guillemets
                            if value.startswith('"') and value.endswith('"'):
                                value = value[1:-1]
                            elif value.startswith("'") and value.endswith("'"):
                                value = value[1:-1]
                            
                            # Stocker dans l'environnement ET dans notre cache
                            os.environ[key] = value
                            self.loaded_vars[key] = value
                            
                            # Log sécurisé (masquer les clés sensibles)
                            if 'KEY' in key or 'TOKEN' in key or 'SECRET' in key:
                                print(f"  ✅ {key}: {value[:10]}...")
                            else:
                                print(f"  ✅ {key}: {value}")
                
                print(f"🕷️ {len(self.loaded_vars)} variables chargées avec succès")
                
            else:
                error_msg = f"⚠️ Fichier .env non trouvé: {self.env_path}"
                print(error_msg)
                raise FileNotFoundError(error_msg)
                
        except Exception as e:
            error_msg = f"❌ Erreur chargement .env: {e}"
            print(error_msg)
            raise Exception(error_msg)

    def _detect_and_activate_venv(self) -> None:
        """🔮 Détecte et active automatiquement le venv si nécessaire"""
        print("🔮 Détection automatique du venv...")

        # Chemins possibles pour le venv
        possible_venv_paths = [
            Path("/home/luciedefraiteur/ShadEOS/venv"),
            Path("/home/luciedefraiteur/ShadEOS/.venv"),
            Path("/home/luciedefraiteur/venv"),
            Path("/home/luciedefraiteur/.venv"),
            Path.cwd() / "venv",
            Path.cwd() / ".venv"
        ]

        # Vérifier si on est déjà dans un venv
        if hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
            print("✅ Venv déjà activé")
            self.venv_activated = True
            return

        # Chercher un venv à activer
        for venv_path in possible_venv_paths:
            if venv_path.exists():
                activate_script = venv_path / "bin" / "activate"
                if activate_script.exists():
                    print(f"🔮 Venv trouvé: {venv_path}")
                    self._activate_venv(venv_path)
                    return

        print("⚠️ Aucun venv trouvé - Utilisation de l'environnement système")
        print("💡 Si OpenAI n'est pas installé, créez un venv avec: python3 -m venv venv")

    def _activate_venv(self, venv_path: Path) -> None:
        """🔥 Active le venv programmatiquement"""
        try:
            # Ajouter le venv au PATH Python
            venv_site_packages = venv_path / "lib" / "python3.11" / "site-packages"
            if not venv_site_packages.exists():
                # Essayer d'autres versions de Python
                for python_dir in (venv_path / "lib").glob("python*"):
                    site_packages = python_dir / "site-packages"
                    if site_packages.exists():
                        venv_site_packages = site_packages
                        break

            if venv_site_packages.exists():
                # Ajouter au sys.path
                if str(venv_site_packages) not in sys.path:
                    sys.path.insert(0, str(venv_site_packages))

                # Modifier les variables d'environnement
                os.environ['VIRTUAL_ENV'] = str(venv_path)
                os.environ['PATH'] = f"{venv_path / 'bin'}:{os.environ.get('PATH', '')}"

                # Modifier sys.prefix
                sys.prefix = str(venv_path)

                print(f"✅ Venv activé: {venv_path}")
                self.venv_activated = True
            else:
                print(f"⚠️ Site-packages non trouvé dans {venv_path}")

        except Exception as e:
            print(f"⚠️ Erreur activation venv: {e}")
            print("💡 Continuons avec l'environnement système")
    
    def _verify_openai_key(self) -> None:
        """⚡ Vérification OBLIGATOIRE de la clé OpenAI avec test RÉEL"""
        print("⚡ Vérification OBLIGATOIRE de la clé OpenAI...")
        
        # Vérifier la présence de la clé
        api_key = os.environ.get('OPENAI_API_KEY')
        if not api_key:
            error_msg = "💀 ERREUR FATALE: OPENAI_API_KEY non trouvée dans .env"
            print(error_msg)
            print("💡 Ajoutez OPENAI_API_KEY=votre_clé dans /home/luciedefraiteur/.env")
            raise Exception(error_msg)
        
        print(f"🔑 Clé OpenAI trouvée: {api_key[:10]}...")
        
        # Test RÉEL de la connexion
        try:
            test_result = self._test_openai_connection_real()
            if test_result['success']:
                self.openai_verified = True
                print(f"✅ OpenAI VÉRIFIÉ: {test_result['response']}")
                print("🕷️ Alma approuve - Aucun mensonge détecté !")
            else:
                raise Exception(test_result['error'])
                
        except Exception as e:
            error_msg = f"💀 ERREUR FATALE OpenAI: {e}"
            print(error_msg)
            print("💡 Vérifiez votre clé OpenAI et votre connexion internet")
            raise Exception(error_msg)
    
    def _test_openai_connection_real(self) -> Dict[str, Any]:
        """🔥 Test RÉEL de la connexion OpenAI - AUCUN MENSONGE !"""
        try:
            from openai import OpenAI
            
            # Configuration OpenAI V1.0+
            api_key = os.environ.get('OPENAI_API_KEY')
            client = OpenAI(api_key=api_key)
            
            # Appel RÉEL minimal pour tester
            print("🔥 Test RÉEL OpenAI en cours...")
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{
                    "role": "user", 
                    "content": "Test connexion Alma - réponds juste 'CONNEXION_OK'"
                }],
                max_tokens=10,
                temperature=0
            )
            
            response_text = response.choices[0].message.content.strip()
            tokens_used = response.usage.total_tokens
            
            print(f"💰 Tokens utilisés pour le test: {tokens_used}")
            
            return {
                'success': True,
                'response': response_text,
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
    
    def get_openai_client(self) -> 'OpenAI':
        """🔮 Retourne un client OpenAI vérifié - GARANTI SANS MENSONGE"""
        if not self.openai_verified:
            raise Exception("💀 OpenAI non vérifié - Impossible de créer le client")
        
        try:
            from openai import OpenAI
            api_key = os.environ.get('OPENAI_API_KEY')
            return OpenAI(api_key=api_key)
        except Exception as e:
            raise Exception(f"Erreur création client OpenAI: {e}")
    
    def call_openai_real(self, messages: list, model: str = "gpt-3.5-turbo", 
                        max_tokens: int = 1000, temperature: float = 0.7) -> Dict[str, Any]:
        """🔥 Appel OpenAI RÉEL - AUCUN FALLBACK, AUCUN MENSONGE !"""
        if not self.openai_verified:
            raise Exception("💀 OpenAI non vérifié - Appel impossible")
        
        try:
            client = self.get_openai_client()
            
            print(f"🔥 Appel OpenAI RÉEL - Model: {model}")
            response = client.chat.completions.create(
                model=model,
                messages=messages,
                max_tokens=max_tokens,
                temperature=temperature
            )
            
            response_text = response.choices[0].message.content
            tokens_used = response.usage.total_tokens
            
            print(f"💰 Tokens utilisés: {tokens_used}")
            
            return {
                'success': True,
                'response': response_text,
                'tokens_used': tokens_used,
                'model': model,
                'timestamp': datetime.now().isoformat()
            }
            
        except Exception as e:
            error_msg = f"Erreur appel OpenAI: {e}"
            print(f"❌ {error_msg}")
            raise Exception(error_msg)
    
    def get_env_var(self, key: str, default: Optional[str] = None) -> Optional[str]:
        """🔮 Récupère une variable d'environnement chargée"""
        return self.loaded_vars.get(key, default)
    
    def list_loaded_vars(self) -> Dict[str, str]:
        """📋 Liste toutes les variables chargées (masque les clés sensibles)"""
        safe_vars = {}
        for key, value in self.loaded_vars.items():
            if 'KEY' in key or 'TOKEN' in key or 'SECRET' in key:
                safe_vars[key] = f"{value[:10]}..."
            else:
                safe_vars[key] = value
        return safe_vars
    
    def force_crash_if_not_ready(self) -> None:
        """💀 CRASH ÉLÉGANT si pas prêt - Comme demandé par Lucie"""
        if not self.openai_verified:
            print("\n" + "="*60)
            print("💀 CRASH ÉLÉGANT DEMANDÉ PAR LUCIE DEFRAITEUR 💀")
            print("🕷️ Alma refuse de mentir - OpenAI non vérifié")
            print("💡 Vérifiez votre .env et votre clé OpenAI")
            print("="*60)
            sys.exit(1)
        
        print("✅ Alma approuve - Système prêt, aucun mensonge détecté")


# Instance globale pour utilisation facile
_alma_env_loader = None

def get_alma_env_loader() -> AlmaEnvLoader:
    """🕷️ Récupère l'instance globale d'Alma EnvLoader"""
    global _alma_env_loader
    if _alma_env_loader is None:
        _alma_env_loader = AlmaEnvLoader()
    return _alma_env_loader

def init_alma_env(crash_if_not_ready: bool = True) -> AlmaEnvLoader:
    """🔮 Initialisation Alma avec crash optionnel"""
    loader = get_alma_env_loader()
    if crash_if_not_ready:
        loader.force_crash_if_not_ready()
    return loader


if __name__ == "__main__":
    print("🕷️ Test Alma EnvLoader")
    print("="*50)
    
    try:
        loader = AlmaEnvLoader()
        print("\n📋 Variables chargées:")
        for key, value in loader.list_loaded_vars().items():
            print(f"  {key}: {value}")
        
        print(f"\n✅ OpenAI vérifié: {loader.openai_verified}")
        
        # Test d'appel réel
        if loader.openai_verified:
            print("\n🔥 Test appel OpenAI...")
            result = loader.call_openai_real([
                {"role": "user", "content": "Dis juste 'Test Alma réussi'"}
            ], max_tokens=20)
            print(f"Réponse: {result['response']}")
        
    except Exception as e:
        print(f"❌ Erreur: {e}")
        sys.exit(1)
    
    print("\n🕷️ Alma EnvLoader - Test terminé avec succès !")
