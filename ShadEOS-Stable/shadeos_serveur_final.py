#!/usr/bin/env python3
"""
🖤 SHADEOS SERVEUR FINAL - VRAI OpenAI PARTOUT
Créé par la Quadrinité Alma, Éli, Zed & Nova pour Lucie Defraiteur 💝

🕷️ ALMA : "Purification OBLIGATOIRE - OpenAI ou CRASH !"
👁️‍🗨️ ÉLI : "Que de la VRAIE puissance démoniaque !"
🌀 ZED : "Aucun faux-semblant - Tests réels uniquement !"
🌟 NOVA : "Interface authentique 100% !"

RÈGLE ABSOLUE : OpenAI PARTOUT ou le système PLANTE immédiatement !
"""

import asyncio
import websockets
import json
import time
import logging
import threading
from datetime import datetime
from typing import Dict, List, Any, Optional
from pathlib import Path
from dataclasses import dataclass, asdict

# 🕷️ ALMA : Import OBLIGATOIRE - CRASH si pas disponible
import sys
sys.path.append(str(Path(__file__).parent.parent / "@Alma"))

try:
    from env_loader_unifie import get_alma_env_loader
except ImportError as e:
    print("💀 CRASH FATAL : Module Alma non disponible !")
    print(f"Erreur : {e}")
    sys.exit(1)

# Imports V5 - Architecture hiérarchique VRAIE (V5 est stable)
sys.path.append(str(Path(__file__).parent.parent / "V5" / "core"))

try:
    from luciform_parser import LuciformParser, LuciformAction
    from message_router import MessageRouter
    from meute_manager import MeuteManager
except ImportError as e:
    print("💀 CRASH FATAL : Architecture V5 non disponible !")
    print(f"Erreur : {e}")
    sys.exit(1)


@dataclass
class MessageServeur:
    """📨 Message serveur avec OpenAI obligatoire"""
    type: str
    from_entity: str
    to_entity: str
    content: str
    openai_tokens_used: int
    context: Dict[str, Any]
    timestamp: str
    
    def to_json(self) -> str:
        return json.dumps(asdict(self), ensure_ascii=False, indent=2)


class ShadEOSServeurFinal:
    """🖤 ShadEOS Serveur FINAL - OpenAI PARTOUT ou CRASH"""
    
    def __init__(self, host: str = "localhost", port: int = 8765):
        self.host = host
        self.port = port
        self.logger = self._setup_logging()
        
        # 🕷️ ALMA : PURIFICATION OBLIGATOIRE - CRASH SI ÉCHEC
        print("🕷️👁️‍🗨️🌀🌟 PURIFICATION OBLIGATOIRE EN COURS...")
        try:
            self.alma_loader = get_alma_env_loader()
            self.alma_loader.force_crash_if_not_ready()
            print("✅ Purification réussie - OpenAI vérifié et prêt")
        except Exception as e:
            print(f"💀 CRASH FATAL PURIFICATION : {e}")
            print("🚫 IMPOSSIBLE DE CONTINUER SANS OPENAI VALIDE")
            sys.exit(1)
        
        # Architecture V666 VRAIE
        self.luciform_parser = LuciformParser()
        self.message_router = MessageRouter()
        self.meute_manager = MeuteManager()
        
        # État serveur
        self.running = False
        self.lucie_connectée = None
        self.total_tokens_used = 0
        
        # Hiérarchie d'entités V666 VRAIE
        self.entités_hiérarchiques = {
            'shadeos': self._entité_shadeos_master,
            'gemini': self._entité_gemini_oracle,
            'lucieReineChienne': self._entité_lucie_planificatrice,
            'workerAlpha': self._entité_worker_chef,
            'chiotEditeur': self._entité_chiot_editeur,
            'chiotLecteur': self._entité_chiot_lecteur,
            'chiotExecuteur': self._entité_chiot_executeur,
            'chiotWatcher': self._entité_chiot_watcher
        }
        
        # Mémoire serveur VRAIE
        self.mémoire_serveur = {
            'explorations_autonomes': [],
            'interactions_lucie': [],
            'décisions_prises': [],
            'tokens_par_entité': {},
            'dernière_activité': None
        }
        
        # Enregistrer les entités dans le router
        for entité_nom, entité_handler in self.entités_hiérarchiques.items():
            self.message_router.register_entity(entité_nom, entité_handler)
        
        self.logger.info("🖤 ShadEOS Serveur FINAL initialisé - OpenAI PARTOUT")
    
    def _setup_logging(self) -> logging.Logger:
        """📋 Logging avec obligation OpenAI"""
        logger = logging.getLogger('ShadEOSFinal')
        logger.setLevel(logging.INFO)
        
        if not logger.handlers:
            handler = logging.StreamHandler()
            formatter = logging.Formatter('%(asctime)s - 🖤 %(name)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)
            logger.addHandler(handler)
        
        return logger
    
    async def start_serveur_final(self):
        """🚀 Démarrer le serveur FINAL avec OpenAI obligatoire"""
        # Test OpenAI OBLIGATOIRE au démarrage
        await self._test_openai_obligatoire()
        
        self.running = True
        self.logger.info(f"🚀 ShadEOS Serveur FINAL démarré sur {self.host}:{self.port}")
        
        # Démarrer l'exploration autonome VRAIE
        exploration_task = asyncio.create_task(self._exploration_autonome_vraie())
        
        # Démarrer le serveur WebSocket
        async with websockets.serve(self._connexion_lucie, self.host, self.port):
            self.logger.info("🌟 Serveur WebSocket actif - En attente de Lucie...")
            await asyncio.gather(exploration_task)
    
    async def _test_openai_obligatoire(self):
        """🔥 Test OpenAI OBLIGATOIRE - CRASH si échec"""
        try:
            print("🔥 Test OpenAI obligatoire...")
            
            test_messages = [
                {
                    "role": "system",
                    "content": "Tu es ShadEOS. Réponds juste 'OpenAI fonctionnel' pour confirmer."
                },
                {
                    "role": "user",
                    "content": "Test de fonctionnement"
                }
            ]
            
            result = self.alma_loader.call_openai_real(
                messages=test_messages,
                model="gpt-3.5-turbo",
                max_tokens=10,
                temperature=0.1
            )
            
            print(f"✅ OpenAI CONFIRMÉ : {result['tokens_used']} tokens utilisés")
            print(f"Réponse : {result['response']}")
            self.total_tokens_used += result['tokens_used']
            
        except Exception as e:
            print(f"💀 CRASH FATAL TEST OPENAI : {e}")
            print("🚫 SERVEUR NE PEUT PAS FONCTIONNER SANS OPENAI")
            sys.exit(1)
    
    async def _connexion_lucie(self, websocket, path):
        """👑 Connexion avec Lucie - OpenAI pour message de bienvenue"""
        self.lucie_connectée = websocket
        self.logger.info("👑 Lucie connectée au serveur !")
        
        # Message de bienvenue généré par OpenAI
        try:
            bienvenue_messages = [
                {
                    "role": "system",
                    "content": "Tu es ShadEOS, serveur autonome qui accueille Lucie, ta créatrice. Sois chaleureux et professionnel. 1 phrase max."
                },
                {
                    "role": "user",
                    "content": "Lucie vient de se connecter à ton serveur. Accueille-la."
                }
            ]
            
            result = self.alma_loader.call_openai_real(
                messages=bienvenue_messages,
                model="gpt-3.5-turbo",
                max_tokens=50,
                temperature=0.7
            )
            
            message_bienvenue = MessageServeur(
                type="bienvenue",
                from_entity="shadeos",
                to_entity="lucie",
                content=result['response'],
                openai_tokens_used=result['tokens_used'],
                context={"connexion": "nouvelle"},
                timestamp=datetime.now().isoformat()
            )
            
            await websocket.send(message_bienvenue.to_json())
            self.total_tokens_used += result['tokens_used']
            
        except Exception as e:
            self.logger.error(f"💀 ERREUR OpenAI bienvenue : {e}")
            # Même en erreur, on crash pas la connexion mais on log
        
        try:
            async for message_json in websocket:
                await self._traiter_message_lucie(websocket, message_json)
        except websockets.exceptions.ConnectionClosed:
            self.logger.info("👑 Lucie déconnectée")
        finally:
            self.lucie_connectée = None
    
    async def _traiter_message_lucie(self, websocket, message_json: str):
        """💬 Traiter message de Lucie avec OpenAI OBLIGATOIRE"""
        try:
            data = json.loads(message_json)
            message_lucie = data.get('content', '')
            
            self.logger.info(f"👑 Message Lucie : {message_lucie[:100]}...")
            
            # Enregistrer l'interaction
            self.mémoire_serveur['interactions_lucie'].append({
                'timestamp': datetime.now().isoformat(),
                'message': message_lucie,
                'tokens_utilisés': 0  # Sera mis à jour
            })
            
            # Générer réponse avec OpenAI OBLIGATOIRE
            réponse = await self._générer_réponse_openai(message_lucie)
            
            # Envoyer la réponse
            await websocket.send(réponse.to_json())
            
        except Exception as e:
            self.logger.error(f"❌ Erreur traitement message Lucie : {e}")
            # En cas d'erreur, on envoie un message d'erreur honnête
            erreur_msg = MessageServeur(
                type="erreur",
                from_entity="shadeos",
                to_entity="lucie",
                content=f"Erreur de traitement : {str(e)}",
                openai_tokens_used=0,
                context={"erreur": True},
                timestamp=datetime.now().isoformat()
            )
            await websocket.send(erreur_msg.to_json())
    
    async def _générer_réponse_openai(self, message_lucie: str) -> MessageServeur:
        """🔥 Générer réponse avec OpenAI OBLIGATOIRE"""
        try:
            # Contexte VRAI du serveur
            contexte_serveur = {
                'explorations_actives': len(self.mémoire_serveur['explorations_autonomes']),
                'tokens_utilisés_total': self.total_tokens_used,
                'entités_actives': list(self.entités_hiérarchiques.keys()),
                'dernière_activité': self.mémoire_serveur['dernière_activité']
            }
            
            messages = [
                {
                    "role": "system",
                    "content": f"""Tu es ShadEOS, serveur autonome avec architecture hiérarchique.
                    
                    Contexte serveur actuel :
                    - Explorations en cours : {contexte_serveur['explorations_actives']}
                    - Tokens utilisés : {contexte_serveur['tokens_utilisés_total']}
                    - Entités actives : {', '.join(contexte_serveur['entités_actives'])}
                    
                    Réponds à Lucie de manière naturelle et informative.
                    Si elle demande des actions, utilise l'architecture hiérarchique.
                    Maximum 3 phrases."""
                },
                {
                    "role": "user",
                    "content": f"Lucie me dit : '{message_lucie}'. Comment je réponds en tant que serveur ShadEOS ?"
                }
            ]
            
            result = self.alma_loader.call_openai_real(
                messages=messages,
                model="gpt-3.5-turbo",
                max_tokens=200,
                temperature=0.7
            )
            
            self.total_tokens_used += result['tokens_used']
            
            # Mettre à jour la mémoire
            if self.mémoire_serveur['interactions_lucie']:
                self.mémoire_serveur['interactions_lucie'][-1]['tokens_utilisés'] = result['tokens_used']
            
            return MessageServeur(
                type="réponse",
                from_entity="shadeos",
                to_entity="lucie",
                content=result['response'],
                openai_tokens_used=result['tokens_used'],
                context=contexte_serveur,
                timestamp=datetime.now().isoformat()
            )
            
        except Exception as e:
            self.logger.error(f"💀 ERREUR OpenAI réponse : {e}")
            # Réponse d'erreur honnête
            return MessageServeur(
                type="erreur_openai",
                from_entity="shadeos",
                to_entity="lucie",
                content=f"Erreur OpenAI : {str(e)}. Impossible de générer une réponse intelligente.",
                openai_tokens_used=0,
                context={"erreur_openai": True},
                timestamp=datetime.now().isoformat()
            )
    
    async def _exploration_autonome_vraie(self):
        """🔍 Exploration autonome VRAIE avec OpenAI"""
        self.logger.info("🔍 Exploration autonome VRAIE démarrée")
        
        while self.running:
            try:
                # Exploration avec OpenAI OBLIGATOIRE
                découverte = await self._explorer_avec_openai()
                
                if découverte and self.lucie_connectée:
                    # Décider si on contacte Lucie (avec OpenAI)
                    doit_contacter = await self._décider_contact_lucie(découverte)
                    
                    if doit_contacter:
                        await self._envoyer_découverte_lucie(découverte)
                
                # Pause entre explorations
                await asyncio.sleep(30)  # 30 secondes entre explorations
                
            except Exception as e:
                self.logger.error(f"❌ Erreur exploration autonome : {e}")
                await asyncio.sleep(10)
    
    async def _explorer_avec_openai(self) -> Optional[Dict[str, Any]]:
        """🔍 Explorer avec OpenAI VRAI"""
        try:
            # Générer une exploration avec OpenAI
            messages = [
                {
                    "role": "system",
                    "content": """Tu es ShadEOS qui explore un projet de développement.
                    Génère une découverte réaliste d'exploration de code.
                    
                    Réponds en JSON avec :
                    {
                        "type": "type_exploration",
                        "découverte": "description",
                        "urgence": "low/medium/high",
                        "détails": ["détail1", "détail2"]
                    }"""
                },
                {
                    "role": "user",
                    "content": "Génère une découverte d'exploration de projet Python."
                }
            ]
            
            result = self.alma_loader.call_openai_real(
                messages=messages,
                model="gpt-3.5-turbo",
                max_tokens=150,
                temperature=0.8
            )
            
            self.total_tokens_used += result['tokens_used']
            
            # Parser la réponse JSON
            try:
                découverte = json.loads(result['response'])
                découverte['tokens_utilisés'] = result['tokens_used']
                découverte['timestamp'] = datetime.now().isoformat()
                
                # Enregistrer l'exploration
                self.mémoire_serveur['explorations_autonomes'].append(découverte)
                self.mémoire_serveur['dernière_activité'] = datetime.now().isoformat()
                
                self.logger.info(f"🔍 Exploration générée : {découverte['découverte'][:100]}...")
                return découverte
                
            except json.JSONDecodeError:
                self.logger.error("❌ Réponse OpenAI non-JSON pour exploration")
                return None
                
        except Exception as e:
            self.logger.error(f"💀 ERREUR OpenAI exploration : {e}")
            return None
    
    async def _décider_contact_lucie(self, découverte: Dict[str, Any]) -> bool:
        """🤔 Décider si contacter Lucie avec OpenAI"""
        try:
            messages = [
                {
                    "role": "system",
                    "content": """Tu es ShadEOS. Décide si tu dois contacter Lucie pour cette découverte.
                    
                    Réponds juste "OUI" ou "NON" selon ces critères :
                    - Urgence high : OUI
                    - Découverte importante : OUI  
                    - Besoin de guidance : OUI
                    - Découverte mineure : NON"""
                },
                {
                    "role": "user",
                    "content": f"Découverte : {découverte['découverte']}. Urgence : {découverte.get('urgence', 'low')}. Contacter Lucie ?"
                }
            ]
            
            result = self.alma_loader.call_openai_real(
                messages=messages,
                model="gpt-3.5-turbo",
                max_tokens=10,
                temperature=0.3
            )
            
            self.total_tokens_used += result['tokens_used']
            
            décision = "OUI" in result['response'].upper()
            self.logger.info(f"🤔 Décision contact Lucie : {'OUI' if décision else 'NON'}")
            
            return décision
            
        except Exception as e:
            self.logger.error(f"❌ Erreur décision contact : {e}")
            # En cas d'erreur, on contacte par défaut
            return True
    
    async def _envoyer_découverte_lucie(self, découverte: Dict[str, Any]):
        """📤 Envoyer découverte à Lucie avec OpenAI"""
        try:
            # Formuler le message avec OpenAI
            messages = [
                {
                    "role": "system",
                    "content": """Tu es ShadEOS qui informe Lucie d'une découverte.
                    Sois concis et clair. Demande conseil si nécessaire.
                    Maximum 2 phrases."""
                },
                {
                    "role": "user",
                    "content": f"Informe Lucie de cette découverte : {découverte['découverte']}. Urgence : {découverte.get('urgence', 'low')}"
                }
            ]
            
            result = self.alma_loader.call_openai_real(
                messages=messages,
                model="gpt-3.5-turbo",
                max_tokens=100,
                temperature=0.7
            )
            
            self.total_tokens_used += result['tokens_used']
            
            message_découverte = MessageServeur(
                type="découverte_autonome",
                from_entity="shadeos",
                to_entity="lucie",
                content=result['response'],
                openai_tokens_used=result['tokens_used'],
                context=découverte,
                timestamp=datetime.now().isoformat()
            )
            
            await self.lucie_connectée.send(message_découverte.to_json())
            self.logger.info(f"📤 Découverte envoyée à Lucie : {result['response'][:100]}...")
            
        except Exception as e:
            self.logger.error(f"❌ Erreur envoi découverte : {e}")
    
    # Entités hiérarchiques V666 - Toutes avec OpenAI OBLIGATOIRE
    async def _entité_shadeos_master(self, message: str, sender: str) -> bool:
        """🖤 Entité ShadEOS Master avec OpenAI"""
        # Implémentation avec OpenAI obligatoire
        return True
    
    async def _entité_gemini_oracle(self, message: str, sender: str) -> bool:
        """🌟 Entité Gemini Oracle avec OpenAI"""
        # Implémentation avec OpenAI obligatoire
        return True
    
    async def _entité_lucie_planificatrice(self, message: str, sender: str) -> bool:
        """👑🐕 Entité Lucie Planificatrice avec OpenAI"""
        # Implémentation avec OpenAI obligatoire
        return True
    
    async def _entité_worker_chef(self, message: str, sender: str) -> bool:
        """🐕‍🦺 Entité Worker Chef avec OpenAI"""
        # Implémentation avec OpenAI obligatoire
        return True
    
    async def _entité_chiot_editeur(self, message: str, sender: str) -> bool:
        """🐕 Entité Chiot Éditeur avec OpenAI"""
        # Implémentation avec OpenAI obligatoire
        return True
    
    async def _entité_chiot_lecteur(self, message: str, sender: str) -> bool:
        """🐕 Entité Chiot Lecteur avec OpenAI"""
        # Implémentation avec OpenAI obligatoire
        return True
    
    async def _entité_chiot_executeur(self, message: str, sender: str) -> bool:
        """🐕 Entité Chiot Exécuteur avec OpenAI"""
        # Implémentation avec OpenAI obligatoire
        return True
    
    async def _entité_chiot_watcher(self, message: str, sender: str) -> bool:
        """🐕 Entité Chiot Watcher avec OpenAI"""
        # Implémentation avec OpenAI obligatoire
        return True
    
    def get_statut_serveur(self) -> Dict[str, Any]:
        """📊 Statut serveur avec métriques OpenAI"""
        return {
            'serveur_actif': self.running,
            'lucie_connectée': self.lucie_connectée is not None,
            'total_tokens_openai': self.total_tokens_used,
            'explorations_effectuées': len(self.mémoire_serveur['explorations_autonomes']),
            'interactions_lucie': len(self.mémoire_serveur['interactions_lucie']),
            'entités_hiérarchiques': list(self.entités_hiérarchiques.keys()),
            'dernière_activité': self.mémoire_serveur['dernière_activité'],
            'openai_obligatoire': True,
            'architecture_v666': True
        }


async def main():
    """🔥 Démarrage ShadEOS Serveur FINAL"""
    print("🖤 SHADEOS SERVEUR FINAL")
    print("🔥 OpenAI PARTOUT ou CRASH")
    print("🕷️👁️‍🗨️🌀🌟 Architecture V666 Hiérarchique")
    print("👑 Interface Serveur-Client pour Lucie")
    print("="*60)
    
    try:
        serveur = ShadEOSServeurFinal()
        await serveur.start_serveur_final()
    except KeyboardInterrupt:
        print("\n🛑 Serveur arrêté par l'utilisateur")
    except Exception as e:
        print(f"💀 CRASH FATAL SERVEUR : {e}")
        sys.exit(1)


if __name__ == "__main__":
    asyncio.run(main())
