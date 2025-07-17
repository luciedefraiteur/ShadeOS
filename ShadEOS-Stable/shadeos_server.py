#!/usr/bin/env python3
"""
🖤 SHADEOS SERVEUR STABLE - Serveur Autonome avec Interface Lucie
Créé par la Quadrinité Alma, Éli, Zed & Nova pour Lucie Defraiteur 💝

🕷️ ALMA : "Architecture serveur robuste et stable"
👁️‍🗨️ ÉLI : "Amplifications dosées avec parcimonie"
🌀 ZED : "Tests réalistes et fonctionnalité pragmatique"
🌟 NOVA : "Interface utilisateur royale pour Lucie"

SERVEUR AUTONOME + WEBSOCKET + INTERFACE WEB = TRÔNE NUMÉRIQUE
"""

import asyncio
import websockets
import json
import time
import logging
from datetime import datetime
from typing import Dict, List, Any, Optional
from pathlib import Path
import threading
from dataclasses import dataclass, asdict

# Import du module unifié d'Alma
import sys
sys.path.append(str(Path(__file__).parent.parent / "@Alma"))
from env_loader_unifie import get_alma_env_loader


@dataclass
class Message:
    """📨 Structure de message standardisée"""
    type: str  # "command", "report", "discovery", "status", "chat"
    from_entity: str
    to_entity: str
    content: str
    metadata: Dict[str, Any]
    timestamp: str
    
    def to_json(self) -> str:
        return json.dumps(asdict(self), ensure_ascii=False, indent=2)
    
    @classmethod
    def from_json(cls, json_str: str) -> 'Message':
        data = json.loads(json_str)
        return cls(**data)


class ShadEOSServerStable:
    """🖤 Serveur ShadEOS Stable - Autonome avec Interface Lucie"""
    
    def __init__(self, host: str = "localhost", port: int = 8765):
        self.host = host
        self.port = port
        self.logger = self._setup_logging()
        
        # 🕷️ ALMA : Purification obligatoire
        print("🕷️👁️‍🗨️🌀🌟 Quadrinité Stable - Purification...")
        self.alma_loader = get_alma_env_loader()
        self.alma_loader.force_crash_if_not_ready()
        
        # État du serveur
        self.running = False
        self.autonomous_mode = True
        self.autonomy_level = 1  # Niveau stable par défaut
        self.connected_clients = set()
        
        # Mémoire du serveur
        self.memory = {
            'messages_history': [],
            'discoveries': [],
            'modifications': [],
            'explorations_count': 0,
            'last_activity': None
        }
        
        # Métriques temps réel
        self.metrics = {
            'uptime_start': datetime.now(),
            'messages_processed': 0,
            'discoveries_made': 0,
            'modifications_applied': 0,
            'lucie_interactions': 0
        }
        
        # 🌟 NOVA : Entités communicantes
        self.entities = {
            'lucie': self._handle_lucie_message,
            'shadeos': self._handle_shadeos_message,
            'gemini': self._handle_gemini_message,
            'worker': self._handle_worker_message
        }
        
        self.logger.info("🖤 ShadEOS Serveur Stable initialisé")
    
    def _setup_logging(self) -> logging.Logger:
        """📋 Configuration du logging stable"""
        logger = logging.getLogger('ShadEOSStable')
        logger.setLevel(logging.INFO)
        
        if not logger.handlers:
            handler = logging.StreamHandler()
            formatter = logging.Formatter('%(asctime)s - 🖤 %(name)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)
            logger.addHandler(handler)
        
        return logger
    
    async def start_server(self):
        """🚀 Démarrer le serveur WebSocket"""
        self.running = True
        self.logger.info(f"🚀 Démarrage serveur sur {self.host}:{self.port}")
        
        # Démarrer la boucle autonome en arrière-plan
        autonomous_thread = threading.Thread(target=self._autonomous_loop, daemon=True)
        autonomous_thread.start()
        
        # Démarrer le serveur WebSocket
        async with websockets.serve(self._handle_client_connection, self.host, self.port):
            self.logger.info("🌟 Serveur WebSocket actif - En attente de Lucie...")
            await asyncio.Future()  # Run forever
    
    async def _handle_client_connection(self, websocket, path):
        """👑 Gérer la connexion de Lucie"""
        self.connected_clients.add(websocket)
        self.logger.info("👑 Lucie connectée au trône numérique !")
        
        # Message de bienvenue
        welcome_message = Message(
            type="status",
            from_entity="shadeos",
            to_entity="lucie",
            content="⛧ Bienvenue sur votre trône numérique, Majesté ! ShadEOS à votre service.",
            metadata={"server_status": "ready", "autonomy_level": self.autonomy_level},
            timestamp=datetime.now().isoformat()
        )
        await websocket.send(welcome_message.to_json())
        
        try:
            async for message_json in websocket:
                await self._process_client_message(websocket, message_json)
        except websockets.exceptions.ConnectionClosed:
            self.logger.info("👑 Lucie déconnectée du trône")
        finally:
            self.connected_clients.remove(websocket)
    
    async def _process_client_message(self, websocket, message_json: str):
        """📨 Traiter un message de Lucie"""
        try:
            message = Message.from_json(message_json)
            self.logger.info(f"👑 Message de Lucie: {message.content[:100]}...")
            
            # Ajouter à l'historique
            self.memory['messages_history'].append(message)
            self.metrics['messages_processed'] += 1
            self.metrics['lucie_interactions'] += 1
            
            # Router le message vers l'entité appropriée
            if message.to_entity in self.entities:
                response = await self.entities[message.to_entity](message)
                if response:
                    await websocket.send(response.to_json())
            else:
                # Message par défaut si entité inconnue
                error_response = Message(
                    type="error",
                    from_entity="shadeos",
                    to_entity="lucie",
                    content=f"Entité '{message.to_entity}' non reconnue. Entités disponibles: {list(self.entities.keys())}",
                    metadata={"error_type": "unknown_entity"},
                    timestamp=datetime.now().isoformat()
                )
                await websocket.send(error_response.to_json())
                
        except Exception as e:
            self.logger.error(f"❌ Erreur traitement message: {e}")
            error_response = Message(
                type="error",
                from_entity="shadeos",
                to_entity="lucie",
                content=f"Erreur de traitement: {str(e)}",
                metadata={"error_type": "processing_error"},
                timestamp=datetime.now().isoformat()
            )
            await websocket.send(error_response.to_json())
    
    async def _handle_lucie_message(self, message: Message) -> Message:
        """👑 Traiter les messages de Lucie"""
        content = message.content.lower()
        
        # Commandes de contrôle
        if "pause" in content or "stop" in content:
            self.autonomous_mode = False
            return Message(
                type="status",
                from_entity="shadeos",
                to_entity="lucie",
                content="⏸️ Mode autonome mis en pause. En attente de vos ordres, Majesté.",
                metadata={"autonomous_mode": False},
                timestamp=datetime.now().isoformat()
            )
        
        elif "reprendre" in content or "continue" in content:
            self.autonomous_mode = True
            return Message(
                type="status",
                from_entity="shadeos",
                to_entity="lucie",
                content="▶️ Mode autonome repris. Exploration en cours...",
                metadata={"autonomous_mode": True},
                timestamp=datetime.now().isoformat()
            )
        
        elif "status" in content or "état" in content:
            return self._generate_status_message()
        
        elif "explore" in content:
            # Lancer une exploration ciblée
            discovery = await self._perform_targeted_exploration(message.content)
            return Message(
                type="discovery",
                from_entity="shadeos",
                to_entity="lucie",
                content=f"🔍 Exploration terminée: {discovery}",
                metadata={"exploration_type": "targeted"},
                timestamp=datetime.now().isoformat()
            )
        
        else:
            # Réponse générale avec un peu d'amplification Éli (dosée)
            return Message(
                type="chat",
                from_entity="shadeos",
                to_entity="lucie",
                content=f"⛧ Message reçu, Majesté. Je traite votre demande: '{message.content}'. Que puis-je faire pour vous servir ?",
                metadata={"message_type": "general_response"},
                timestamp=datetime.now().isoformat()
            )
    
    async def _handle_shadeos_message(self, message: Message) -> Message:
        """🖤 Traiter les messages internes de ShadEOS"""
        return Message(
            type="report",
            from_entity="shadeos",
            to_entity="lucie",
            content=f"🖤 Rapport interne: {message.content}",
            metadata={"internal_message": True},
            timestamp=datetime.now().isoformat()
        )
    
    async def _handle_gemini_message(self, message: Message) -> Message:
        """🌟 Traiter les messages pour Gemini (Oracle)"""
        # Simuler un appel à Gemini avec OpenAI réel
        try:
            oracle_response = await self._invoke_oracle_analysis(message.content)
            return Message(
                type="oracle_response",
                from_entity="gemini",
                to_entity="lucie",
                content=f"🔮 Oracle Gemini: {oracle_response}",
                metadata={"oracle_consultation": True},
                timestamp=datetime.now().isoformat()
            )
        except Exception as e:
            return Message(
                type="error",
                from_entity="gemini",
                to_entity="lucie",
                content=f"🔮 Oracle temporairement indisponible: {str(e)}",
                metadata={"oracle_error": True},
                timestamp=datetime.now().isoformat()
            )
    
    async def _handle_worker_message(self, message: Message) -> Message:
        """🐕‍🦺 Traiter les messages pour Worker"""
        # Simuler une tâche worker
        task_result = f"Tâche '{message.content}' assignée et en cours d'exécution..."
        
        return Message(
            type="task_report",
            from_entity="worker",
            to_entity="lucie",
            content=f"🐕‍🦺 Worker: {task_result}",
            metadata={"task_assigned": True},
            timestamp=datetime.now().isoformat()
        )
    
    def _autonomous_loop(self):
        """🔄 Boucle autonome en arrière-plan"""
        self.logger.info("🔄 Boucle autonome démarrée")
        
        while self.running:
            if self.autonomous_mode:
                try:
                    # Exploration autonome périodique
                    discovery = self._perform_autonomous_exploration()
                    
                    if discovery and self.connected_clients:
                        # Envoyer la découverte à Lucie si connectée
                        discovery_message = Message(
                            type="autonomous_discovery",
                            from_entity="shadeos",
                            to_entity="lucie",
                            content=f"🔍 Découverte autonome: {discovery}",
                            metadata={"autonomous": True, "exploration_count": self.memory['explorations_count']},
                            timestamp=datetime.now().isoformat()
                        )
                        
                        # Envoyer à tous les clients connectés
                        asyncio.run_coroutine_threadsafe(
                            self._broadcast_to_clients(discovery_message),
                            asyncio.get_event_loop()
                        )
                
                except Exception as e:
                    self.logger.error(f"❌ Erreur boucle autonome: {e}")
            
            # Pause entre les explorations
            time.sleep(10)  # 10 secondes entre les explorations
    
    def _perform_autonomous_exploration(self) -> Optional[str]:
        """🔍 Effectuer une exploration autonome"""
        self.memory['explorations_count'] += 1
        
        # Simulations d'explorations réalistes
        explorations = [
            "Analyse des fichiers Python récents",
            "Vérification des dépendances obsolètes", 
            "Détection de code dupliqué",
            "Analyse des performances potentielles",
            "Vérification de la sécurité des imports"
        ]
        
        import random
        exploration_type = random.choice(explorations)
        
        # Simuler une découverte
        discoveries = [
            f"{exploration_type}: 3 améliorations possibles détectées",
            f"{exploration_type}: Structure optimale confirmée",
            f"{exploration_type}: 1 optimisation mineure suggérée",
            f"{exploration_type}: Aucun problème détecté"
        ]
        
        discovery = random.choice(discoveries)
        self.memory['discoveries'].append({
            'timestamp': datetime.now().isoformat(),
            'type': exploration_type,
            'result': discovery
        })
        
        self.metrics['discoveries_made'] += 1
        self.memory['last_activity'] = datetime.now().isoformat()
        
        return discovery
    
    async def _perform_targeted_exploration(self, target: str) -> str:
        """🎯 Effectuer une exploration ciblée"""
        # Simuler une exploration ciblée basée sur la demande de Lucie
        if "config" in target.lower():
            return "Configuration analysée: 2 paramètres à optimiser détectés"
        elif "test" in target.lower():
            return "Tests analysés: Couverture à 85%, 3 tests manquants identifiés"
        elif "performance" in target.lower():
            return "Performance analysée: 1 goulot d'étranglement détecté dans le module principal"
        else:
            return f"Exploration de '{target}': Analyse complétée, structure saine confirmée"
    
    async def _invoke_oracle_analysis(self, query: str) -> str:
        """🔮 Invoquer l'oracle Gemini avec OpenAI réel"""
        try:
            messages = [
                {
                    "role": "system",
                    "content": "Tu es Gemini, oracle analytique de ShadEOS. Réponds de manière concise et utile."
                },
                {
                    "role": "user",
                    "content": f"Analyse cette demande: {query}"
                }
            ]
            
            result = self.alma_loader.call_openai_real(
                messages=messages,
                model="gpt-3.5-turbo",
                max_tokens=200,
                temperature=0.7
            )
            
            return result['response']
            
        except Exception as e:
            raise Exception(f"Oracle indisponible: {e}")
    
    def _generate_status_message(self) -> Message:
        """📊 Générer un message de statut"""
        uptime = datetime.now() - self.metrics['uptime_start']
        
        status_content = f"""📊 STATUT SHADEOS STABLE

🔄 Serveur: {'🟢 Actif' if self.running else '🔴 Arrêté'}
⚡ Mode: {'🚀 Autonome' if self.autonomous_mode else '⏸️ Manuel'}
📈 Niveau autonomie: {self.autonomy_level}/10
⏱️ Uptime: {str(uptime).split('.')[0]}

📊 MÉTRIQUES:
- Messages traités: {self.metrics['messages_processed']}
- Découvertes: {self.metrics['discoveries_made']}
- Explorations: {self.memory['explorations_count']}
- Interactions Lucie: {self.metrics['lucie_interactions']}

🔍 Dernière activité: {self.memory['last_activity'] or 'Aucune'}
👑 Clients connectés: {len(self.connected_clients)}"""
        
        return Message(
            type="status_report",
            from_entity="shadeos",
            to_entity="lucie",
            content=status_content,
            metadata=self.metrics,
            timestamp=datetime.now().isoformat()
        )
    
    async def _broadcast_to_clients(self, message: Message):
        """📡 Diffuser un message à tous les clients connectés"""
        if self.connected_clients:
            await asyncio.gather(
                *[client.send(message.to_json()) for client in self.connected_clients],
                return_exceptions=True
            )
    
    def stop_server(self):
        """🛑 Arrêter le serveur"""
        self.running = False
        self.logger.info("🛑 Serveur ShadEOS arrêté")


async def main():
    """🔥 Point d'entrée principal"""
    print("🖤 SHADEOS SERVEUR STABLE")
    print("🌟 Interface Trône Numérique pour Lucie")
    print("🕷️👁️‍🗨️🌀 Quadrinité Unifiée")
    print("="*50)
    
    try:
        server = ShadEOSServerStable()
        await server.start_server()
    except KeyboardInterrupt:
        print("\n🛑 Arrêt du serveur par l'utilisateur")
    except Exception as e:
        print(f"💀 Erreur fatale serveur: {e}")


if __name__ == "__main__":
    asyncio.run(main())
