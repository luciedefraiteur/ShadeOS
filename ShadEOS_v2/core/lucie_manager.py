#!/usr/bin/env python3
"""
👑 LUCIE MANAGER - Gestionnaire Intermédiaire
Coordonne l'exécution des ordres de ShadEOS via le worker chien
"""

import logging
import json
from datetime import datetime
from typing import Dict, List, Any, Optional
from pathlib import Path

class LucieManager:
    """👑 Gestionnaire intermédiaire - Interface entre ShadEOS et Worker"""
    
    def __init__(self, base_dir: str = "/home/luciedefraiteur/ShadEOS_v2"):
        self.base_dir = Path(base_dir)
        self.logger = self._setup_logging()
        
        # Mémoire des ordres reçus et exécutés
        self.memory = {
            'ordres_recus': [],
            'executions': [],
            'performance_history': []
        }
        
        self.logger.info("👑 Lucie Manager initialisé")
    
    def _setup_logging(self) -> logging.Logger:
        """📝 Configuration du logging"""
        logger = logging.getLogger('lucie_manager')
        logger.setLevel(logging.INFO)
        
        # Créer le répertoire de logs
        log_dir = self.base_dir / "memory" / "logs"
        log_dir.mkdir(parents=True, exist_ok=True)
        
        # Handler fichier
        handler = logging.FileHandler(log_dir / "lucie_manager.log")
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        
        return logger
    
    def recevoir_ordres_shadeos(self, ordres: Dict[str, Any]) -> Dict[str, Any]:
        """📋 Réception et validation des ordres de ShadEOS"""
        
        timestamp = datetime.now().isoformat()
        
        # Validation basique des ordres
        validation = self._valider_ordres(ordres)
        
        if not validation['valide']:
            self.logger.error(f"❌ Ordres invalides: {validation['erreurs']}")
            return {
                'timestamp': timestamp,
                'ordres_acceptes': False,
                'erreurs': validation['erreurs']
            }
        
        # Sauvegarder les ordres
        ordres_enrichis = {
            **ordres,
            'timestamp_reception': timestamp,
            'status': 'recu'
        }
        
        self.memory['ordres_recus'].append(ordres_enrichis)
        
        self.logger.info(f"📋 Ordres reçus de ShadEOS: {len(ordres.get('actions_demandees', []))} actions")
        
        return {
            'timestamp': timestamp,
            'ordres_acceptes': True,
            'actions_count': len(ordres.get('actions_demandees', [])),
            'priorite': ordres.get('priorite', 'normale')
        }
    
    def _valider_ordres(self, ordres: Dict[str, Any]) -> Dict[str, Any]:
        """✅ Validation de la structure des ordres"""
        
        erreurs = []
        
        # Vérifications obligatoires
        if 'actions_demandees' not in ordres:
            erreurs.append("Champ 'actions_demandees' manquant")
        
        if 'objectif' not in ordres:
            erreurs.append("Champ 'objectif' manquant")
        
        if 'cycle' not in ordres:
            erreurs.append("Champ 'cycle' manquant")
        
        # Vérification des actions
        actions = ordres.get('actions_demandees', [])
        if not isinstance(actions, list):
            erreurs.append("'actions_demandees' doit être une liste")
        elif len(actions) == 0:
            erreurs.append("Aucune action demandée")
        
        return {
            'valide': len(erreurs) == 0,
            'erreurs': erreurs
        }
    
    def executer_ordres(self, ordres: Dict[str, Any]) -> Dict[str, Any]:
        """🔄 Exécution des ordres via le worker chien"""
        
        timestamp_start = datetime.now()
        
        # Réception des ordres
        reception = self.recevoir_ordres_shadeos(ordres)
        
        if not reception['ordres_acceptes']:
            return {
                'timestamp': timestamp_start.isoformat(),
                'success': False,
                'erreur': 'Ordres rejetés',
                'details': reception['erreurs']
            }
        
        # Traduction des ordres en tâches pour le worker
        taches_worker = self._traduire_ordres_en_taches(ordres)
        
        # Simulation d'exécution par le worker (pour l'instant)
        resultats_worker = self._simuler_execution_worker(taches_worker)
        
        # Compilation du rapport final
        rapport = self._compiler_rapport_execution(ordres, resultats_worker, timestamp_start)
        
        # Sauvegarder l'exécution
        self.memory['executions'].append(rapport)
        
        # Mettre à jour l'historique de performance
        self._mettre_a_jour_performance(rapport)
        
        self.logger.info(f"🔄 Exécution terminée: {'✅' if rapport['success'] else '❌'}")
        
        return rapport
    
    def _traduire_ordres_en_taches(self, ordres: Dict[str, Any]) -> List[Dict[str, Any]]:
        """🔧 Traduction des ordres en tâches exécutables"""
        
        taches = []
        actions = ordres.get('actions_demandees', [])
        
        for i, action in enumerate(actions):
            tache = {
                'id': f"tache_{i+1}",
                'action': action,
                'type': self._determiner_type_action(action),
                'priorite': ordres.get('priorite', 'normale'),
                'timeout': 30
            }
            taches.append(tache)
        
        self.logger.info(f"🔧 {len(taches)} tâches générées pour le worker")
        return taches
    
    def _determiner_type_action(self, action: str) -> str:
        """🎯 Détermination du type d'action"""
        
        action_lower = action.lower()
        
        if 'log' in action_lower or 'analyser' in action_lower:
            return 'analyse'
        elif 'disque' in action_lower or 'espace' in action_lower:
            return 'system_check'
        elif 'processus' in action_lower:
            return 'process_check'
        elif 'métrique' in action_lower or 'rapport' in action_lower:
            return 'reporting'
        else:
            return 'general'
    
    def _simuler_execution_worker(self, taches: List[Dict[str, Any]]) -> Dict[str, Any]:
        """🐕 Simulation temporaire d'exécution par le worker"""
        
        resultats = {
            'timestamp': datetime.now().isoformat(),
            'taches_executees': len(taches),
            'taches_reussies': len(taches),  # Simulation: toutes réussies
            'taches_echouees': 0,
            'resultats_detailles': []
        }
        
        for tache in taches:
            resultat_tache = {
                'id': tache['id'],
                'action': tache['action'],
                'success': True,
                'output': self._generer_output_simule(tache['type']),
                'duration': 0.5
            }
            resultats['resultats_detailles'].append(resultat_tache)
        
        return resultats
    
    def _generer_output_simule(self, type_action: str) -> str:
        """📊 Génération d'output simulé selon le type d'action"""
        
        outputs = {
            'analyse': 'Logs analysés: 25 fichiers, 3 warnings détectés',
            'system_check': 'Espace disque: 78% libre (45GB disponibles)',
            'process_check': 'Processus actifs: 15 Python, 8 système',
            'reporting': 'Métriques collectées: CPU 12%, RAM 34%, Réseau OK',
            'general': 'Action exécutée avec succès'
        }
        
        return outputs.get(type_action, 'Résultat générique')
    
    def _compiler_rapport_execution(self, ordres: Dict[str, Any], 
                                   resultats_worker: Dict[str, Any], 
                                   timestamp_start: datetime) -> Dict[str, Any]:
        """📊 Compilation du rapport d'exécution final"""
        
        duration = (datetime.now() - timestamp_start).total_seconds()
        
        rapport = {
            'timestamp': timestamp_start.isoformat(),
            'cycle': ordres.get('cycle', 0),
            'objectif': ordres.get('objectif', ''),
            'actions_demandees': len(ordres.get('actions_demandees', [])),
            'actions_executees': resultats_worker['taches_executees'],
            'actions_reussies': resultats_worker['taches_reussies'],
            'success': resultats_worker['taches_echouees'] == 0,
            'duration': duration,
            'resultats': [r['output'] for r in resultats_worker['resultats_detailles']],
            'performance_score': self._calculer_score_performance(resultats_worker)
        }
        
        return rapport
    
    def _calculer_score_performance(self, resultats: Dict[str, Any]) -> float:
        """📈 Calcul du score de performance"""
        
        if resultats['taches_executees'] == 0:
            return 0.0
        
        taux_reussite = resultats['taches_reussies'] / resultats['taches_executees']
        return round(taux_reussite, 2)
    
    def _mettre_a_jour_performance(self, rapport: Dict[str, Any]) -> None:
        """📊 Mise à jour de l'historique de performance"""
        
        performance = {
            'timestamp': rapport['timestamp'],
            'cycle': rapport['cycle'],
            'score': rapport['performance_score'],
            'success': rapport['success'],
            'duration': rapport['duration']
        }
        
        self.memory['performance_history'].append(performance)
        
        # Garder seulement les 50 dernières performances
        if len(self.memory['performance_history']) > 50:
            self.memory['performance_history'] = self.memory['performance_history'][-50:]
    
    def get_status(self) -> Dict[str, Any]:
        """📊 Statut du gestionnaire Lucie"""
        
        # Calcul de la performance moyenne
        if self.memory['performance_history']:
            scores = [p['score'] for p in self.memory['performance_history']]
            performance_moyenne = sum(scores) / len(scores)
        else:
            performance_moyenne = 0.0
        
        return {
            'ordres_recus_total': len(self.memory['ordres_recus']),
            'executions_total': len(self.memory['executions']),
            'performance_moyenne': round(performance_moyenne, 2),
            'derniere_execution': self.memory['executions'][-1]['timestamp'] if self.memory['executions'] else None
        }

if __name__ == "__main__":
    # Test du gestionnaire
    lucie = LucieManager()
    
    print("👑 Test Lucie Manager")
    
    # Test d'ordres
    ordres_test = {
        'cycle': 1,
        'objectif': 'Test du gestionnaire',
        'actions_demandees': [
            'Vérifier l\'état du système',
            'Analyser les logs',
            'Rapporter les métriques'
        ],
        'priorite': 'normale'
    }
    
    # Exécution
    rapport = lucie.executer_ordres(ordres_test)
    print(f"🔄 Rapport: {'✅' if rapport['success'] else '❌'} - Score: {rapport['performance_score']}")
    
    # Statut
    status = lucie.get_status()
    print(f"📊 Statut: {status}")
