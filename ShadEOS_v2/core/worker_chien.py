#!/usr/bin/env python3
"""
🐕 WORKER CHIEN - Exécuteur de Base
Worker simple qui exécute les commandes shell de base
"""

import os
import subprocess
import logging
import json
from datetime import datetime
from typing import Dict, List, Any, Optional
from pathlib import Path

class WorkerChien:
    """🐕 Worker chien - Exécuteur obéissant de commandes"""
    
    def __init__(self, base_dir: str = "/home/luciedefraiteur/ShadEOS_v2"):
        self.base_dir = Path(base_dir)
        self.logger = self._setup_logging()
        
        # Mémoire des tâches exécutées
        self.memory = {
            'taches_executees': [],
            'commandes_history': [],
            'performance_stats': {
                'total_executions': 0,
                'successful_executions': 0,
                'failed_executions': 0
            }
        }
        
        # Commandes autorisées pour la sécurité
        self.commandes_autorisees = {
            'ls', 'pwd', 'ps', 'df', 'free', 'uptime', 'date', 'whoami',
            'cat', 'head', 'tail', 'wc', 'grep', 'find', 'du', 'top'
        }
        
        self.logger.info("🐕 Worker Chien initialisé")
    
    def _setup_logging(self) -> logging.Logger:
        """📝 Configuration du logging"""
        logger = logging.getLogger('worker_chien')
        logger.setLevel(logging.INFO)
        
        # Créer le répertoire de logs
        log_dir = self.base_dir / "memory" / "logs"
        log_dir.mkdir(parents=True, exist_ok=True)
        
        # Handler fichier
        handler = logging.FileHandler(log_dir / "worker_chien.log")
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        
        return logger
    
    def executer_tache(self, tache: Dict[str, Any]) -> Dict[str, Any]:
        """🔄 Exécution d'une tâche individuelle"""
        
        timestamp_start = datetime.now()
        
        # Traduction de la tâche en commandes
        commandes = self._traduire_tache_en_commandes(tache)
        
        # Validation sécurité
        commandes_validees = self._valider_commandes_securite(commandes)
        
        if not commandes_validees:
            return {
                'tache_id': tache.get('id', 'unknown'),
                'success': False,
                'error': 'Aucune commande valide après validation sécurité',
                'timestamp': timestamp_start.isoformat(),
                'duration': 0
            }
        
        # Exécution des commandes
        resultats_commandes = []
        success_global = True
        
        for commande in commandes_validees:
            resultat = self._executer_commande(commande)
            resultats_commandes.append(resultat)
            
            if not resultat['success']:
                success_global = False
        
        # Compilation du résultat
        duration = (datetime.now() - timestamp_start).total_seconds()
        
        resultat_tache = {
            'tache_id': tache.get('id', 'unknown'),
            'action': tache.get('action', ''),
            'success': success_global,
            'timestamp': timestamp_start.isoformat(),
            'duration': duration,
            'commandes_executees': len(commandes_validees),
            'resultats_commandes': resultats_commandes,
            'output_resume': self._resumer_outputs(resultats_commandes)
        }
        
        # Sauvegarder dans la mémoire
        self.memory['taches_executees'].append(resultat_tache)
        self._mettre_a_jour_stats(success_global)
        
        self.logger.info(f"🔄 Tâche {tache.get('id')}: {'✅' if success_global else '❌'}")
        
        return resultat_tache
    
    def _traduire_tache_en_commandes(self, tache: Dict[str, Any]) -> List[str]:
        """🔧 Traduction d'une tâche en commandes shell"""
        
        action = tache.get('action', '').lower()
        type_action = tache.get('type', 'general')
        
        # Mapping action -> commandes
        if 'log' in action or 'analyser' in action:
            return [
                'find . -name "*.log" -type f | head -10',
                'ls -la memory/logs/',
                'wc -l memory/logs/*.log'
            ]
        
        elif 'disque' in action or 'espace' in action:
            return [
                'df -h',
                'du -sh .',
                'du -sh memory/'
            ]
        
        elif 'processus' in action:
            return [
                'ps aux | grep python',
                'ps aux | head -10',
                'uptime'
            ]
        
        elif 'métrique' in action or 'rapport' in action:
            return [
                'free -h',
                'df -h',
                'ps aux | wc -l',
                'date'
            ]
        
        else:
            # Commandes génériques
            return [
                'pwd',
                'ls -la',
                'date'
            ]
    
    def _valider_commandes_securite(self, commandes: List[str]) -> List[str]:
        """🛡️ Validation sécurité des commandes"""
        
        commandes_validees = []
        
        for commande in commandes:
            # Extraire la commande de base
            cmd_base = commande.split()[0] if commande.split() else ''
            
            # Vérifier si autorisée
            if cmd_base in self.commandes_autorisees:
                commandes_validees.append(commande)
            else:
                self.logger.warning(f"🛡️ Commande bloquée: {commande}")
        
        return commandes_validees
    
    def _executer_commande(self, commande: str) -> Dict[str, Any]:
        """⚡ Exécution d'une commande shell"""
        
        timestamp_start = datetime.now()
        
        try:
            result = subprocess.run(
                commande,
                shell=True,
                capture_output=True,
                text=True,
                timeout=30,
                cwd=str(self.base_dir)
            )
            
            duration = (datetime.now() - timestamp_start).total_seconds()
            
            resultat = {
                'commande': commande,
                'success': result.returncode == 0,
                'returncode': result.returncode,
                'stdout': result.stdout.strip(),
                'stderr': result.stderr.strip(),
                'duration': duration,
                'timestamp': timestamp_start.isoformat()
            }
            
            # Sauvegarder dans l'historique
            self.memory['commandes_history'].append(resultat)
            
            return resultat
            
        except subprocess.TimeoutExpired:
            self.logger.error(f"⏰ Timeout commande: {commande}")
            return {
                'commande': commande,
                'success': False,
                'error': 'Timeout (30s)',
                'duration': 30.0,
                'timestamp': timestamp_start.isoformat()
            }
            
        except Exception as e:
            self.logger.error(f"❌ Erreur commande {commande}: {e}")
            return {
                'commande': commande,
                'success': False,
                'error': str(e),
                'duration': 0,
                'timestamp': timestamp_start.isoformat()
            }
    
    def _resumer_outputs(self, resultats_commandes: List[Dict[str, Any]]) -> str:
        """📊 Résumé des outputs des commandes"""
        
        outputs = []
        
        for resultat in resultats_commandes:
            if resultat['success'] and resultat.get('stdout'):
                # Prendre les premières lignes de l'output
                lines = resultat['stdout'].split('\n')[:3]
                output_court = ' | '.join(lines)
                outputs.append(f"{resultat['commande']}: {output_court}")
            elif not resultat['success']:
                outputs.append(f"{resultat['commande']}: ERREUR")
        
        return ' ; '.join(outputs)
    
    def _mettre_a_jour_stats(self, success: bool) -> None:
        """📈 Mise à jour des statistiques"""
        
        self.memory['performance_stats']['total_executions'] += 1
        
        if success:
            self.memory['performance_stats']['successful_executions'] += 1
        else:
            self.memory['performance_stats']['failed_executions'] += 1
    
    def executer_taches_multiples(self, taches: List[Dict[str, Any]]) -> Dict[str, Any]:
        """🔄 Exécution de plusieurs tâches"""
        
        timestamp_start = datetime.now()
        resultats = []
        
        for tache in taches:
            resultat = self.executer_tache(tache)
            resultats.append(resultat)
        
        # Compilation globale
        taches_reussies = sum(1 for r in resultats if r['success'])
        
        rapport_global = {
            'timestamp': timestamp_start.isoformat(),
            'taches_total': len(taches),
            'taches_reussies': taches_reussies,
            'taches_echouees': len(taches) - taches_reussies,
            'success_rate': taches_reussies / len(taches) if taches else 0,
            'duration_total': (datetime.now() - timestamp_start).total_seconds(),
            'resultats_detailles': resultats
        }
        
        self.logger.info(f"🔄 Exécution multiple: {taches_reussies}/{len(taches)} réussies")
        
        return rapport_global
    
    def get_status(self) -> Dict[str, Any]:
        """📊 Statut du worker"""
        
        stats = self.memory['performance_stats']
        
        success_rate = 0
        if stats['total_executions'] > 0:
            success_rate = stats['successful_executions'] / stats['total_executions']
        
        return {
            'total_executions': stats['total_executions'],
            'successful_executions': stats['successful_executions'],
            'failed_executions': stats['failed_executions'],
            'success_rate': round(success_rate, 2),
            'commandes_autorisees': len(self.commandes_autorisees),
            'derniere_execution': self.memory['taches_executees'][-1]['timestamp'] if self.memory['taches_executees'] else None
        }

if __name__ == "__main__":
    # Test du worker
    worker = WorkerChien()
    
    print("🐕 Test Worker Chien")
    
    # Test d'une tâche
    tache_test = {
        'id': 'test_1',
        'action': 'Vérifier l\'état du système',
        'type': 'system_check'
    }
    
    resultat = worker.executer_tache(tache_test)
    print(f"🔄 Tâche: {'✅' if resultat['success'] else '❌'}")
    print(f"📊 Output: {resultat['output_resume']}")
    
    # Statut
    status = worker.get_status()
    print(f"📊 Statut: {status}")
