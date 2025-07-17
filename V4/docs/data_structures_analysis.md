# 📊 ANALYSE DES STRUCTURES DE DONNÉES V4

## 🔮 **DONNÉES EXTRAITES DES PROMPTS LUCIFORM**

### 📝 **VARIABLES CONTEXTUELLES**
```python
# Variables communes à tous les prompts
monFilDiscussion: str          # Historique chronologique des messages
monEtapePlanActuelle: str      # Étape actuelle (Lucie/Worker)
mesEtapesPlan: List[str]       # Toutes les étapes du plan (Lucie)
```

### 💬 **STRUCTURE MESSAGE**
```python
@dataclass
class Message:
    expediteur: str            # "shadeos", "gemini", "lucie", "worker"
    destinataire: str          # Entité cible
    contenu: str              # Contenu du message
    timestamp: datetime       # Horodatage
    type_message: str         # "commande", "rapport", "analyse"
```

### 🔄 **STRUCTURE SENDMESSAGE**
```python
@dataclass
class SendMessage:
    destinataire: str         # Entité cible
    message: str             # Contenu à envoyer
    source_entite: str       # Qui envoie
```

### 📋 **STRUCTURE PLANIFICATION (LUCIE)**
```python
@dataclass
class Etape:
    id: str                  # "1", "2", "3"...
    description: str         # Description de l'étape
    statut: str             # "en_attente", "en_cours", "terminee", "echec"

@dataclass
class Planification:
    etapes: List[Etape]
    etape_actuelle: int
    total_etapes: int
```

### 🔧 **STRUCTURE EXÉCUTION (WORKER)**
```python
@dataclass
class CommandeShell:
    commande: str           # Commande à exécuter
    resultat: str          # Résultat de l'exécution
    code_retour: int       # Code de retour
    timestamp: datetime    # Quand exécutée

@dataclass
class ExecutionWorker:
    commandes: List[CommandeShell]
    statut_global: str     # "succes", "echec", "en_cours"
    rapport: str          # Rapport final
```

### 📊 **STRUCTURE ANALYSE (GEMINI)**
```python
@dataclass
class AnalyseGemini:
    contexte: str
    observations: List[str]
    tendances: List[str]
    risques: List[str]
    recommandations: Dict[str, List[str]]  # priorite -> actions
```

### 🎯 **STRUCTURE ÉVALUATION (LUCIE)**
```python
@dataclass
class EvaluationWorker:
    statut_worker: str      # "SUCCÈS" ou "ÉCHEC"
    analyse_resultats: str
    probleme_identifie: str = None
    solution_proposee: str = None
    etapes_correctives: List[Etape] = None
```

## 🏗️ **ARCHITECTURE DATA-DRIVEN**

### 📦 **ENTITÉS PRINCIPALES**
```python
@dataclass
class Entite:
    nom: str                    # "shadeos", "gemini", etc.
    role: str                   # "Maître Coordinateur", etc.
    fil_discussion: List[Message]
    contacts_autorises: List[str]
    etat_actuel: Dict[str, Any]
```

### 🔄 **FLUX DE DONNÉES**
```python
@dataclass
class FluxMessage:
    message_entrant: Message
    traitement: str            # Type de traitement requis
    reponse_generee: List[SendMessage]
    donnees_mises_a_jour: Dict[str, Any]
```
