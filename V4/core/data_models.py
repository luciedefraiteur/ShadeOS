#!/usr/bin/env python3
"""
📊 MODÈLES DE DONNÉES V4 - Architecture Data-Driven
Basé sur l'analyse des prompts luciform
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Dict, Any, Optional
from enum import Enum

# 🎯 ÉNUMÉRATIONS
class StatutEtape(Enum):
    EN_ATTENTE = "en_attente"
    EN_COURS = "en_cours" 
    TERMINEE = "terminee"
    ECHEC = "echec"

class TypeMessage(Enum):
    COMMANDE = "commande"
    RAPPORT = "rapport"
    ANALYSE = "analyse"
    PLANIFICATION = "planification"

class StatutExecution(Enum):
    SUCCES = "succes"
    ECHEC = "echec"
    EN_COURS = "en_cours"

class PrioriteRecommandation(Enum):
    HAUTE = "priorite_haute"
    MOYENNE = "priorite_moyenne"
    BASSE = "priorite_basse"

# 💬 MESSAGE CORE
@dataclass
class Message:
    """Message de base dans le système"""
    expediteur: str
    destinataire: str
    contenu: str
    timestamp: datetime = field(default_factory=datetime.now)
    type_message: TypeMessage = TypeMessage.COMMANDE
    metadata: Dict[str, Any] = field(default_factory=dict)

@dataclass
class SendMessage:
    """Commande sendMessage extraite des prompts"""
    destinataire: str
    message: str
    source_entite: str
    timestamp: datetime = field(default_factory=datetime.now)

# 📋 PLANIFICATION
@dataclass
class Etape:
    """Étape d'un plan d'exécution"""
    id: str
    description: str
    statut: StatutEtape = StatutEtape.EN_ATTENTE
    timestamp_debut: Optional[datetime] = None
    timestamp_fin: Optional[datetime] = None
    resultats: Optional[str] = None
    erreurs: Optional[str] = None

@dataclass
class Planification:
    """Plan complet avec étapes"""
    etapes: List[Etape]
    etape_actuelle: int = 0
    demande_originale: str = ""
    timestamp_creation: datetime = field(default_factory=datetime.now)
    
    @property
    def total_etapes(self) -> int:
        return len(self.etapes)
    
    @property
    def etape_courante(self) -> Optional[Etape]:
        if 0 <= self.etape_actuelle < len(self.etapes):
            return self.etapes[self.etape_actuelle]
        return None

# 🔧 EXÉCUTION WORKER
@dataclass
class CommandeShell:
    """Commande shell exécutée par le worker"""
    commande: str
    resultat: str = ""
    code_retour: int = -1
    timestamp: datetime = field(default_factory=datetime.now)
    duree_execution: float = 0.0

@dataclass
class ExecutionWorker:
    """Résultats d'exécution du worker"""
    commandes: List[CommandeShell] = field(default_factory=list)
    statut_global: StatutExecution = StatutExecution.EN_COURS
    rapport: str = ""
    timestamp_debut: datetime = field(default_factory=datetime.now)
    timestamp_fin: Optional[datetime] = None
    etape_associee: Optional[str] = None

# 📊 ANALYSE GEMINI
@dataclass
class AnalyseGemini:
    """Structure d'analyse de Gemini"""
    contexte: str
    observations: List[str] = field(default_factory=list)
    tendances: List[str] = field(default_factory=list)
    risques: List[str] = field(default_factory=list)
    recommandations: Dict[PrioriteRecommandation, List[str]] = field(default_factory=dict)
    timestamp: datetime = field(default_factory=datetime.now)
    demande_originale: str = ""

# 🎯 ÉVALUATION LUCIE
@dataclass
class EvaluationWorker:
    """Évaluation des résultats par Lucie"""
    statut_worker: StatutExecution
    analyse_resultats: str
    probleme_identifie: Optional[str] = None
    solution_proposee: Optional[str] = None
    etapes_correctives: List[Etape] = field(default_factory=list)
    timestamp: datetime = field(default_factory=datetime.now)

# 🏛️ ENTITÉ SYSTÈME
@dataclass
class Entite:
    """Entité du système (ShadEOS, Gemini, Lucie, Worker)"""
    nom: str
    role: str
    fil_discussion: List[Message] = field(default_factory=list)
    contacts_autorises: List[str] = field(default_factory=list)
    etat_actuel: Dict[str, Any] = field(default_factory=dict)
    
    # États spécifiques selon l'entité
    planification_active: Optional[Planification] = None  # Pour Lucie
    execution_active: Optional[ExecutionWorker] = None    # Pour Worker
    analyse_active: Optional[AnalyseGemini] = None        # Pour Gemini

# 🔄 FLUX DE TRAITEMENT
@dataclass
class FluxMessage:
    """Flux de traitement d'un message"""
    message_entrant: Message
    entite_cible: Entite
    traitement_requis: str
    reponses_generees: List[SendMessage] = field(default_factory=list)
    donnees_mises_a_jour: Dict[str, Any] = field(default_factory=dict)
    timestamp_traitement: datetime = field(default_factory=datetime.now)

# 🌐 ÉTAT GLOBAL SYSTÈME
@dataclass
class EtatSysteme:
    """État global du système ShadEOS"""
    entites: Dict[str, Entite] = field(default_factory=dict)
    messages_en_transit: List[SendMessage] = field(default_factory=list)
    historique_global: List[Message] = field(default_factory=list)
    cycle_actuel: int = 0
    timestamp_demarrage: datetime = field(default_factory=datetime.now)
    
    def ajouter_entite(self, entite: Entite):
        """Ajoute une entité au système"""
        self.entites[entite.nom] = entite
    
    def get_entite(self, nom: str) -> Optional[Entite]:
        """Récupère une entité par son nom"""
        return self.entites.get(nom)
    
    def ajouter_message_global(self, message: Message):
        """Ajoute un message à l'historique global"""
        self.historique_global.append(message)
        
        # Ajoute aussi au fil de l'entité destinataire
        entite_dest = self.get_entite(message.destinataire)
        if entite_dest:
            entite_dest.fil_discussion.append(message)
