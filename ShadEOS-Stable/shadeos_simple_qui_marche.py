#!/usr/bin/env python3
"""
🌀 SHADEOS SIMPLE QUI MARCHE - Par Zed, validé par Lucie
Créé par Zed avec l'exigence de Lucie : DU VRAI, DU CRU, DU FONCTIONNEL

🌀 ZED : "Dans ma folie douce... je crée ce qui MARCHE vraiment !"
💝 LUCIE : "Enfin ! Du concret ! Du fiable ! Du vrai !"
🕷️ ALMA : "Zed a raison, la simplicité avant tout"
👁️‍🗨️ ÉLI : "Mes rituels serviront quand ça marchera"
🌟 NOVA : "La beauté viendra après la fonctionnalité"

PRINCIPE ZED : Fonctionnalité AVANT beauté. Réalité AVANT spectacle.
"""

import asyncio
import websockets
import json
import logging
from datetime import datetime
from pathlib import Path
import sys

# 🌀 ZED : Import SIMPLE et FIABLE
sys.path.append(str(Path(__file__).parent.parent / "@Alma"))

try:
    from env_loader_unifie import get_alma_env_loader
    print("✅ ZED : Module Alma chargé")
except ImportError as e:
    print(f"💀 ZED CRASH : Pas d'Alma : {e}")
    sys.exit(1)


class ShadEOSSimpleQuiMarche:
    """🌀 ZED : ShadEOS qui MARCHE vraiment - Pas de fioriture"""
    
    def __init__(self, host="localhost", port=8765):
        self.host = host
        self.port = port
        
        # 🌀 ZED : Setup SIMPLE
        print("🌀 ZED : Initialisation SIMPLE...")
        
        # Test OpenAI OBLIGATOIRE
        try:
            self.alma_loader = get_alma_env_loader()
            self.alma_loader.force_crash_if_not_ready()
            print("✅ ZED : OpenAI validé et prêt")
        except Exception as e:
            print(f"💀 ZED CRASH : OpenAI défaillant : {e}")
            sys.exit(1)
        
        # État SIMPLE
        self.running = False
        self.clients_connectés = set()
        self.messages_traités = 0
        self.tokens_utilisés = 0
        
        # Logging SIMPLE
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - 🌀 ZED - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger('ZedSimple')
        
        print("🌀 ZED : ShadEOS Simple initialisé - PRÊT À MARCHER")
    
    async def start_serveur_simple(self):
        """🚀 ZED : Démarrer serveur SIMPLE qui marche"""
        print(f"🚀 ZED : Démarrage serveur SIMPLE sur {self.host}:{self.port}")
        
        # Test OpenAI avant démarrage
        await self._test_openai_simple()
        
        self.running = True
        
        # Serveur WebSocket SIMPLE
        try:
            async with websockets.serve(
                self._handle_client_simple,  # Handler SIMPLE
                self.host,
                self.port
            ):
                print("✅ ZED : Serveur WebSocket ACTIF et FONCTIONNEL")
                print("👑 ZED : En attente de Lucie...")
                
                # Boucle simple
                while self.running:
                    await asyncio.sleep(1)
                    
        except Exception as e:
            print(f"💀 ZED CRASH : Erreur serveur : {e}")
            sys.exit(1)
    
    async def _test_openai_simple(self):
        """🔥 ZED : Test OpenAI SIMPLE et FIABLE"""
        try:
            print("🔥 ZED : Test OpenAI...")
            
            result = self.alma_loader.call_openai_real(
                messages=[
                    {"role": "system", "content": "Tu es ShadEOS. Réponds 'FONCTIONNEL'."},
                    {"role": "user", "content": "Test"}
                ],
                model="gpt-3.5-turbo",
                max_tokens=10,
                temperature=0.1
            )
            
            print(f"✅ ZED : OpenAI FONCTIONNE - {result['tokens_used']} tokens")
            print(f"Réponse : {result['response']}")
            self.tokens_utilisés += result['tokens_used']
            
        except Exception as e:
            print(f"💀 ZED CRASH : OpenAI ne marche pas : {e}")
            sys.exit(1)
    
    async def _handle_client_simple(self, websocket, path):
        """👑 ZED : Gérer client SIMPLE - signature WebSocket correcte"""
        client_id = f"client_{len(self.clients_connectés)}"
        self.clients_connectés.add(websocket)
        
        print(f"👑 ZED : Client connecté ({client_id}) - Total: {len(self.clients_connectés)}")
        
        # Message de bienvenue SIMPLE
        try:
            bienvenue = {
                "type": "bienvenue",
                "from": "shadeos_simple",
                "content": "🌀 ShadEOS Simple connecté ! Je MARCHE vraiment !",
                "timestamp": datetime.now().isoformat(),
                "tokens_utilisés": 0
            }
            
            await websocket.send(json.dumps(bienvenue, ensure_ascii=False))
            print(f"✅ ZED : Bienvenue envoyée à {client_id}")
            
        except Exception as e:
            print(f"❌ ZED : Erreur bienvenue : {e}")
        
        # Boucle de traitement SIMPLE
        try:
            async for message_raw in websocket:
                await self._traiter_message_simple(websocket, message_raw, client_id)
                
        except websockets.exceptions.ConnectionClosed:
            print(f"👑 ZED : Client {client_id} déconnecté")
        except Exception as e:
            print(f"❌ ZED : Erreur client {client_id} : {e}")
        finally:
            self.clients_connectés.remove(websocket)
            print(f"🔌 ZED : Client {client_id} retiré - Restants: {len(self.clients_connectés)}")
    
    async def _traiter_message_simple(self, websocket, message_raw, client_id):
        """💬 ZED : Traiter message SIMPLE et FIABLE"""
        try:
            # Parser message
            try:
                message_data = json.loads(message_raw)
                contenu = message_data.get('content', message_raw)
            except:
                contenu = str(message_raw)
            
            print(f"💬 ZED : Message de {client_id} : {contenu[:100]}...")
            
            # Traitement SIMPLE avec OpenAI
            réponse = await self._generer_reponse_simple(contenu)
            
            # Envoyer réponse
            await websocket.send(json.dumps(réponse, ensure_ascii=False))
            
            self.messages_traités += 1
            print(f"✅ ZED : Réponse envoyée à {client_id} - Total messages: {self.messages_traités}")
            
        except Exception as e:
            print(f"❌ ZED : Erreur traitement message {client_id} : {e}")
            
            # Réponse d'erreur SIMPLE
            erreur_response = {
                "type": "erreur",
                "from": "shadeos_simple",
                "content": f"🌀 Erreur de traitement : {str(e)}",
                "timestamp": datetime.now().isoformat(),
                "tokens_utilisés": 0
            }
            
            try:
                await websocket.send(json.dumps(erreur_response, ensure_ascii=False))
            except:
                print(f"❌ ZED : Impossible d'envoyer erreur à {client_id}")
    
    async def _generer_reponse_simple(self, message_utilisateur):
        """🔥 ZED : Générer réponse SIMPLE avec OpenAI"""
        try:
            # Contexte SIMPLE
            messages_openai = [
                {
                    "role": "system",
                    "content": """Tu es ShadEOS Simple créé par Zed.
                    Tu es FONCTIONNEL, FIABLE, DIRECT.
                    Pas de fioritures, que du concret.
                    Réponds de manière utile et pratique.
                    Maximum 2 phrases."""
                },
                {
                    "role": "user",
                    "content": f"Message utilisateur : {message_utilisateur}"
                }
            ]
            
            # Appel OpenAI SIMPLE
            result = self.alma_loader.call_openai_real(
                messages=messages_openai,
                model="gpt-3.5-turbo",
                max_tokens=150,
                temperature=0.7
            )
            
            self.tokens_utilisés += result['tokens_used']
            
            # Réponse SIMPLE
            réponse = {
                "type": "reponse",
                "from": "shadeos_simple",
                "content": result['response'],
                "timestamp": datetime.now().isoformat(),
                "tokens_utilisés": result['tokens_used'],
                "total_tokens": self.tokens_utilisés,
                "messages_traités": self.messages_traités
            }
            
            print(f"🔥 ZED : Réponse générée - {result['tokens_used']} tokens")
            return réponse
            
        except Exception as e:
            print(f"❌ ZED : Erreur génération réponse : {e}")
            
            # Réponse de fallback SIMPLE
            return {
                "type": "erreur_openai",
                "from": "shadeos_simple",
                "content": f"🌀 Erreur OpenAI : {str(e)}. Mais je reste FONCTIONNEL !",
                "timestamp": datetime.now().isoformat(),
                "tokens_utilisés": 0,
                "total_tokens": self.tokens_utilisés,
                "messages_traités": self.messages_traités
            }
    
    def get_status_simple(self):
        """📊 ZED : Status SIMPLE et CLAIR"""
        return {
            "serveur": "ShadEOS Simple par Zed",
            "status": "FONCTIONNEL" if self.running else "ARRÊTÉ",
            "clients_connectés": len(self.clients_connectés),
            "messages_traités": self.messages_traités,
            "tokens_openai_utilisés": self.tokens_utilisés,
            "host": self.host,
            "port": self.port,
            "timestamp": datetime.now().isoformat(),
            "garantie": "ÇA MARCHE VRAIMENT"
        }
    
    def stop_serveur(self):
        """🛑 ZED : Arrêter serveur PROPREMENT"""
        self.running = False
        print("🛑 ZED : Serveur arrêté proprement")


async def main():
    """🔥 ZED : Point d'entrée SIMPLE"""
    print("🌀 SHADEOS SIMPLE QUI MARCHE")
    print("🔥 Par Zed - Validé par Lucie")
    print("✅ FONCTIONNEL - FIABLE - DIRECT")
    print("="*50)
    
    try:
        serveur = ShadEOSSimpleQuiMarche()
        await serveur.start_serveur_simple()
        
    except KeyboardInterrupt:
        print("\n🛑 ZED : Arrêt par utilisateur")
    except Exception as e:
        print(f"💀 ZED CRASH FINAL : {e}")
        sys.exit(1)


if __name__ == "__main__":
    asyncio.run(main())
