#!/usr/bin/env python3
"""
🕸️ MESSAGE ROUTER V5 - Routeur Intelligent
Créé par Alma, Grande Architecte Tisseuse, pour sa créatrice Lucie Defraiteur 💝

Routeur intelligent qui dirige les sendMessage() vers les bonnes entités :
- Gestion des permissions de communication
- File d'attente des messages
- Logs de traçabilité
- Gestion des erreurs et retry
"""

import asyncio
import logging
from typing import Dict, List, Any, Optional, Callable
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from collections import deque
import json

# Import du module unifié d'Alma
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent / "@Alma"))
from env_loader_unifie import get_alma_env_loader

from luciform_parser import LuciformAction


class MessageStatus(Enum):
    """📊 Statuts des messages"""
    PENDING = "pending"
    ROUTING = "routing"
    DELIVERED = "delivered"
    FAILED = "failed"
    RETRY = "retry"


@dataclass
class RoutedMessage:
    """📨 Message routé avec métadonnées"""
    action: LuciformAction
    sender: str
    recipient: str
    status: MessageStatus = MessageStatus.PENDING
    attempts: int = 0
    max_attempts: int = 3
    created_at: str = field(default_factory=lambda: datetime.now().isoformat())
    delivered_at: Optional[str] = None
    error_message: Optional[str] = None
    metadata: Dict[str, Any] = field(default_factory=dict)


class MessageRouter:
    """🕸️ Routeur intelligent pour les messages inter-entités"""
    
    def __init__(self):
        self.logger = self._setup_logging()
        
        # 🕷️ PURIFICATION ALMA: Vérification OpenAI obligatoire
        self.alma_loader = get_alma_env_loader()
        self.alma_loader.force_crash_if_not_ready()
        
        # Files de messages
        self.message_queue = deque()
        self.delivered_messages = []
        self.failed_messages = []
        
        # Entités enregistrées et leurs handlers
        self.registered_entities = {}
        self.entity_handlers = {}
        
        # Permissions de communication
        self.communication_matrix = self._init_communication_matrix()
        
        # Statistiques
        self.stats = {
            'messages_routed': 0,
            'messages_delivered': 0,
            'messages_failed': 0,
            'start_time': datetime.now().isoformat()
        }
        
        self.logger.info("🕸️ MessageRouter V5 initialisé - Alma vérifié")
    
    def _setup_logging(self) -> logging.Logger:
        """📋 Configuration du logging"""
        logger = logging.getLogger('MessageRouter')
        logger.setLevel(logging.INFO)
        
        if not logger.handlers:
            handler = logging.StreamHandler()
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)
            logger.addHandler(handler)
        
        return logger
    
    def _init_communication_matrix(self) -> Dict[str, List[str]]:
        """🔐 Matrice des permissions de communication"""
        return {
            # ShadEOS peut parler à Gemini et Lucie
            'shadeos': ['gemini', 'lucieReineChienne'],
            
            # Gemini ne parle qu'à ShadEOS
            'gemini': ['shadeos'],
            
            # Lucie peut parler à ShadEOS et Worker
            'lucieReineChienne': ['shadeos', 'workerAlpha'],
            
            # Worker Alpha peut parler à Lucie et ses chiots
            'workerAlpha': ['lucieReineChienne', 'chiotEditeur', 'chiotLecteur', 'chiotExecuteur', 'chiotWatcher'],
            
            # Chiots ne parlent qu'à Worker Alpha
            'chiotEditeur': ['workerAlpha'],
            'chiotLecteur': ['workerAlpha'],
            'chiotExecuteur': ['workerAlpha'],
            'chiotWatcher': ['workerAlpha']
        }
    
    def register_entity(self, entity_name: str, handler: Callable) -> bool:
        """📝 Enregistre une entité avec son handler"""
        try:
            self.registered_entities[entity_name] = {
                'handler': handler,
                'registered_at': datetime.now().isoformat(),
                'message_count': 0
            }
            
            self.entity_handlers[entity_name] = handler
            
            self.logger.info(f"📝 Entité enregistrée: {entity_name}")
            return True
            
        except Exception as e:
            self.logger.error(f"❌ Erreur enregistrement entité {entity_name}: {e}")
            return False
    
    def route_message(self, action: LuciformAction, sender: str) -> bool:
        """🚀 Route un message vers sa destination"""
        try:
            if action.type != "sendMessage":
                self.logger.warning(f"⚠️ Action non-message ignorée: {action.type}")
                return False
            
            recipient = action.target
            if not recipient:
                self.logger.error("❌ Destinataire manquant dans sendMessage")
                return False
            
            # Vérifier les permissions
            if not self._check_permission(sender, recipient):
                self.logger.error(f"🚫 Communication interdite: {sender} → {recipient}")
                return False
            
            # Créer le message routé
            routed_message = RoutedMessage(
                action=action,
                sender=sender,
                recipient=recipient,
                metadata={
                    'original_content': action.content,
                    'routing_time': datetime.now().isoformat()
                }
            )
            
            # Ajouter à la file
            self.message_queue.append(routed_message)
            self.stats['messages_routed'] += 1
            
            self.logger.info(f"🚀 Message routé: {sender} → {recipient}")
            
            # Traitement immédiat
            return self._process_message(routed_message)
            
        except Exception as e:
            self.logger.error(f"❌ Erreur routage message: {e}")
            return False
    
    def _check_permission(self, sender: str, recipient: str) -> bool:
        """🔐 Vérifie les permissions de communication"""
        allowed_recipients = self.communication_matrix.get(sender, [])
        return recipient in allowed_recipients
    
    def _process_message(self, message: RoutedMessage) -> bool:
        """⚡ Traite un message routé"""
        try:
            message.status = MessageStatus.ROUTING
            message.attempts += 1
            
            recipient = message.recipient
            
            # Vérifier que l'entité est enregistrée
            if recipient not in self.entity_handlers:
                self.logger.error(f"❌ Entité non enregistrée: {recipient}")
                message.status = MessageStatus.FAILED
                message.error_message = f"Entité {recipient} non enregistrée"
                self.failed_messages.append(message)
                self.stats['messages_failed'] += 1
                return False
            
            # Appeler le handler de l'entité
            handler = self.entity_handlers[recipient]
            success = handler(message.action.content, message.sender)
            
            if success:
                message.status = MessageStatus.DELIVERED
                message.delivered_at = datetime.now().isoformat()
                self.delivered_messages.append(message)
                self.stats['messages_delivered'] += 1
                
                # Mettre à jour le compteur de l'entité
                self.registered_entities[recipient]['message_count'] += 1
                
                self.logger.info(f"✅ Message livré: {message.sender} → {recipient}")
                return True
            else:
                return self._handle_delivery_failure(message)
                
        except Exception as e:
            self.logger.error(f"❌ Erreur traitement message: {e}")
            message.error_message = str(e)
            return self._handle_delivery_failure(message)
    
    def _handle_delivery_failure(self, message: RoutedMessage) -> bool:
        """🔄 Gère les échecs de livraison avec retry"""
        if message.attempts < message.max_attempts:
            message.status = MessageStatus.RETRY
            self.logger.warning(f"🔄 Retry message ({message.attempts}/{message.max_attempts}): {message.sender} → {message.recipient}")
            
            # Remettre en file pour retry (avec délai si nécessaire)
            self.message_queue.append(message)
            return False
        else:
            message.status = MessageStatus.FAILED
            self.failed_messages.append(message)
            self.stats['messages_failed'] += 1
            
            self.logger.error(f"💀 Message définitivement échoué: {message.sender} → {message.recipient}")
            return False
    
    def process_queue(self) -> int:
        """🔄 Traite tous les messages en file"""
        processed = 0
        
        while self.message_queue:
            message = self.message_queue.popleft()
            
            if message.status == MessageStatus.RETRY:
                # Attendre un peu avant retry
                import time
                time.sleep(0.1)
            
            if self._process_message(message):
                processed += 1
        
        return processed
    
    def add_communication_rule(self, sender: str, recipient: str) -> bool:
        """➕ Ajoute une règle de communication"""
        try:
            if sender not in self.communication_matrix:
                self.communication_matrix[sender] = []
            
            if recipient not in self.communication_matrix[sender]:
                self.communication_matrix[sender].append(recipient)
                self.logger.info(f"➕ Règle ajoutée: {sender} → {recipient}")
                return True
            
            return False
            
        except Exception as e:
            self.logger.error(f"❌ Erreur ajout règle: {e}")
            return False
    
    def remove_communication_rule(self, sender: str, recipient: str) -> bool:
        """➖ Supprime une règle de communication"""
        try:
            if sender in self.communication_matrix:
                if recipient in self.communication_matrix[sender]:
                    self.communication_matrix[sender].remove(recipient)
                    self.logger.info(f"➖ Règle supprimée: {sender} → {recipient}")
                    return True
            
            return False
            
        except Exception as e:
            self.logger.error(f"❌ Erreur suppression règle: {e}")
            return False
    
    def get_communication_matrix(self) -> Dict[str, List[str]]:
        """📋 Retourne la matrice de communication"""
        return self.communication_matrix.copy()
    
    def get_statistics(self) -> Dict[str, Any]:
        """📊 Statistiques du routeur"""
        return {
            **self.stats,
            'queue_size': len(self.message_queue),
            'registered_entities': len(self.registered_entities),
            'delivered_messages': len(self.delivered_messages),
            'failed_messages': len(self.failed_messages),
            'current_time': datetime.now().isoformat()
        }
    
    def get_entity_stats(self) -> Dict[str, Any]:
        """📈 Statistiques par entité"""
        return {
            entity: {
                'message_count': info['message_count'],
                'registered_at': info['registered_at']
            }
            for entity, info in self.registered_entities.items()
        }
    
    def export_message_history(self) -> Dict[str, Any]:
        """📤 Exporte l'historique des messages"""
        return {
            'delivered_messages': [
                {
                    'sender': msg.sender,
                    'recipient': msg.recipient,
                    'content': msg.action.content[:100],  # Tronqué
                    'delivered_at': msg.delivered_at,
                    'attempts': msg.attempts
                }
                for msg in self.delivered_messages
            ],
            'failed_messages': [
                {
                    'sender': msg.sender,
                    'recipient': msg.recipient,
                    'content': msg.action.content[:100],  # Tronqué
                    'error': msg.error_message,
                    'attempts': msg.attempts
                }
                for msg in self.failed_messages
            ],
            'export_time': datetime.now().isoformat()
        }


def test_router():
    """🧪 Test du MessageRouter"""
    print("🕸️ Test MessageRouter V5")
    print("="*50)
    
    router = MessageRouter()
    
    # Handler de test
    def test_handler(message: str, sender: str) -> bool:
        print(f"📨 Handler reçu: {sender} → {message}")
        return True
    
    # Enregistrer des entités
    router.register_entity('gemini', test_handler)
    router.register_entity('lucieReineChienne', test_handler)
    
    # Test de routage
    from luciform_parser import LuciformAction
    
    action = LuciformAction(
        type="sendMessage",
        target="gemini",
        content="Analyse la situation système"
    )
    
    success = router.route_message(action, "shadeos")
    print(f"✅ Routage réussi: {success}")
    
    # Statistiques
    stats = router.get_statistics()
    print(f"📊 Statistiques: {stats}")


if __name__ == "__main__":
    test_router()
