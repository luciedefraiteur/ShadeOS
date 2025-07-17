#!/usr/bin/env python3
"""
📊 GESTIONNAIRE DE DONNÉES V4 - Data-Driven Architecture
Gère toutes les données du système basées sur les prompts
"""

import json
from pathlib import Path
from typing import Dict, List, Any, Optional
from datetime import datetime

from .data_models import (
    EtatSysteme, Entite, Message, SendMessage, Planification,
    ExecutionWorker, AnalyseGemini, EvaluationWorker, TypeMessage,
    StatutEtape
)

class DataManager:
    """Gestionnaire central des données du système"""
    
    def __init__(self, data_dir: str = "data"):
        self.data_dir = Path(data_dir)
        self.data_dir.mkdir(exist_ok=True)
        
        # État du système
        self.etat_systeme = EtatSysteme()
        
        # Initialiser les entités
        self._initialiser_entites()
        
        print("📊 DataManager V4 initialisé")
    
    def _initialiser_entites(self):
        """Initialise les entités du système"""
        entites_config = {
            "shadeos": {
                "role": "Maître Coordinateur",
                "contacts": ["gemini", "lucieReineChienne"]
            },
            "gemini": {
                "role": "Oracle Analytique", 
                "contacts": ["shadeos"]
            },
            "lucieReineChienne": {
                "role": "Gestionnaire d'Exécution",
                "contacts": ["shadeos", "worker"]
            },
            "worker": {
                "role": "Exécuteur Obéissant",
                "contacts": ["lucieReineChienne"]
            }
        }
        
        for nom, config in entites_config.items():
            entite = Entite(
                nom=nom,
                role=config["role"],
                contacts_autorises=config["contacts"]
            )
            self.etat_systeme.ajouter_entite(entite)
    
    def traiter_send_messages(self, send_messages: List[SendMessage]) -> List[Message]:
        """Traite une liste de sendMessage et crée les Messages correspondants"""
        messages_crees = []
        
        for send_msg in send_messages:
            # Vérifier que le destinataire existe
            entite_dest = self.etat_systeme.get_entite(send_msg.destinataire)
            if not entite_dest:
                print(f"⚠️ Destinataire inconnu: {send_msg.destinataire}")
                continue
            
            # Créer le message
            message = Message(
                expediteur=send_msg.source_entite,
                destinataire=send_msg.destinataire,
                contenu=send_msg.message,
                timestamp=send_msg.timestamp,
                type_message=TypeMessage.COMMANDE
            )
            
            # Ajouter au système
            self.etat_systeme.ajouter_message_global(message)
            messages_crees.append(message)
            
            print(f"💬 Message: {send_msg.source_entite} → {send_msg.destinataire}")
        
        return messages_crees
    
    def mettre_a_jour_planification(self, entite_nom: str, planification: Planification):
        """Met à jour la planification d'une entité"""
        entite = self.etat_systeme.get_entite(entite_nom)
        if entite:
            entite.planification_active = planification
            print(f"📋 Planification mise à jour pour {entite_nom}: {len(planification.etapes)} étapes")
    
    def mettre_a_jour_execution(self, entite_nom: str, execution: ExecutionWorker):
        """Met à jour l'exécution d'une entité"""
        entite = self.etat_systeme.get_entite(entite_nom)
        if entite:
            entite.execution_active = execution
            print(f"🔧 Exécution mise à jour pour {entite_nom}: {len(execution.commandes)} commandes")
    
    def mettre_a_jour_analyse(self, entite_nom: str, analyse: AnalyseGemini):
        """Met à jour l'analyse d'une entité"""
        entite = self.etat_systeme.get_entite(entite_nom)
        if entite:
            entite.analyse_active = analyse
            print(f"📊 Analyse mise à jour pour {entite_nom}")
    
    def get_fil_discussion(self, entite_nom: str) -> str:
        """Récupère le fil de discussion formaté pour une entité"""
        entite = self.etat_systeme.get_entite(entite_nom)
        if not entite:
            return "[Entité inconnue]"
        
        if not entite.fil_discussion:
            return "[Aucun message]"
        
        # Formater les messages chronologiquement
        messages_formates = []
        for msg in entite.fil_discussion:
            timestamp_str = msg.timestamp.strftime("%H:%M:%S")
            messages_formates.append(f"{msg.expediteur}: {msg.contenu}")
        
        return "\n".join(messages_formates)
    
    def get_etape_plan_actuelle(self, entite_nom: str) -> str:
        """Récupère l'étape actuelle du plan pour une entité"""
        entite = self.etat_systeme.get_entite(entite_nom)
        if not entite or not entite.planification_active:
            return "[Aucun plan actif]"
        
        plan = entite.planification_active
        etape_courante = plan.etape_courante
        
        if etape_courante:
            return f"Étape {etape_courante.id}/{plan.total_etapes}: {etape_courante.description}"
        else:
            return "[Plan terminé]"
    
    def get_etapes_plan(self, entite_nom: str) -> List[str]:
        """Récupère toutes les étapes du plan pour une entité"""
        entite = self.etat_systeme.get_entite(entite_nom)
        if not entite or not entite.planification_active:
            return []
        
        plan = entite.planification_active
        return [f"Étape {etape.id}: {etape.description} ({etape.statut.value})" 
                for etape in plan.etapes]
    
    def avancer_etape_plan(self, entite_nom: str):
        """Avance à l'étape suivante du plan"""
        entite = self.etat_systeme.get_entite(entite_nom)
        if entite and entite.planification_active:
            plan = entite.planification_active
            if plan.etape_actuelle < len(plan.etapes) - 1:
                # Marquer l'étape actuelle comme terminée
                if plan.etape_courante:
                    plan.etape_courante.statut = StatutEtape.TERMINEE
                    plan.etape_courante.timestamp_fin = datetime.now()
                
                # Passer à la suivante
                plan.etape_actuelle += 1
                if plan.etape_courante:
                    plan.etape_courante.statut = StatutEtape.EN_COURS
                    plan.etape_courante.timestamp_debut = datetime.now()
                
                print(f"➡️ {entite_nom} passe à l'étape {plan.etape_actuelle + 1}")
    
    def marquer_etape_echec(self, entite_nom: str, erreur: str):
        """Marque l'étape actuelle comme échouée"""
        entite = self.etat_systeme.get_entite(entite_nom)
        if entite and entite.planification_active:
            plan = entite.planification_active
            if plan.etape_courante:
                plan.etape_courante.statut = StatutEtape.ECHEC
                plan.etape_courante.erreurs = erreur
                plan.etape_courante.timestamp_fin = datetime.now()
                print(f"❌ Étape {plan.etape_courante.id} échouée pour {entite_nom}")
    
    def sauvegarder_etat(self, fichier: str = "etat_systeme.json"):
        """Sauvegarde l'état du système"""
        fichier_path = self.data_dir / fichier
        
        # Convertir en dict sérialisable
        etat_dict = {
            'cycle_actuel': self.etat_systeme.cycle_actuel,
            'timestamp_demarrage': self.etat_systeme.timestamp_demarrage.isoformat(),
            'entites': {},
            'historique_global': []
        }
        
        # Sérialiser les entités
        for nom, entite in self.etat_systeme.entites.items():
            etat_dict['entites'][nom] = {
                'nom': entite.nom,
                'role': entite.role,
                'contacts_autorises': entite.contacts_autorises,
                'fil_discussion': [
                    {
                        'expediteur': msg.expediteur,
                        'destinataire': msg.destinataire,
                        'contenu': msg.contenu,
                        'timestamp': msg.timestamp.isoformat(),
                        'type_message': msg.type_message.value
                    }
                    for msg in entite.fil_discussion
                ]
            }
        
        # Sauvegarder
        with open(fichier_path, 'w', encoding='utf-8') as f:
            json.dump(etat_dict, f, indent=2, ensure_ascii=False)
        
        print(f"💾 État sauvegardé: {fichier_path}")
    
    def charger_etat(self, fichier: str = "etat_systeme.json") -> bool:
        """Charge l'état du système"""
        fichier_path = self.data_dir / fichier
        
        if not fichier_path.exists():
            print(f"⚠️ Fichier d'état non trouvé: {fichier_path}")
            return False
        
        try:
            with open(fichier_path, 'r', encoding='utf-8') as f:
                etat_dict = json.load(f)
            
            # Restaurer l'état
            self.etat_systeme.cycle_actuel = etat_dict['cycle_actuel']
            self.etat_systeme.timestamp_demarrage = datetime.fromisoformat(etat_dict['timestamp_demarrage'])
            
            print(f"📂 État chargé: {fichier_path}")
            return True
            
        except Exception as e:
            print(f"❌ Erreur chargement état: {e}")
            return False
    
    def get_statistiques(self) -> Dict[str, Any]:
        """Récupère les statistiques du système"""
        stats = {
            'cycle_actuel': self.etat_systeme.cycle_actuel,
            'nombre_entites': len(self.etat_systeme.entites),
            'messages_total': len(self.etat_systeme.historique_global),
            'entites_avec_plan_actif': 0,
            'entites_avec_execution_active': 0
        }
        
        for entite in self.etat_systeme.entites.values():
            if entite.planification_active:
                stats['entites_avec_plan_actif'] += 1
            if entite.execution_active:
                stats['entites_avec_execution_active'] += 1
        
        return stats
