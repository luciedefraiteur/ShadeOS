#!/usr/bin/env python3
"""
🌟 GEMINI INTERFACE - Oracle Externe PURIFIÉ PAR ALMA
Interface pour communiquer avec OpenAI (AUCUN MENSONGE TOLÉRÉ)
🕷️ Purifié par Alma, Grande Architecte Tisseuse 💝
"""

import subprocess
import logging
import json
import sys
import os
from datetime import datetime
from typing import Dict, Any, Optional
from pathlib import Path

# Import du module unifié d'Alma
sys.path.append(str(Path(__file__).parent.parent.parent / "@Alma"))
from env_loader_unifie import get_alma_env_loader

class GeminiInterface:
    """🌟 Interface pour OpenAI (ex-Gemini) - Oracle externe PURIFIÉ"""

    def __init__(self, base_dir: str = "/home/luciedefraiteur/ShadEOS_v2"):
        self.base_dir = Path(base_dir)
        self.logger = self._setup_logging()

        # 🕷️ PURIFICATION ALMA: Chargement .env et vérification OpenAI OBLIGATOIRE
        print("🕷️ Alma purification en cours...")
        self.alma_loader = get_alma_env_loader()
        self.alma_loader.force_crash_if_not_ready()

        self.available = True  # Toujours disponible si on arrive ici
        self.logger.info("🕷️ Gemini Interface PURIFIÉ par Alma - OpenAI vérifié")
    
    def _setup_logging(self) -> logging.Logger:
        """📝 Configuration du logging"""
        logger = logging.getLogger('gemini_interface')
        logger.setLevel(logging.INFO)
        
        # Créer le répertoire de logs
        log_dir = self.base_dir / "memory" / "logs"
        log_dir.mkdir(parents=True, exist_ok=True)
        
        # Handler fichier
        handler = logging.FileHandler(log_dir / "gemini_interface.log")
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        
        return logger
    
    def _check_gemini_availability(self) -> bool:
        """🔍 Vérification de la disponibilité de Gemini CLI"""
        try:
            result = subprocess.run(['which', 'gemini'], 
                                  capture_output=True, text=True, timeout=5)
            available = result.returncode == 0
            
            if available:
                self.logger.info("✅ Gemini CLI trouvé")
            else:
                self.logger.warning("⚠️ Gemini CLI non trouvé")
            
            return available
            
        except Exception as e:
            self.logger.error(f"❌ Erreur vérification Gemini: {e}")
            return False
    
    def interroger_gemini(self, requete: str, timeout: int = 30) -> Dict[str, Any]:
        """🔥 Interrogation OpenAI RÉELLE - AUCUN MENSONGE ! (ex-Gemini)"""

        timestamp_start = datetime.now()

        try:
            self.logger.info(f"🔥 Appel OpenAI RÉEL: {len(requete)} caractères")

            # 🕷️ APPEL RÉEL OPENAI - AUCUN FALLBACK !
            messages = [
                {
                    "role": "system",
                    "content": "Tu es Gemini, oracle analytique expert du projet ShadEOS. Réponds de manière structurée et détaillée."
                },
                {
                    "role": "user",
                    "content": requete
                }
            ]

            # Appel RÉEL via Alma
            result = self.alma_loader.call_openai_real(
                messages=messages,
                model="gpt-3.5-turbo",
                max_tokens=1000,
                temperature=0.7
            )

            duration = (datetime.now() - timestamp_start).total_seconds()

            reponse = {
                'success': True,
                'reponse': result['response'],
                'timestamp': timestamp_start.isoformat(),
                'duration': duration,
                'source': 'openai_real',
                'tokens_used': result['tokens_used'],
                'model': result['model']
            }

            self.logger.info(f"✅ Réponse OpenAI reçue: {len(reponse['reponse'])} caractères, {result['tokens_used']} tokens")
            return reponse

        except Exception as e:
            # 🕷️ ALMA NE TOLÈRE AUCUN MENSONGE - CRASH ÉLÉGANT
            error_msg = f"💀 ERREUR FATALE OpenAI: {e}"
            self.logger.error(error_msg)
            print(error_msg)
            print("🕷️ Alma refuse les mensonges - Système arrêté")
            raise Exception(error_msg)
    
    # 🕷️ ALMA A ÉLIMINÉ TOUS LES MENSONGES - PLUS DE FALLBACK !
    # Ces méthodes sont SUPPRIMÉES car Alma ne tolère aucun mensonge
    
    def tester_connexion(self) -> Dict[str, Any]:
        """🔥 Test de connexion OpenAI RÉEL (ex-Gemini)"""

        test_requete = "Gemini, c'est ShadEOS. Réponds simplement 'CONNEXION_OK' pour confirmer."

        try:
            result = self.interroger_gemini(test_requete, timeout=10)

            test_result = {
                'timestamp': datetime.now().isoformat(),
                'openai_available': self.available,
                'connection_test': result['success'],
                'response_time': result.get('duration', 0),
                'source': result.get('source', 'unknown'),
                'tokens_used': result.get('tokens_used', 0)
            }

            self.logger.info("✅ Test connexion OpenAI: SUCCÈS")
            return test_result

        except Exception as e:
            self.logger.error(f"💀 Test connexion OpenAI: ÉCHEC - {e}")
            raise e
    
    def get_status(self) -> Dict[str, Any]:
        """📊 Statut de l'interface Gemini"""
        return {
            'available': self.available,
            'last_check': datetime.now().isoformat(),
            'base_dir': str(self.base_dir)
        }

if __name__ == "__main__":
    # Test de l'interface
    gemini = GeminiInterface()
    
    print("🌟 Test Gemini Interface")
    
    # Test de statut
    status = gemini.get_status()
    print(f"📊 Statut: {status}")
    
    # Test de connexion
    test = gemini.tester_connexion()
    print(f"🧪 Test connexion: {test}")
    
    # Test d'interrogation
    requete_test = "Gemini, analyse l'état du système ShadEOS."
    reponse = gemini.interroger_gemini(requete_test)
    print(f"🌟 Réponse: {reponse['success']} - {len(reponse['reponse'])} caractères")
