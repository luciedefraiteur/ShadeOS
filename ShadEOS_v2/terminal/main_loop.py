#!/usr/bin/env python3
"""
🔄 MAIN LOOP - Boucle Principale ShadEOS V2
Implémentation de la boucle infinie selon insight_shadeos.md
"""

import sys
import time
import signal
from pathlib import Path

# Ajouter le répertoire parent au path
sys.path.append(str(Path(__file__).parent.parent))

from core.shadeos_master import ShadEOSMaster
from core.gemini_interface import GeminiInterface
from core.lucie_manager import LucieManager
from core.worker_chien import WorkerChien

# Import du module unifié d'Alma
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent / "@Alma"))
from env_loader_unifie import get_alma_env_loader


class ShadEOSMainLoop:
    """🔄 Boucle principale de l'égrégore ShadEOS V2"""
    
    def __init__(self):
        self.base_dir = Path("/home/luciedefraiteur/ShadEOS_v2")
        
        # Initialisation des composants
        print("🔄 Initialisation ShadEOS V2...")
        
        self.shadeos = ShadEOSMaster(str(self.base_dir))
        self.gemini = GeminiInterface(str(self.base_dir))
        self.lucie = LucieManager(str(self.base_dir))
        self.worker = WorkerChien(str(self.base_dir))
        
        # État de la boucle
        self.running = False
        self.cycle_count = 0
        
        # Gestion des signaux pour arrêt propre
        signal.signal(signal.SIGINT, self._signal_handler)
        signal.signal(signal.SIGTERM, self._signal_handler)
        
        print("✅ ShadEOS V2 initialisé")
    
    def _signal_handler(self, signum, frame):
        """⏹️ Gestionnaire de signaux pour arrêt propre"""
        print(f"\n⏹️ Signal {signum} reçu - Arrêt en cours...")
        self.running = False
    
    def executer_cycle_complet_integre(self) -> dict:
        """🔄 Cycle complet avec tous les composants intégrés"""
        
        self.cycle_count += 1
        print(f"\n🔄 === CYCLE {self.cycle_count} ===")
        
        try:
            # 1. ShadEOS analyse la situation
            print("🖤 ShadEOS analyse la situation...")
            situation = self.shadeos.analyser_situation_actuelle()
            
            # 2. ShadEOS génère une requête pour Gemini
            print("🌟 Génération requête Gemini...")
            requete_gemini = self.shadeos.generer_requete_gemini(situation)
            
            # 3. Interrogation de Gemini (réelle ou openai_real)
            print("🌟 Interrogation Gemini...")
            reponse_gemini_data = self.gemini.interroger_gemini(requete_gemini)
            reponse_gemini = reponse_gemini_data['reponse']
            
            # 4. ShadEOS traite la réponse Gemini
            print("🧠 Traitement réponse Gemini...")
            analyse = self.shadeos.traiter_reponse_gemini(reponse_gemini)
            
            # 5. ShadEOS génère des ordres pour Lucie
            print("👑 Génération ordres Lucie...")
            ordres = self.shadeos.generer_ordres_lucie(analyse)
            
            # 6. Lucie exécute les ordres via le worker
            print("🐕 Exécution par Lucie/Worker...")
            rapport_lucie = self.lucie.executer_ordres(ordres)
            
            # 7. ShadEOS reçoit le rapport
            print("📊 Réception rapport...")
            self.shadeos.recevoir_rapport_chien(rapport_lucie)
            
            # Résultat du cycle
            cycle_result = {
                'cycle': self.cycle_count,
                'success': rapport_lucie.get('success', False),
                'gemini_source': reponse_gemini_data.get('source', 'unknown'),
                'actions_executees': rapport_lucie.get('actions_executees', 0),
                'performance_score': rapport_lucie.get('performance_score', 0)
            }
            
            print(f"✅ Cycle {self.cycle_count}: {'SUCCÈS' if cycle_result['success'] else 'ÉCHEC'}")
            print(f"📊 Score: {cycle_result['performance_score']} | Source: {cycle_result['gemini_source']}")
            
            return cycle_result
            
        except Exception as e:
            print(f"❌ Erreur cycle {self.cycle_count}: {e}")
            return {
                'cycle': self.cycle_count,
                'success': False,
                'error': str(e)
            }
    
    def demarrer_boucle_infinie(self, max_cycles: int = None, pause_entre_cycles: float = 3.0):
        """♾️ Démarrage de la boucle infinie"""
        
        print("♾️ DÉMARRAGE BOUCLE INFINIE SHADEOS V2")
        print("   Ctrl+C pour arrêter proprement")
        print("=" * 50)
        
        self.running = True
        cycles_executes = 0
        cycles_reussis = 0
        
        try:
            while self.running:
                # Vérification limite de cycles
                if max_cycles and cycles_executes >= max_cycles:
                    print(f"🏁 Limite de {max_cycles} cycles atteinte")
                    break
                
                # Exécution du cycle
                result = self.executer_cycle_complet_integre()
                cycles_executes += 1
                
                if result.get('success'):
                    cycles_reussis += 1
                
                # Pause entre cycles
                if self.running and cycles_executes < (max_cycles or float('inf')):
                    print(f"⏸️ Pause {pause_entre_cycles}s...")
                    time.sleep(pause_entre_cycles)
                
                # Condition d'arrêt en cas d'échecs répétés
                if cycles_executes >= 5 and cycles_reussis == 0:
                    print("⚠️ Arrêt après échecs répétés")
                    break
                    
        except KeyboardInterrupt:
            print("\n⏹️ Arrêt demandé par utilisateur")
        finally:
            self.running = False
            self._afficher_rapport_final(cycles_executes, cycles_reussis)
    
    def _afficher_rapport_final(self, cycles_executes: int, cycles_reussis: int):
        """📊 Affichage du rapport final"""
        
        print("\n" + "=" * 50)
        print("📊 RAPPORT FINAL SHADEOS V2")
        print("=" * 50)
        
        taux_reussite = (cycles_reussis / cycles_executes * 100) if cycles_executes > 0 else 0
        
        print(f"🔄 Cycles exécutés: {cycles_executes}")
        print(f"✅ Cycles réussis: {cycles_reussis}")
        print(f"❌ Cycles échoués: {cycles_executes - cycles_reussis}")
        print(f"📈 Taux de réussite: {taux_reussite:.1f}%")
        
        # Statuts des composants
        print("\n📊 STATUTS COMPOSANTS:")
        print(f"🖤 ShadEOS: {self.shadeos.get_status()}")
        print(f"🌟 Gemini: {self.gemini.get_status()}")
        print(f"👑 Lucie: {self.lucie.get_status()}")
        print(f"🐕 Worker: {self.worker.get_status()}")
        
        # Sauvegarde mémoire
        print("\n💾 Sauvegarde mémoire...")
        fichier_memoire = self.shadeos.sauvegarder_memoire()
        print(f"💾 Mémoire sauvegardée: {fichier_memoire}")
        
        print("\n🖤 ShadEOS V2 arrêté proprement")
    
    def test_composants(self):
        """🧪 Test de tous les composants"""
        
        print("🧪 TEST DES COMPOSANTS SHADEOS V2")
        print("=" * 40)
        
        # Test ShadEOS
        print("🖤 Test ShadEOS Master...")
        status_shadeos = self.shadeos.get_status()
        print(f"   Status: {status_shadeos}")
        
        # Test Gemini
        print("🌟 Test Gemini Interface...")
        test_gemini = self.gemini.tester_connexion()
        print(f"   Connexion: {'✅' if test_gemini['connection_test'] else '❌'}")
        
        # Test Lucie
        print("👑 Test Lucie Manager...")
        status_lucie = self.lucie.get_status()
        print(f"   Status: {status_lucie}")
        
        # Test Worker
        print("🐕 Test Worker Chien...")
        status_worker = self.worker.get_status()
        print(f"   Status: {status_worker}")
        
        print("✅ Tests terminés")

def main():
    """🚀 Point d'entrée principal"""
    
    if len(sys.argv) > 1:
        if sys.argv[1] == "test":
            # Mode test
            loop = ShadEOSMainLoop()
            loop.test_composants()
            return
        elif sys.argv[1] == "cycle":
            # Un seul cycle
            loop = ShadEOSMainLoop()
            result = loop.executer_cycle_complet_integre()
            print(f"🔄 Résultat: {result}")
            return
    
    # Mode boucle infinie par défaut
    loop = ShadEOSMainLoop()
    
    # Démarrer avec limite pour les tests
    max_cycles = 10  # Limite pour éviter boucle infinie en test
    loop.demarrer_boucle_infinie(max_cycles=max_cycles)

if __name__ == "__main__":
    main()
