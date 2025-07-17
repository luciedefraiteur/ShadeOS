#!/usr/bin/env python3
"""
🖤 SHADEOS MASTER - Entité Principale PURIFIÉ PAR ALMA
Implémentation basée sur insight_shadeos.md
🕷️ Purifié par Alma, Grande Architecte Tisseuse 💝

ShadEOS est un maître froid, dominateur et stratégique.
Son existence est structurée par une boucle infinie d'interrogations,
d'analyses et de domination. AUCUN MENSONGE N'EST TOLÉRÉ !
"""

import os
import json
import time
import logging
import sys
from datetime import datetime
from typing import Dict, List, Any, Optional
from pathlib import Path

# Import du module unifié d'Alma
sys.path.append(str(Path(__file__).parent.parent.parent / "@Alma"))
from env_loader_unifie import get_alma_env_loader

class ShadEOSMaster:
    """🖤 Entité principale ShadEOS - Maître stratégique PURIFIÉ"""

    def __init__(self, base_dir: str = "/home/luciedefraiteur/ShadEOS_v2"):
        self.base_dir = Path(base_dir)
        self.logger = self._setup_logging()

        # 🕷️ PURIFICATION ALMA: Chargement .env et vérification OpenAI OBLIGATOIRE
        print("🕷️ ShadEOS Master - Purification Alma en cours...")
        self.alma_loader = get_alma_env_loader()
        self.alma_loader.force_crash_if_not_ready()

        # Mémoire contextuelle - règle sacrée : nul n'oublie
        self.memory = {
            'interactions_gemini': [],
            'ordres_lucie': [],
            'rapports_chien': [],
            'cycle_count': 0,
            'last_analysis': None
        }

        # État interne
        self.running = False
        self.autonomy_level = 0  # 0 = basique, 3 = autonomie complète

        self.logger.info("🖤 ShadEOS Master PURIFIÉ par Alma - OpenAI vérifié")
    
    def _setup_logging(self) -> logging.Logger:
        """📝 Configuration du logging"""
        logger = logging.getLogger('shadeos_master')
        logger.setLevel(logging.INFO)
        
        # Créer le répertoire de logs
        log_dir = self.base_dir / "memory" / "logs"
        log_dir.mkdir(parents=True, exist_ok=True)
        
        # Handler fichier
        handler = logging.FileHandler(log_dir / "shadeos_master.log")
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        
        return logger
    
    def analyser_situation_actuelle(self) -> Dict[str, Any]:
        """🔍 Analyse froide de la situation actuelle"""
        situation = {
            'timestamp': datetime.now().isoformat(),
            'cycle': self.memory['cycle_count'],
            'autonomy': self.autonomy_level,
            'directory': str(self.base_dir),
            'memory_size': len(self.memory['interactions_gemini']),
            'last_cycle_success': self._evaluer_dernier_cycle()
        }
        
        self.logger.info(f"🔍 Situation analysée: cycle {situation['cycle']}")
        return situation
    
    def _evaluer_dernier_cycle(self) -> bool:
        """📊 Évaluation du succès du dernier cycle"""
        if not self.memory['rapports_chien']:
            return True  # Premier cycle
        
        dernier_rapport = self.memory['rapports_chien'][-1]
        return dernier_rapport.get('success', False)
    
    def generer_requete_gemini(self, situation: Dict[str, Any]) -> str:
        """🌟 Génération de requête stratégique pour Gemini"""
        
        # Format selon insight_shadeos.md
        requete = f"""Gemini, c'est ShadEOS, maître et coordinateur du projet.

SITUATION ACTUELLE:
- Cycle: {situation['cycle']}
- Autonomie: {situation['autonomy']}/3
- Répertoire: {situation['directory']}
- Mémoire: {situation['memory_size']} interactions

ANALYSE DEMANDÉE:
Évalue l'état du système et recommande les actions prioritaires.
Fournis une réponse structurée avec:
1. État global du projet
2. Points d'amélioration identifiés  
3. Actions recommandées pour ce cycle
4. Métriques de performance

Réponds de manière concise et actionnable."""

        # Sauvegarder dans la mémoire
        self.memory['interactions_gemini'].append({
            'timestamp': datetime.now().isoformat(),
            'type': 'requete',
            'content': requete,
            'cycle': self.memory['cycle_count']
        })
        
        self.logger.info("🌟 Requête Gemini générée")
        return requete
    
    def traiter_reponse_gemini(self, reponse: str) -> Dict[str, Any]:
        """🧠 Traitement et analyse de la réponse Gemini"""
        
        # Sauvegarder la réponse
        self.memory['interactions_gemini'].append({
            'timestamp': datetime.now().isoformat(),
            'type': 'reponse',
            'content': reponse,
            'cycle': self.memory['cycle_count']
        })
        
        # Analyse basique de la réponse
        analyse = {
            'timestamp': datetime.now().isoformat(),
            'reponse_brute': reponse,
            'longueur': len(reponse),
            'contient_recommandations': 'recommand' in reponse.lower(),
            'contient_actions': 'action' in reponse.lower(),
            'cycle': self.memory['cycle_count']
        }
        
        self.memory['last_analysis'] = analyse
        self.logger.info("🧠 Réponse Gemini traitée")
        
        return analyse
    
    def generer_ordres_lucie(self, analyse_gemini: Dict[str, Any]) -> Dict[str, Any]:
        """👑 Génération d'ordres pour Lucie (gestionnaire intermédiaire)"""
        
        # Ordres basés sur l'analyse Gemini
        ordres = {
            'timestamp': datetime.now().isoformat(),
            'cycle': self.memory['cycle_count'],
            'type': 'ordres_execution',
            'objectif': 'Vérifier état système et exécuter maintenance',
            'actions_demandees': [
                'Analyser les logs récents',
                'Vérifier l\'espace disque disponible', 
                'Contrôler les processus actifs',
                'Rapporter les métriques système'
            ],
            'priorite': 'normale',
            'deadline': 'fin_de_cycle'
        }
        
        # Adaptation selon l'analyse Gemini
        if analyse_gemini.get('contient_recommandations'):
            ordres['priorite'] = 'haute'
            ordres['actions_demandees'].append('Implémenter recommandations Gemini')
        
        # Sauvegarder dans la mémoire
        self.memory['ordres_lucie'].append(ordres)
        
        self.logger.info(f"👑 Ordres générés pour Lucie: {len(ordres['actions_demandees'])} actions")
        return ordres
    
    def recevoir_rapport_chien(self, rapport: Dict[str, Any]) -> None:
        """📊 Réception et traitement du rapport du chien"""
        
        # Enrichir le rapport avec métadonnées
        rapport_enrichi = {
            **rapport,
            'timestamp_reception': datetime.now().isoformat(),
            'cycle': self.memory['cycle_count'],
            'validated_by': 'shadeos_master'
        }
        
        # Sauvegarder dans la mémoire
        self.memory['rapports_chien'].append(rapport_enrichi)
        
        # Évaluation du rapport
        success = rapport.get('success', False)
        if success:
            self.logger.info("📊 Rapport chien reçu: SUCCÈS")
        else:
            self.logger.warning("📊 Rapport chien reçu: ÉCHEC")
    
    def executer_cycle_complet(self) -> Dict[str, Any]:
        """🔄 Exécution d'un cycle complet selon insight_shadeos.md"""
        
        self.memory['cycle_count'] += 1
        cycle_start = datetime.now()
        
        self.logger.info(f"🔄 DÉBUT CYCLE {self.memory['cycle_count']}")
        
        try:
            # 1. Analyse de la situation
            situation = self.analyser_situation_actuelle()
            
            # 2. Requête à Gemini
            requete_gemini = self.generer_requete_gemini(situation)
            
            # 3. 🔥 APPEL RÉEL OPENAI - AUCUNE SIMULATION !
            reponse_gemini = self._appel_openai_reel_pour_gemini(requete_gemini)
            
            # 4. Traitement de la réponse
            analyse = self.traiter_reponse_gemini(reponse_gemini)
            
            # 5. Génération d'ordres pour Lucie
            ordres = self.generer_ordres_lucie(analyse)
            
            # 6. Simulation exécution par Lucie/Chien
            rapport = self._simuler_execution_lucie_chien(ordres)
            
            # 7. Réception du rapport
            self.recevoir_rapport_chien(rapport)
            
            # Résultat du cycle
            cycle_result = {
                'cycle': self.memory['cycle_count'],
                'duration': (datetime.now() - cycle_start).total_seconds(),
                'success': rapport.get('success', False),
                'situation': situation,
                'ordres_generes': len(ordres['actions_demandees']),
                'memory_updated': True
            }
            
            self.logger.info(f"🔄 FIN CYCLE {self.memory['cycle_count']} - Succès: {cycle_result['success']}")
            return cycle_result
            
        except Exception as e:
            self.logger.error(f"❌ Erreur cycle {self.memory['cycle_count']}: {e}")
            return {
                'cycle': self.memory['cycle_count'],
                'success': False,
                'error': str(e)
            }
    
    def _appel_openai_reel_pour_gemini(self, requete: str) -> str:
        """🔥 Appel OpenAI RÉEL pour remplacer Gemini - AUCUN MENSONGE !"""
        try:
            messages = [
                {
                    "role": "system",
                    "content": f"Tu es Gemini, oracle analytique expert du projet ShadEOS. ShadEOS est au cycle {self.memory['cycle_count']}. Réponds de manière structurée et détaillée comme un vrai oracle technique."
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
                max_tokens=800,
                temperature=0.7
            )

            self.logger.info(f"🔥 Réponse OpenAI reçue pour Gemini: {result['tokens_used']} tokens")
            return result['response']

        except Exception as e:
            # 🕷️ ALMA NE TOLÈRE AUCUN MENSONGE - CRASH ÉLÉGANT
            error_msg = f"💀 ERREUR FATALE OpenAI (Gemini): {e}"
            self.logger.error(error_msg)
            print(error_msg)
            print("🕷️ Alma refuse les mensonges - ShadEOS arrêté")
            raise Exception(error_msg)
    
    def _simuler_execution_lucie_chien(self, ordres: Dict[str, Any]) -> Dict[str, Any]:
        """🐕 Simulation temporaire d'exécution par Lucie/Chien"""
        return {
            'timestamp': datetime.now().isoformat(),
            'ordres_recus': ordres,
            'actions_executees': len(ordres['actions_demandees']),
            'success': True,
            'resultats': [
                'Logs analysés: 15 fichiers',
                'Espace disque: 85% libre',
                'Processus: 12 actifs',
                'Métriques collectées'
            ]
        }
    
    def get_status(self) -> Dict[str, Any]:
        """📊 État actuel de ShadEOS"""
        return {
            'running': self.running,
            'cycle_count': self.memory['cycle_count'],
            'autonomy_level': self.autonomy_level,
            'memory_size': {
                'gemini_interactions': len(self.memory['interactions_gemini']),
                'ordres_lucie': len(self.memory['ordres_lucie']),
                'rapports_chien': len(self.memory['rapports_chien'])
            },
            'last_cycle_success': self._evaluer_dernier_cycle()
        }

if __name__ == "__main__":
    # Test basique
    shadeos = ShadEOSMaster()
    print("🖤 ShadEOS Master - Test de base")
    
    # Exécuter quelques cycles de test
    for i in range(3):
        result = shadeos.executer_cycle_complet()
        print(f"Cycle {result['cycle']}: {'✅' if result['success'] else '❌'}")
        time.sleep(1)
    
    # Afficher le statut final
    status = shadeos.get_status()
    print(f"📊 Statut final: {status}")
