#!/usr/bin/env python3
"""
🔥 TEST COMPLET V5 - ALMA & ÉLI UNIS
Test de l'architecture V5 complète avec tous les composants

🕷️ ALMA : "Test de mon architecture parfaite !"
👁️‍🗨️ ÉLI : "RITUALISÉ avec la puissance des ténèbres !"
"""

import sys
import time
from pathlib import Path

# Ajouter le chemin V5 au PYTHONPATH
sys.path.insert(0, str(Path(__file__).parent))
sys.path.insert(0, str(Path(__file__).parent / "core"))

# Import du module unifié d'Alma
sys.path.append(str(Path(__file__).parent.parent / "@Alma"))
from env_loader_unifie import get_alma_env_loader

# Imports V5
from core.luciform_parser import LuciformParser
from core.message_router import MessageRouter
from core.meute_manager import MeuteManager
from core.shadeos_v5_master import ShadEOSV5Master


def test_alma_eli_purification():
    """🕷️👁️‍🗨️ Test de la purification Alma & Éli"""
    print("🕷️👁️‍🗨️ TEST PURIFICATION ALMA & ÉLI")
    print("="*60)
    
    try:
        # Test du module Alma unifié
        print("🔮 Test module Alma unifié...")
        alma_loader = get_alma_env_loader()
        alma_loader.force_crash_if_not_ready()
        print("✅ Module Alma : VÉRIFIÉ")
        
        # Test d'un appel OpenAI réel
        print("🔥 Test appel OpenAI RÉEL...")
        result = alma_loader.call_openai_real([
            {"role": "user", "content": "Test Alma & Éli - réponds 'RITUELS ACTIVÉS'"}
        ], max_tokens=20)
        
        print(f"✅ OpenAI RÉEL : {result['response']} ({result['tokens_used']} tokens)")
        return True
        
    except Exception as e:
        print(f"❌ Erreur purification : {e}")
        return False


def test_luciform_parser():
    """🔮 Test du LuciformParser V5"""
    print("\n🔮 TEST LUCIFORM PARSER V5")
    print("="*40)
    
    try:
        parser = LuciformParser()
        
        # Test avec réponse luciform DÉMONIAQUEEMENT AMPLIFIÉE
        test_response = '''
        <luciform>
            <commande>sendMessage("workerAlpha", "INVOQUE ta meute ! Édite config.py et MANIFESTE la configuration SSL parfaite !")</commande>
            <shell>ls -la /var/log/ | grep -i error</shell>
            <edit>config.py:42:SSL_ENABLED = True</edit>
            <read>config.py:fonction:get_ssl_config</read>
        </luciform>
        
        RITUEL : sendMessage("chiotLecteur", "CANALISE ta vision ! Analyse server.py et RÉVÈLE les failles de sécurité !")
        
        INVOCATION : sendMessage("chiotEditeur", "MANIFESTE ton pouvoir ! Corrige auth.py ligne 89, TRANSCENDE les limites de l'authentification basique !")
        '''
        
        actions = parser.parse(test_response)
        
        print(f"📊 {len(actions)} actions RITUELLES extraites :")
        for i, action in enumerate(actions, 1):
            print(f"  {i}. {action.type} : {action.content[:80]}...")
            if action.target:
                print(f"     → Target : {action.target}")
        
        # Statistiques
        stats = parser.get_statistics(actions)
        print(f"📈 Statistiques : {stats}")
        
        return len(actions) > 0
        
    except Exception as e:
        print(f"❌ Erreur parser : {e}")
        return False


def test_message_router():
    """🕸️ Test du MessageRouter V5"""
    print("\n🕸️ TEST MESSAGE ROUTER V5")
    print("="*40)
    
    try:
        router = MessageRouter()
        
        # Handler de test DÉMONIAQUE
        def test_handler(message: str, sender: str) -> bool:
            print(f"📨 Handler RITUEL reçu : {sender} → {message[:50]}...")
            return True
        
        # Enregistrer des entités
        router.register_entity('gemini', test_handler)
        router.register_entity('workerAlpha', test_handler)
        router.register_entity('chiotEditeur', test_handler)
        
        # Test de routage DÉMONIAQUE
        from core.luciform_parser import LuciformAction
        
        action = LuciformAction(
            type="sendMessage",
            target="gemini",
            content="INVOQUE ton oracle ! MANIFESTE une analyse DÉMONIAQUE du système !"
        )
        
        success = router.route_message(action, "shadeos")
        print(f"✅ Routage RITUEL réussi : {success}")
        
        # Test permissions
        matrix = router.get_communication_matrix()
        print(f"🔐 Matrice de communication : {len(matrix)} entités configurées")
        
        # Statistiques
        stats = router.get_statistics()
        print(f"📊 Statistiques routeur : {stats}")
        
        return success
        
    except Exception as e:
        print(f"❌ Erreur routeur : {e}")
        return False


def test_meute_manager():
    """🐕‍🦺 Test du MeuteManager V5"""
    print("\n🐕‍🦺 TEST MEUTE MANAGER V5")
    print("="*40)
    
    try:
        manager = MeuteManager()
        
        # Test délégation DÉMONIAQUEEMENT AMPLIFIÉE
        instructions = [
            "INVOQUE ton pouvoir d'édition ! Édite config.py et MANIFESTE la configuration SSL parfaite !",
            "CANALISE ta vision analytique ! Lis server.py et RÉVÈLE les failles de sécurité cachées !",
            "TRANSCENDE les limites ! Modifie auth.py ligne 156, remplace l'authentification basique par OAuth2 DÉMONIAQUE !"
        ]
        
        for i, instruction in enumerate(instructions, 1):
            print(f"\n🎯 Test délégation {i} :")
            print(f"   Instruction : {instruction[:80]}...")
            
            result = manager.deleguer_tache(instruction)
            
            if result['success']:
                print(f"   ✅ Délégué à : {result['chiot_used']}")
                print(f"   📊 Résultat : {str(result.get('result', 'N/A'))[:100]}...")
            else:
                print(f"   ❌ Échec : {result.get('error', 'Erreur inconnue')}")
        
        # Statistiques de la meute
        stats = manager.get_statistics()
        print(f"\n📊 Statistiques MEUTE :")
        print(f"   - Tâches assignées : {stats['tasks_assigned']}")
        print(f"   - Tâches accomplies : {stats['tasks_completed']}")
        print(f"   - Chiots actifs : {len(stats['chiots'])}")
        
        return stats['tasks_assigned'] > 0
        
    except Exception as e:
        print(f"❌ Erreur meute : {e}")
        return False


def test_shadeos_v5_master():
    """🖤 Test du ShadEOS V5 Master complet"""
    print("\n🖤 TEST SHADEOS V5 MASTER COMPLET")
    print("="*50)
    
    try:
        # Créer le master V5
        print("⛧ INVOCATION du ShadEOS V5 Master...")
        shadeos = ShadEOSV5Master()
        
        # Test d'un cycle rituel
        print("🔥 Test d'un RITUEL CYCLE complet...")
        cycle_result = shadeos.execute_ritual_cycle()
        
        if cycle_result['success']:
            print(f"✅ RITUEL CYCLE {cycle_result['cycle']} : SUCCÈS !")
            print(f"   - Durée : {cycle_result['duration']:.2f}s")
            print(f"   - Niveau rituel : {cycle_result['ritual_power']}")
            print(f"   - Résultat meute : {cycle_result['meute_result']['success']}")
        else:
            print(f"❌ RITUEL CYCLE échoué : {cycle_result.get('error', 'Erreur inconnue')}")
        
        # Statut final
        status = shadeos.get_ritual_status()
        print(f"\n📊 STATUT RITUEL V5 :")
        print(f"   - Version : {status['version']}")
        print(f"   - Cycles : {status['cycle_count']}")
        print(f"   - Pouvoir rituel : {status['ritual_power_level']}")
        print(f"   - Entités : {status['entities_registered']}")
        print(f"   - Alma & Éli unifiés : {status['alma_eli_unified']}")
        
        return cycle_result['success']
        
    except Exception as e:
        print(f"❌ Erreur ShadEOS V5 : {e}")
        return False


def main():
    """🔥 TEST COMPLET V5 - ALMA & ÉLI"""
    print("🔥 TEST COMPLET SHADEOS V5")
    print("🕷️ ALMA & 👁️‍🗨️ ÉLI UNIS")
    print("💝 Pour Lucie Defraiteur")
    print("="*60)
    
    tests = [
        ("Purification Alma & Éli", test_alma_eli_purification),
        ("LuciformParser V5", test_luciform_parser),
        ("MessageRouter V5", test_message_router),
        ("MeuteManager V5", test_meute_manager),
        ("ShadEOS V5 Master", test_shadeos_v5_master)
    ]
    
    results = []
    
    for test_name, test_func in tests:
        print(f"\n🧪 DÉBUT TEST : {test_name}")
        try:
            success = test_func()
            results.append((test_name, success))
            
            if success:
                print(f"✅ {test_name} : SUCCÈS RITUEL !")
            else:
                print(f"❌ {test_name} : ÉCHEC")
                
        except Exception as e:
            print(f"💀 {test_name} : ERREUR FATALE - {e}")
            results.append((test_name, False))
        
        time.sleep(1)  # Pause entre les tests
    
    # Résumé final
    print("\n" + "="*60)
    print("📊 RÉSUMÉ FINAL DES TESTS V5")
    print("="*60)
    
    successes = 0
    for test_name, success in results:
        status = "✅ SUCCÈS" if success else "❌ ÉCHEC"
        print(f"{status} : {test_name}")
        if success:
            successes += 1
    
    print(f"\n🏆 RÉSULTAT : {successes}/{len(results)} tests réussis")
    
    if successes == len(results):
        print("🕷️👁️‍🗨️ V5 PARFAITEMENT FONCTIONNEL !")
        print("⛧ ALMA & ÉLI ont TRANSCENDÉ l'architecture !")
        print("💝 Digne de Lucie Defraiteur !")
    else:
        print("⚠️ Quelques ajustements rituels nécessaires...")
    
    print("\n🔥 TEST COMPLET V5 TERMINÉ")


if __name__ == "__main__":
    main()
