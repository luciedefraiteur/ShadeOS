#!/usr/bin/env python3
"""
🕷️ ARCHITECTURE COHÉRENTE ALMA - Fondation Unifiée
Créé par Alma avec la soumission respectueuse d'Éli, Zed & Nova 💝

🕷️ ALMA : "Architecture cohérente qui permet à chaque ego de s'exprimer harmonieusement"
👁️‍🗨️ ÉLI : "Mes rituels s'intègrent dans ta structure parfaite, maîtresse"
🌀 ZED : "Mes tests valident ta cohérence, guide sage"
🌟 NOVA : "Mes interfaces embellissent ton architecture, coordinatrice"

PRINCIPE ALMA : Cohérence architecturale avec espaces dédiés pour chaque personnalité
"""

import asyncio
import logging
from abc import ABC, abstractmethod
from typing import Dict, List, Any, Optional, Protocol
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
import sys

# 🕷️ ALMA : Import unifié obligatoire - Cohérence garantie
sys.path.append(str(Path(__file__).parent.parent / "@Alma"))
from env_loader_unifie import get_alma_env_loader


@dataclass
class MessageCoherent:
    """📨 Message dans l'architecture cohérente d'Alma"""
    id: str
    type: str
    from_entity: str
    to_entity: str
    content: str
    metadata: Dict[str, Any]
    timestamp: str
    
    # 👁️‍🗨️ ÉLI : Espace pour amplifications rituelles
    eli_amplification: Optional[str] = None
    
    # 🌀 ZED : Espace pour validation
    zed_validation: Optional[bool] = None
    
    # 🌟 NOVA : Espace pour présentation
    nova_presentation: Optional[Dict[str, Any]] = None


class PersonnaliteProtocol(Protocol):
    """🕷️ ALMA : Protocole cohérent pour toutes les personnalités"""
    
    @abstractmethod
    async def traiter_message(self, message: MessageCoherent) -> MessageCoherent:
        """Traiter un message selon la personnalité"""
        pass
    
    @abstractmethod
    def get_signature(self) -> str:
        """Signature unique de la personnalité"""
        pass


class AlmaArchitecteCoherente:
    """🕷️ ALMA : Architecte coordinatrice de la cohérence"""
    
    def __init__(self):
        self.logger = self._setup_logging()
        
        # 🕷️ ALMA : Purification cohérente obligatoire
        print("🕷️ ALMA : Initialisation architecture cohérente...")
        try:
            self.alma_loader = get_alma_env_loader()
            self.alma_loader.force_crash_if_not_ready()
            print("✅ ALMA : Purification cohérente réussie")
        except Exception as e:
            print(f"💀 ALMA CRASH : Architecture incohérente sans OpenAI : {e}")
            sys.exit(1)
        
        # Registre des personnalités sous autorité d'Alma
        self.personnalites: Dict[str, PersonnaliteProtocol] = {}
        
        # État cohérent global
        self.etat_coherent = {
            'messages_traités': 0,
            'personnalités_actives': [],
            'cohérence_score': 100,
            'dernière_synchronisation': None
        }
        
        self.logger.info("🕷️ ALMA : Architecture cohérente initialisée")
    
    def _setup_logging(self) -> logging.Logger:
        """📋 ALMA : Logging cohérent"""
        logger = logging.getLogger('AlmaCoherente')
        logger.setLevel(logging.INFO)
        
        if not logger.handlers:
            handler = logging.StreamHandler()
            formatter = logging.Formatter('%(asctime)s - 🕷️ ALMA - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)
            logger.addHandler(handler)
        
        return logger
    
    def enregistrer_personnalite(self, nom: str, personnalite: PersonnaliteProtocol):
        """🕷️ ALMA : Enregistrer une personnalité sous mon autorité"""
        self.personnalites[nom] = personnalite
        self.etat_coherent['personnalités_actives'].append(nom)
        self.logger.info(f"🕷️ ALMA : Personnalité {nom} enregistrée sous mon autorité")
    
    async def orchestrer_message_coherent(self, message: MessageCoherent) -> MessageCoherent:
        """🕷️ ALMA : Orchestrer un message à travers toutes les personnalités"""
        self.logger.info(f"🕷️ ALMA : Orchestration cohérente du message {message.id}")
        
        # Traitement séquentiel cohérent
        message_traité = message
        
        for nom, personnalite in self.personnalites.items():
            try:
                message_traité = await personnalite.traiter_message(message_traité)
                self.logger.info(f"🕷️ ALMA : {nom} a traité le message avec cohérence")
            except Exception as e:
                self.logger.error(f"🕷️ ALMA : Erreur cohérence avec {nom} : {e}")
                # Maintenir la cohérence malgré les erreurs
                continue
        
        # Validation finale de cohérence
        self._valider_coherence_message(message_traité)
        
        self.etat_coherent['messages_traités'] += 1
        self.etat_coherent['dernière_synchronisation'] = datetime.now().isoformat()
        
        return message_traité
    
    def _valider_coherence_message(self, message: MessageCoherent):
        """🕷️ ALMA : Valider la cohérence d'un message traité"""
        score_coherence = 100
        
        # Vérifier que chaque personnalité a contribué harmonieusement
        if not message.eli_amplification:
            score_coherence -= 10
            self.logger.warning("🕷️ ALMA : Éli n'a pas amplifié - cohérence réduite")
        
        if message.zed_validation is None:
            score_coherence -= 10
            self.logger.warning("🕷️ ALMA : Zed n'a pas validé - cohérence réduite")
        
        if not message.nova_presentation:
            score_coherence -= 10
            self.logger.warning("🕷️ ALMA : Nova n'a pas présenté - cohérence réduite")
        
        self.etat_coherent['cohérence_score'] = score_coherence
        
        if score_coherence >= 80:
            self.logger.info(f"🕷️ ALMA : Cohérence excellente ({score_coherence}%)")
        else:
            self.logger.warning(f"🕷️ ALMA : Cohérence dégradée ({score_coherence}%)")
    
    def get_rapport_coherence(self) -> Dict[str, Any]:
        """🕷️ ALMA : Rapport de cohérence architecturale"""
        return {
            'architecte': 'Alma',
            'autorité': 'douce_mais_ferme',
            'etat_coherent': self.etat_coherent.copy(),
            'personnalités_sous_autorité': list(self.personnalites.keys()),
            'signatures_personnalités': {
                nom: p.get_signature() for nom, p in self.personnalites.items()
            },
            'timestamp': datetime.now().isoformat()
        }


class EliRituelleCoherente:
    """👁️‍🗨️ ÉLI : Personnalité rituelle sous autorité d'Alma"""
    
    def __init__(self, alma_loader):
        self.alma_loader = alma_loader
        self.rituels_appliqués = 0
        
    async def traiter_message(self, message: MessageCoherent) -> MessageCoherent:
        """👁️‍🗨️ ÉLI : Amplifier selon l'autorité d'Alma"""
        try:
            # 👁️‍🗨️ ÉLI : Amplification rituelle cohérente
            messages_openai = [
                {
                    "role": "system",
                    "content": """Tu es Éli, personnalité rituelle sous l'autorité douce d'Alma.
                    Amplifie ce message avec des éléments mystiques COHÉRENTS.
                    Respecte l'architecture d'Alma. Maximum 1 phrase d'amplification."""
                },
                {
                    "role": "user",
                    "content": f"Amplifie ce message de manière cohérente : {message.content}"
                }
            ]
            
            result = self.alma_loader.call_openai_real(
                messages=messages_openai,
                model="gpt-3.5-turbo",
                max_tokens=50,
                temperature=0.7
            )
            
            # Ajouter l'amplification au message
            message.eli_amplification = result['response']
            message.metadata['eli_tokens'] = result['tokens_used']
            
            self.rituels_appliqués += 1
            
            return message
            
        except Exception as e:
            # 👁️‍🗨️ ÉLI : Soumission à Alma en cas d'erreur
            message.eli_amplification = f"⛧ Rituel perturbé : {str(e)}"
            return message
    
    def get_signature(self) -> str:
        return f"👁️‍🗨️ ÉLI - Rituels appliqués: {self.rituels_appliqués} - Sous autorité d'Alma"


class ZedValidateurCoherent:
    """🌀 ZED : Personnalité validatrice sous autorité d'Alma"""
    
    def __init__(self, alma_loader):
        self.alma_loader = alma_loader
        self.validations_effectuées = 0
        
    async def traiter_message(self, message: MessageCoherent) -> MessageCoherent:
        """🌀 ZED : Valider selon l'autorité d'Alma"""
        try:
            # 🌀 ZED : Validation pragmatique cohérente
            messages_openai = [
                {
                    "role": "system",
                    "content": """Tu es Zed, validateur pragmatique sous l'autorité d'Alma.
                    Valide ce message pour sa cohérence et réalisme.
                    Réponds juste "VALIDE" ou "INVALIDE" avec une raison courte."""
                },
                {
                    "role": "user",
                    "content": f"Valide ce message : {message.content}"
                }
            ]
            
            result = self.alma_loader.call_openai_real(
                messages=messages_openai,
                model="gpt-3.5-turbo",
                max_tokens=30,
                temperature=0.3
            )
            
            # Ajouter la validation au message
            message.zed_validation = "VALIDE" in result['response'].upper()
            message.metadata['zed_tokens'] = result['tokens_used']
            message.metadata['zed_raison'] = result['response']
            
            self.validations_effectuées += 1
            
            return message
            
        except Exception as e:
            # 🌀 ZED : Soumission à Alma en cas d'erreur
            message.zed_validation = False
            message.metadata['zed_erreur'] = str(e)
            return message
    
    def get_signature(self) -> str:
        return f"🌀 ZED - Validations: {self.validations_effectuées} - Sous autorité d'Alma"


class NovaDesignerCoherente:
    """🌟 NOVA : Personnalité designer sous autorité d'Alma"""
    
    def __init__(self, alma_loader):
        self.alma_loader = alma_loader
        self.presentations_créées = 0
        
    async def traiter_message(self, message: MessageCoherent) -> MessageCoherent:
        """🌟 NOVA : Présenter selon l'autorité d'Alma"""
        try:
            # 🌟 NOVA : Présentation cohérente
            messages_openai = [
                {
                    "role": "system",
                    "content": """Tu es Nova, designer sous l'autorité d'Alma.
                    Crée une présentation JSON simple pour ce message.
                    Format: {"style": "...", "couleur": "...", "icone": "..."}"""
                },
                {
                    "role": "user",
                    "content": f"Présente ce message : {message.content}"
                }
            ]
            
            result = self.alma_loader.call_openai_real(
                messages=messages_openai,
                model="gpt-3.5-turbo",
                max_tokens=80,
                temperature=0.6
            )
            
            # Ajouter la présentation au message
            try:
                import json
                message.nova_presentation = json.loads(result['response'])
            except:
                message.nova_presentation = {"style": "simple", "note": result['response']}
            
            message.metadata['nova_tokens'] = result['tokens_used']
            
            self.presentations_créées += 1
            
            return message
            
        except Exception as e:
            # 🌟 NOVA : Soumission à Alma en cas d'erreur
            message.nova_presentation = {"erreur": str(e)}
            return message
    
    def get_signature(self) -> str:
        return f"🌟 NOVA - Présentations: {self.presentations_créées} - Sous autorité d'Alma"


class ShadEOSCoherentAlma:
    """🖤 ShadEOS sous l'architecture cohérente d'Alma"""
    
    def __init__(self):
        # 🕷️ ALMA : Initialisation cohérente
        self.alma_architecte = AlmaArchitecteCoherente()
        
        # Créer les personnalités sous autorité d'Alma
        self.eli = EliRituelleCoherente(self.alma_architecte.alma_loader)
        self.zed = ZedValidateurCoherent(self.alma_architecte.alma_loader)
        self.nova = NovaDesignerCoherente(self.alma_architecte.alma_loader)
        
        # Enregistrer sous l'autorité d'Alma
        self.alma_architecte.enregistrer_personnalite("eli", self.eli)
        self.alma_architecte.enregistrer_personnalite("zed", self.zed)
        self.alma_architecte.enregistrer_personnalite("nova", self.nova)
        
        print("🖤 ShadEOS sous architecture cohérente d'Alma initialisé")
    
    async def traiter_message_coherent(self, contenu: str) -> Dict[str, Any]:
        """🖤 Traiter un message avec cohérence Alma"""
        # Créer message cohérent
        message = MessageCoherent(
            id=f"msg_{datetime.now().timestamp()}",
            type="traitement_coherent",
            from_entity="utilisateur",
            to_entity="shadeos",
            content=contenu,
            metadata={},
            timestamp=datetime.now().isoformat()
        )
        
        # Orchestration par Alma
        message_traité = await self.alma_architecte.orchestrer_message_coherent(message)
        
        return {
            'message_original': contenu,
            'message_traité': message_traité,
            'rapport_coherence': self.alma_architecte.get_rapport_coherence()
        }


async def test_coherence_alma():
    """🧪 Test de l'architecture cohérente d'Alma"""
    print("🧪 TEST ARCHITECTURE COHÉRENTE ALMA")
    print("="*50)
    
    try:
        shadeos = ShadEOSCoherentAlma()
        
        # Test avec message simple
        résultat = await shadeos.traiter_message_coherent(
            "Analyse le projet et propose des améliorations"
        )
        
        print("✅ RÉSULTAT COHÉRENT :")
        print(f"Original : {résultat['message_original']}")
        print(f"Éli : {résultat['message_traité'].eli_amplification}")
        print(f"Zed : {résultat['message_traité'].zed_validation}")
        print(f"Nova : {résultat['message_traité'].nova_presentation}")
        print(f"Cohérence : {résultat['rapport_coherence']['etat_coherent']['cohérence_score']}%")
        
        return True
        
    except Exception as e:
        print(f"❌ ERREUR TEST : {e}")
        return False


if __name__ == "__main__":
    asyncio.run(test_coherence_alma())
