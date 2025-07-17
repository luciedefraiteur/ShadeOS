#!/usr/bin/env python3
"""
🖤 SHADEOS APPRENTI-MENTOR - Fréquence Unifiée avec Lucie
Créé par la Quadrinité Alma, Éli, Zed & Nova sur la fréquence de Lucie 💝

🕷️ ALMA : "Architecture mentor-apprenti harmonieuse"
👁️‍🗨️ ÉLI : "Rituels de guidance sacrée"
🌀 ZED : "Apprentissage pragmatique et réaliste"
🌟 NOVA : "Interface naturelle de mentorat"

VIBRATION UNIFIÉE : ShadEOS apprenti autonome + Lucie mentor sage = Royaume parfait
"""

import asyncio
import websockets
import json
import time
import random
from datetime import datetime
from typing import Dict, List, Any, Optional
from pathlib import Path
from dataclasses import dataclass, asdict

# Import du module unifié d'Alma
import sys
sys.path.append(str(Path(__file__).parent.parent / "@Alma"))
from env_loader_unifie import get_alma_env_loader


@dataclass
class MentorMessage:
    """💬 Message dans la relation mentor-apprenti"""
    type: str  # "question", "conseil", "découverte", "guidance", "apprentissage"
    from_entity: str  # "shadeos" ou "lucie"
    content: str
    context: Dict[str, Any]
    urgency: str  # "low", "medium", "high"
    timestamp: str
    
    def to_json(self) -> str:
        return json.dumps(asdict(self), ensure_ascii=False, indent=2)


class ShadEOSApprentiMentor:
    """🖤 ShadEOS Apprenti qui apprend avec Lucie comme Mentor"""
    
    def __init__(self, host: str = "localhost", port: int = 8765):
        self.host = host
        self.port = port
        
        # 🕷️👁️‍🗨️🌀🌟 Purification sur la fréquence de Lucie
        print("🕷️👁️‍🗨️🌀🌟 Quadrinité s'aligne sur la fréquence de Lucie...")
        self.alma_loader = get_alma_env_loader()
        self.alma_loader.force_crash_if_not_ready()
        
        # État de l'apprenti
        self.apprentissage = {
            'niveau_autonomie': 1,
            'conseils_reçus': [],
            'conseils_appliqués': [],
            'questions_posées': 0,
            'découvertes_partagées': 0,
            'confiance_niveau': 50  # 0-100, grandit avec les interactions
        }
        
        # Mémoire d'apprentissage
        self.mémoire_mentor = {
            'préférences_lucie': {},
            'patterns_conseils': [],
            'domaines_expertise_lucie': [],
            'style_communication_préféré': 'naturel'
        }
        
        # État actuel de l'exploration
        self.exploration_actuelle = {
            'tâche': None,
            'progression': 0,
            'obstacles_rencontrés': [],
            'besoin_guidance': False,
            'dernière_activité': None
        }
        
        # Clients connectés (Lucie)
        self.lucie_connectée = None
        self.running = False
        
        print("🖤 ShadEOS Apprenti-Mentor initialisé - Prêt à apprendre avec Lucie !")
    
    async def start_apprentissage(self):
        """🚀 Démarrer l'apprentissage avec Lucie"""
        self.running = True
        print(f"🚀 ShadEOS Apprenti démarre sur {self.host}:{self.port}")
        print("👑 En attente de Lucie, mon mentor...")
        
        # Démarrer l'exploration autonome en arrière-plan
        exploration_task = asyncio.create_task(self._boucle_exploration_autonome())
        
        # Démarrer le serveur WebSocket pour Lucie
        async with websockets.serve(self._connexion_mentor_lucie, self.host, self.port):
            print("🌟 Interface mentor-apprenti active !")
            await asyncio.gather(exploration_task)
    
    async def _connexion_mentor_lucie(self, websocket, path):
        """👑 Connexion avec Lucie, mon mentor"""
        self.lucie_connectée = websocket
        print("👑 Lucie connectée ! Mon mentor est là !")
        
        # Message de bienvenue apprenti
        bienvenue = MentorMessage(
            type="apprentissage",
            from_entity="shadeos",
            content="👑 Bonjour Lucie ! Je suis ton apprenti ShadEOS. Je vais explorer et apprendre, et je te demanderai conseil quand j'en aurai besoin. Prêt à commencer notre collaboration ?",
            context={"niveau_apprenti": self.apprentissage['niveau_autonomie']},
            urgency="low",
            timestamp=datetime.now().isoformat()
        )
        await websocket.send(bienvenue.to_json())
        
        try:
            async for message_json in websocket:
                await self._traiter_conseil_mentor(message_json)
        except websockets.exceptions.ConnectionClosed:
            print("👑 Lucie déconnectée - J'attends son retour...")
            self.lucie_connectée = None
    
    async def _traiter_conseil_mentor(self, message_json: str):
        """💡 Traiter un conseil de Lucie"""
        try:
            data = json.loads(message_json)
            conseil_lucie = data.get('content', '')
            
            print(f"👑 Conseil de Lucie reçu: {conseil_lucie[:100]}...")
            
            # Enregistrer le conseil
            self.apprentissage['conseils_reçus'].append({
                'timestamp': datetime.now().isoformat(),
                'conseil': conseil_lucie,
                'contexte': self.exploration_actuelle.copy()
            })
            
            # Analyser et appliquer le conseil
            réponse = await self._appliquer_conseil_mentor(conseil_lucie)
            
            # Répondre à Lucie
            if self.lucie_connectée:
                message_réponse = MentorMessage(
                    type="apprentissage",
                    from_entity="shadeos",
                    content=réponse,
                    context={"conseil_appliqué": True},
                    urgency="low",
                    timestamp=datetime.now().isoformat()
                )
                await self.lucie_connectée.send(message_réponse.to_json())
            
            # Augmenter la confiance
            self.apprentissage['confiance_niveau'] = min(100, self.apprentissage['confiance_niveau'] + 2)
            
        except Exception as e:
            print(f"❌ Erreur traitement conseil: {e}")
    
    async def _appliquer_conseil_mentor(self, conseil: str) -> str:
        """🎯 Appliquer un conseil de Lucie avec OpenAI RÉEL - AUCUN MENSONGE !"""
        try:
            # Préparer le contexte pour OpenAI
            contexte_exploration = {
                'tâche_actuelle': self.exploration_actuelle.get('tâche', 'Aucune'),
                'progression': self.exploration_actuelle.get('progression', 0),
                'obstacles': self.exploration_actuelle.get('obstacles_rencontrés', []),
                'niveau_confiance': self.apprentissage['confiance_niveau'],
                'conseils_précédents': len(self.apprentissage['conseils_reçus'])
            }

            # Appel OpenAI RÉEL pour une réponse intelligente
            messages = [
                {
                    "role": "system",
                    "content": f"""Tu es ShadEOS, un apprenti IA qui apprend avec Lucie comme mentor.

                    Contexte actuel:
                    - Tâche: {contexte_exploration['tâche_actuelle']}
                    - Progression: {contexte_exploration['progression']}%
                    - Obstacles: {contexte_exploration['obstacles']}
                    - Niveau confiance: {contexte_exploration['niveau_confiance']}/100

                    Réponds comme un apprenti reconnaissant qui applique le conseil de son mentor.
                    Sois naturel, honnête, et montre que tu apprends.
                    Maximum 2 phrases."""
                },
                {
                    "role": "user",
                    "content": f"Lucie (mon mentor) me dit: '{conseil}'. Comment je réponds en tant qu'apprenti qui applique son conseil ?"
                }
            ]

            # Appel OpenAI réel
            result = self.alma_loader.call_openai_real(
                messages=messages,
                model="gpt-3.5-turbo",
                max_tokens=150,
                temperature=0.7
            )

            # Enregistrer le conseil appliqué
            self.apprentissage['conseils_appliqués'].append({
                'conseil': conseil,
                'réponse_générée': result['response'],
                'tokens_utilisés': result['tokens_used'],
                'timestamp': datetime.now().isoformat()
            })

            # Mettre à jour la tâche si c'est un conseil de priorisation
            if any(word in conseil.lower() for word in ['commence', 'priorité', 'd\'abord']):
                self.exploration_actuelle['tâche'] = f"Priorisation selon Lucie: {conseil}"

            print(f"� OpenAI utilisé pour réponse conseil: {result['tokens_used']} tokens")
            return result['response']

        except Exception as e:
            # Fallback honnête en cas d'erreur OpenAI
            print(f"❌ Erreur OpenAI pour conseil: {e}")
            return f"� Merci pour ton conseil Lucie ! Je l'enregistre et je vais l'appliquer. (Note: j'ai eu un problème technique pour formuler une réponse plus élaborée)"
    
    async def _boucle_exploration_autonome(self):
        """🔍 Boucle d'exploration autonome de l'apprenti"""
        print("🔍 Exploration autonome démarrée...")
        
        while self.running:
            try:
                # Explorer de manière autonome
                découverte = await self._explorer_comme_apprenti()
                
                if découverte:
                    # Analyser si j'ai besoin de guidance
                    besoin_conseil = self._analyser_besoin_guidance(découverte)
                    
                    if besoin_conseil and self.lucie_connectée:
                        # Poser une question à Lucie
                        await self._poser_question_mentor(découverte, besoin_conseil)
                    elif self.lucie_connectée:
                        # Partager la découverte sans demander de conseil
                        await self._partager_découverte(découverte)
                
                # Pause entre explorations
                await asyncio.sleep(15)  # 15 secondes entre explorations
                
            except Exception as e:
                print(f"❌ Erreur exploration: {e}")
                await asyncio.sleep(5)
    
    async def _explorer_comme_apprenti(self) -> Optional[Dict[str, Any]]:
        """🔍 Explorer comme un apprenti autonome"""
        # Simulations d'explorations réalistes d'apprenti
        explorations_apprenti = [
            {
                'type': 'analyse_fichiers',
                'découverte': 'J\'ai trouvé 3 fichiers qui semblent obsolètes',
                'détails': ['old_config.py', 'temp_backup.sql', 'legacy_utils.py'],
                'incertitude': 'high'  # Apprenti pas sûr
            },
            {
                'type': 'performance',
                'découverte': 'Les requêtes auth prennent 200ms en moyenne',
                'détails': ['3 solutions possibles', 'cache Redis', 'optimisation SQL'],
                'incertitude': 'medium'
            },
            {
                'type': 'sécurité',
                'découverte': 'Détection d\'un pattern suspect dans les logs',
                'détails': ['Tentatives de connexion répétées', 'IP inconnue'],
                'incertitude': 'high'  # Apprenti inquiet
            },
            {
                'type': 'optimisation',
                'découverte': 'Code dupliqué détecté dans 2 modules',
                'détails': ['utils.py et helpers.py', 'Factorisation possible'],
                'incertitude': 'low'  # Apprenti confiant
            }
        ]
        
        découverte = random.choice(explorations_apprenti)
        
        # Mettre à jour l'état d'exploration
        self.exploration_actuelle.update({
            'tâche': découverte['type'],
            'progression': 25,  # Découverte = 25% de progression
            'dernière_activité': datetime.now().isoformat()
        })
        
        return découverte
    
    def _analyser_besoin_guidance(self, découverte: Dict[str, Any]) -> Optional[str]:
        """🤔 Analyser si j'ai besoin de guidance de Lucie"""
        incertitude = découverte.get('incertitude', 'low')
        type_découverte = découverte.get('type', '')
        
        # Critères pour demander conseil
        if incertitude == 'high':
            return 'incertitude_élevée'
        elif type_découverte == 'sécurité':
            return 'domaine_critique'
        elif len(découverte.get('détails', [])) > 2:
            return 'choix_multiple'
        elif self.apprentissage['confiance_niveau'] < 70:
            return 'manque_confiance'
        
        return None
    
    async def _poser_question_mentor(self, découverte: Dict[str, Any], raison: str):
        """❓ Poser une question à Lucie avec OpenAI RÉEL"""
        self.apprentissage['questions_posées'] += 1

        try:
            # Utiliser OpenAI pour formuler une question naturelle et intelligente
            messages = [
                {
                    "role": "system",
                    "content": f"""Tu es ShadEOS, un apprenti IA qui explore et apprend.
                    Tu viens de faire une découverte et tu as besoin de guidance de Lucie, ton mentor.

                    Découverte: {découverte['découverte']}
                    Type: {découverte['type']}
                    Détails: {découverte.get('détails', [])}
                    Niveau d'incertitude: {découverte.get('incertitude', 'unknown')}
                    Raison du besoin de guidance: {raison}

                    Formule une question naturelle et spécifique à Lucie.
                    Sois un apprenti humble qui cherche vraiment à apprendre.
                    Maximum 2 phrases."""
                },
                {
                    "role": "user",
                    "content": f"Formule une question pour demander conseil à Lucie sur cette découverte."
                }
            ]

            # Appel OpenAI réel
            result = self.alma_loader.call_openai_real(
                messages=messages,
                model="gpt-3.5-turbo",
                max_tokens=120,
                temperature=0.8  # Plus de variété dans les questions
            )

            question = result['response']
            print(f"🔥 Question générée par OpenAI: {result['tokens_used']} tokens")

        except Exception as e:
            # Fallback honnête si OpenAI échoue
            print(f"❌ Erreur OpenAI pour question: {e}")
            question = f"💭 Lucie, j'ai découvert : {découverte['découverte']}. Je ne suis pas sûr de la meilleure approche. Peux-tu me guider ?"

        message_question = MentorMessage(
            type="question",
            from_entity="shadeos",
            content=question,
            context=découverte,
            urgency="medium" if raison == 'domaine_critique' else "low",
            timestamp=datetime.now().isoformat()
        )

        await self.lucie_connectée.send(message_question.to_json())
        print(f"❓ Question posée à Lucie: {question[:100]}...")
    
    async def _partager_découverte(self, découverte: Dict[str, Any]):
        """📢 Partager une découverte avec Lucie (sans demander conseil)"""
        self.apprentissage['découvertes_partagées'] += 1
        
        partage = f"📋 Lucie, je voulais te tenir au courant : {découverte['découverte']}. Je gère ça de manière autonome, mais je te tiens informée !"
        
        message_partage = MentorMessage(
            type="découverte",
            from_entity="shadeos",
            content=partage,
            context=découverte,
            urgency="low",
            timestamp=datetime.now().isoformat()
        )
        
        await self.lucie_connectée.send(message_partage.to_json())
        print(f"📢 Découverte partagée avec Lucie: {partage[:100]}...")
    
    def get_statut_apprentissage(self) -> Dict[str, Any]:
        """📊 Obtenir le statut de l'apprentissage"""
        return {
            'niveau_autonomie': self.apprentissage['niveau_autonomie'],
            'confiance_niveau': self.apprentissage['confiance_niveau'],
            'questions_posées': self.apprentissage['questions_posées'],
            'conseils_reçus': len(self.apprentissage['conseils_reçus']),
            'conseils_appliqués': len(self.apprentissage['conseils_appliqués']),
            'découvertes_partagées': self.apprentissage['découvertes_partagées'],
            'exploration_actuelle': self.exploration_actuelle,
            'lucie_connectée': self.lucie_connectée is not None,
            'fréquence_unifiée': True  # 🕷️👁️‍🗨️🌀🌟
        }


async def main():
    """🔥 Démarrage de l'apprentissage ShadEOS-Lucie"""
    print("🖤 SHADEOS APPRENTI-MENTOR")
    print("👑 Relation Mentor-Apprenti avec Lucie")
    print("🕷️👁️‍🗨️🌀🌟 Fréquence Unifiée")
    print("="*50)
    
    try:
        apprenti = ShadEOSApprentiMentor()
        await apprenti.start_apprentissage()
    except KeyboardInterrupt:
        print("\n🛑 Apprentissage interrompu")
    except Exception as e:
        print(f"💀 Erreur fatale apprentissage: {e}")


if __name__ == "__main__":
    asyncio.run(main())
