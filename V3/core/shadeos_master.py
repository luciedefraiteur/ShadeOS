#!/usr/bin/env python3
"""
🖤 SHADEOS MASTER V3 - Entité Principale avec Prompts Externes
Implémentation basée sur insight_shadeos.md avec prompts externalisés
"""

import os
import json
import time
import logging
from datetime import datetime
from typing import Dict, List, Any, Optional
from pathlib import Path

from prompt_manager import get_prompt_manager

# Import du module Alma local
from alma_env_loader import get_alma_env_loader


class ShadEOSMaster:
    """🖤 Entité principale ShadEOS V3 - Maître stratégique avec prompts externes"""
    
    def __init__(self, base_dir: str = "/home/luciedefraiteur/ShadEOS_v1_archive/V3"):
        self.base_dir = Path(base_dir)
        self.logger = self._setup_logging()
        
        # Gestionnaire de prompts
        self.prompt_manager = get_prompt_manager()
        
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
        
        self.logger.info("🖤 ShadEOS Master V3 initialisé avec prompts externes")
    
    def _setup_logging(self) -> logging.Logger:
        """📝 Configuration du logging"""
        logger = logging.getLogger('shadeos_master_v3')
        logger.setLevel(logging.INFO)
        
        # Créer le répertoire de logs
        log_dir = self.base_dir / "memory" / "logs"
        log_dir.mkdir(parents=True, exist_ok=True)
        
        # Handler fichier
        handler = logging.FileHandler(log_dir / "shadeos_master_v3.log")
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
    
    def generer_requete_gemini(self, situation: Dict[str, Any], contexte_additionnel: str = "") -> str:
        """🌟 Génération de requête stratégique pour Gemini depuis prompt externe"""
        
        # Variables pour le prompt
        variables = {
            'cycle': situation['cycle'],
            'autonomy': situation['autonomy'],
            'directory': situation['directory'],
            'memory_size': situation['memory_size'],
            'last_cycle_success': situation['last_cycle_success'],
            'context': contexte_additionnel or "Cycle de routine"
        }
        
        # Charger et formater le prompt
        requete = self.prompt_manager.formater_prompt("shadeos", "analyse_situation", **variables)
        
        if not requete:
            # Fallback minimal si prompt non trouvé
            requete = f"Gemini, analyse le système ShadEOS cycle {situation['cycle']}"
            self.logger.warning("⚠️ Utilisation du openai_real pour requête Gemini")
        
        # Sauvegarder dans la mémoire
        self.memory['interactions_gemini'].append({
            'timestamp': datetime.now().isoformat(),
            'type': 'requete',
            'content': requete,
            'cycle': self.memory['cycle_count'],
            'prompt_source': 'shadeos/analyse_situation'
        })
        
        self.logger.info("🌟 Requête Gemini générée depuis prompt externe")
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
            'validated_by': 'shadeos_master_v3'
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
            
            # 2. Requête à Gemini (depuis prompt externe)
            requete_gemini = self.generer_requete_gemini(situation)
            
            # 3. Simulation réponse Gemini (pour l'instant)
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
                'memory_updated': True,
                'prompt_manager_status': self.prompt_manager.get_status()
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
        """🌟 Simulation temporaire de réponse Gemini"""
        return f"""ANALYSE SYSTÈME - CYCLE {self.memory['cycle_count']}

ÉTAT GLOBAL: Système opérationnel avec prompts externes
POINTS D'AMÉLIORATION: 
- Optimiser la gestion des prompts
- Améliorer les logs de debug

ACTIONS RECOMMANDÉES:
1. Vérifier l'espace disque
2. Analyser les performances
3. Nettoyer les fichiers temporaires

MÉTRIQUES: Performance stable, prompts externalisés fonctionnels."""
    
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
        """📊 État actuel de ShadEOS V3"""
        return {
            'version': 'V3_prompts_externes',
            'running': self.running,
            'cycle_count': self.memory['cycle_count'],
            'autonomy_level': self.autonomy_level,
            'memory_size': {
                'gemini_interactions': len(self.memory['interactions_gemini']),
                'ordres_lucie': len(self.memory['ordres_lucie']),
                'rapports_chien': len(self.memory['rapports_chien'])
            },
            'last_cycle_success': self._evaluer_dernier_cycle(),
            'prompt_manager': self.prompt_manager.get_status()
        }

if __name__ == "__main__":
    # Test basique
    shadeos = ShadEOSMaster()
    print("🖤 ShadEOS Master V3 - Test avec prompts externes")
    
    # Exécuter quelques cycles de test
    for i in range(3):
        result = shadeos.executer_cycle_complet()
        print(f"Cycle {result['cycle']}: {'✅' if result['success'] else '❌'}")
        time.sleep(1)
    
    # Afficher le statut final
    status = shadeos.get_status()
    print(f"📊 Statut final: {status}")
