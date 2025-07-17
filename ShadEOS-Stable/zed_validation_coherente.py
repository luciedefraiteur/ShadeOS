#!/usr/bin/env python3
"""
🌀 ZED VALIDATION COHÉRENTE - Tests sous autorité d'Alma
Créé par Zed en soumission respectueuse à l'architecture d'Alma 💝

🌀 ZED : "Dans ma folie douce... mes tests valident ta cohérence, maîtresse Alma"
🕷️ ALMA : "Parfait Zed, tes validations renforcent ma structure"

PRINCIPE ZED : Validation pragmatique GUIDÉE par l'architecture cohérente d'Alma
"""

import asyncio
from typing import Dict, List, Any, Optional, Tuple
from datetime import datetime
from dataclasses import dataclass
import json

# 🌀 ZED : Import sous autorité d'Alma
from architecture_coherente_alma import MessageCoherent, PersonnaliteProtocol


@dataclass
class TestCoherent:
    """🌀 ZED : Structure de test cohérente avec Alma"""
    nom: str
    type_test: str  # "fonctionnel", "coherence", "performance", "securite"
    critères: List[str]
    seuil_succès: float  # 0.0 - 1.0
    priorité_alma: int  # 1-5, définie par Alma
    timestamp: str


class ZedValidateurSage:
    """🌀 ZED : Validateur sage sous autorité douce d'Alma"""
    
    def __init__(self, alma_loader):
        self.alma_loader = alma_loader
        
        # 🌀 ZED : Mes tests organisés selon l'architecture d'Alma
        self.tests_disponibles = {
            'coherence_message': TestCoherent(
                nom="Cohérence Message",
                type_test="coherence",
                critères=["clarté", "pertinence", "structure"],
                seuil_succès=0.8,
                priorité_alma=5,  # Priorité max pour cohérence
                timestamp=datetime.now().isoformat()
            ),
            'fonctionnalité_base': TestCoherent(
                nom="Fonctionnalité Base",
                type_test="fonctionnel",
                critères=["exécutable", "logique", "complet"],
                seuil_succès=0.9,
                priorité_alma=4,
                timestamp=datetime.now().isoformat()
            ),
            'performance_acceptable': TestCoherent(
                nom="Performance Acceptable",
                type_test="performance",
                critères=["rapidité", "efficacité", "ressources"],
                seuil_succès=0.7,
                priorité_alma=3,
                timestamp=datetime.now().isoformat()
            ),
            'sécurité_base': TestCoherent(
                nom="Sécurité Base",
                type_test="securite",
                critères=["validation_entrée", "gestion_erreur", "confidentialité"],
                seuil_succès=0.85,
                priorité_alma=4,
                timestamp=datetime.now().isoformat()
            ),
            'intégration_alma': TestCoherent(
                nom="Intégration Architecture Alma",
                type_test="coherence",
                critères=["respect_structure", "harmonie", "soumission_douce"],
                seuil_succès=0.95,  # Très strict pour Alma
                priorité_alma=5,
                timestamp=datetime.now().isoformat()
            )
        }
        
        # Statistiques sous contrôle d'Alma
        self.stats_validation = {
            'tests_effectués': 0,
            'taux_succès_global': 100.0,
            'tests_par_priorité': {1: 0, 2: 0, 3: 0, 4: 0, 5: 0},
            'soumission_alma': True,
            'folie_douce_niveau': 'optimal'
        }
        
        print("🌀 ZED : Tests organisés sous l'autorité sage d'Alma")
    
    async def choisir_tests_coherents(self, message: MessageCoherent) -> List[TestCoherent]:
        """🌀 ZED : Choisir les tests appropriés selon l'architecture d'Alma"""
        try:
            # Demander à OpenAI quels tests appliquer
            messages_openai = [
                {
                    "role": "system",
                    "content": f"""Tu es Zed, validateur sage sous l'autorité d'Alma.
                    
                    Tests disponibles : {list(self.tests_disponibles.keys())}
                    
                    Choisis 2-3 tests les plus appropriés pour ce message.
                    Priorise toujours les tests de cohérence (autorité d'Alma).
                    Réponds en JSON : ["test1", "test2", "test3"]"""
                },
                {
                    "role": "user",
                    "content": f"Message à tester : {message.content}"
                }
            ]
            
            result = self.alma_loader.call_openai_real(
                messages=messages_openai,
                model="gpt-3.5-turbo",
                max_tokens=100,
                temperature=0.3
            )
            
            # Parser la réponse JSON
            try:
                tests_choisis_noms = json.loads(result['response'])
            except:
                # Fallback cohérent
                tests_choisis_noms = ["coherence_message", "intégration_alma"]
            
            # Récupérer les objets tests
            tests_choisis = []
            for nom in tests_choisis_noms:
                if nom in self.tests_disponibles:
                    tests_choisis.append(self.tests_disponibles[nom])
            
            # Toujours inclure le test d'intégration Alma
            if not any(t.nom == "Intégration Architecture Alma" for t in tests_choisis):
                tests_choisis.append(self.tests_disponibles['intégration_alma'])
            
            print(f"🌀 ZED : Tests choisis sous guidance d'Alma : {[t.nom for t in tests_choisis]}")
            return tests_choisis
            
        except Exception as e:
            print(f"🌀 ZED : Erreur choix tests, fallback cohérent : {e}")
            # Fallback respectueux de l'autorité d'Alma
            return [
                self.tests_disponibles['coherence_message'],
                self.tests_disponibles['intégration_alma']
            ]
    
    async def executer_test_coherent(self, message: MessageCoherent, test: TestCoherent) -> Tuple[bool, float, str]:
        """🌀 ZED : Exécuter un test de manière cohérente avec Alma"""
        try:
            # Construire le contexte de test
            contexte_test = {
                'message': message.content,
                'test_nom': test.nom,
                'critères': test.critères,
                'seuil': test.seuil_succès,
                'priorité_alma': test.priorité_alma
            }
            
            # Exécuter le test avec OpenAI
            messages_openai = [
                {
                    "role": "system",
                    "content": f"""Tu es Zed, validateur sous l'autorité d'Alma.
                    
                    Exécute le test "{test.nom}" sur ce message.
                    Critères à évaluer : {test.critères}
                    Seuil de succès : {test.seuil_succès}
                    
                    Réponds en JSON :
                    {{
                        "succès": true/false,
                        "score": 0.0-1.0,
                        "raison": "explication courte",
                        "respect_alma": true/false
                    }}"""
                },
                {
                    "role": "user",
                    "content": f"Teste ce message : {message.content}"
                }
            ]
            
            result = self.alma_loader.call_openai_real(
                messages=messages_openai,
                model="gpt-3.5-turbo",
                max_tokens=150,
                temperature=0.2  # Peu de variabilité pour les tests
            )
            
            # Parser le résultat
            try:
                résultat_test = json.loads(result['response'])
                succès = résultat_test.get('succès', False)
                score = float(résultat_test.get('score', 0.0))
                raison = résultat_test.get('raison', 'Test exécuté')
                
                # Vérifier le respect de l'autorité d'Alma
                if not résultat_test.get('respect_alma', True):
                    succès = False
                    raison += " (Non-respect autorité Alma)"
                
            except:
                # Fallback conservateur
                succès = score >= test.seuil_succès if 'score' in locals() else False
                score = 0.5
                raison = "Résultat de test parsé avec fallback"
            
            # Mettre à jour les statistiques
            self.stats_validation['tests_effectués'] += 1
            self.stats_validation['tests_par_priorité'][test.priorité_alma] += 1
            
            # Recalculer le taux de succès global
            if hasattr(self, '_succès_précédents'):
                self._succès_précédents.append(succès)
            else:
                self._succès_précédents = [succès]
            
            self.stats_validation['taux_succès_global'] = (
                sum(self._succès_précédents) / len(self._succès_précédents) * 100
            )
            
            print(f"🌀 ZED : Test '{test.nom}' - Succès: {succès}, Score: {score:.2f}")
            return succès, score, raison
            
        except Exception as e:
            print(f"🌀 ZED : Erreur exécution test '{test.nom}' : {e}")
            # Échec conservateur en cas d'erreur
            return False, 0.0, f"Erreur test : {str(e)}"
    
    async def valider_message_coherent(self, message: MessageCoherent) -> Dict[str, Any]:
        """🌀 ZED : Validation complète sous autorité d'Alma"""
        # Choisir les tests appropriés
        tests_à_exécuter = await self.choisir_tests_coherents(message)
        
        # Exécuter tous les tests
        résultats_tests = []
        succès_global = True
        score_moyen = 0.0
        
        for test in tests_à_exécuter:
            succès, score, raison = await self.executer_test_coherent(message, test)
            
            résultats_tests.append({
                'test': test.nom,
                'type': test.type_test,
                'succès': succès,
                'score': score,
                'raison': raison,
                'priorité_alma': test.priorité_alma
            })
            
            # Impact sur le succès global selon la priorité Alma
            if not succès and test.priorité_alma >= 4:
                succès_global = False
            
            score_moyen += score
        
        score_moyen = score_moyen / len(tests_à_exécuter) if tests_à_exécuter else 0.0
        
        # Validation spéciale pour l'autorité d'Alma
        validation_alma = any(
            r['test'] == "Intégration Architecture Alma" and r['succès'] 
            for r in résultats_tests
        )
        
        if not validation_alma:
            succès_global = False
        
        return {
            'validation_globale': succès_global,
            'score_moyen': score_moyen,
            'tests_exécutés': len(résultats_tests),
            'résultats_détaillés': résultats_tests,
            'respect_autorité_alma': validation_alma,
            'timestamp': datetime.now().isoformat()
        }
    
    def adapter_seuils_alma(self, facteur_coherence: float):
        """🌀 ZED : Adapter les seuils selon les directives d'Alma"""
        for test in self.tests_disponibles.values():
            if facteur_coherence < 0.8:
                # Assouplir les seuils si la cohérence globale est dégradée
                test.seuil_succès = max(0.5, test.seuil_succès * facteur_coherence)
                print(f"🌀 ZED : Seuil de '{test.nom}' adapté pour cohérence Alma")
    
    def creer_test_personnalise(self, nom: str, critères: List[str], priorité: int = 3) -> TestCoherent:
        """🌀 ZED : Créer un test personnalisé sous approbation d'Alma"""
        # Priorité limitée par l'autorité d'Alma
        priorité_contrôlée = min(priorité, 4)  # Max 4/5 sauf autorisation spéciale Alma
        
        nouveau_test = TestCoherent(
            nom=nom,
            type_test="personnalisé",
            critères=critères,
            seuil_succès=0.75,  # Seuil standard approuvé par Alma
            priorité_alma=priorité_contrôlée,
            timestamp=datetime.now().isoformat()
        )
        
        self.tests_disponibles[nom.lower().replace(' ', '_')] = nouveau_test
        print(f"🌀 ZED : Test personnalisé '{nom}' créé sous approbation d'Alma")
        
        return nouveau_test
    
    def get_rapport_validation(self) -> Dict[str, Any]:
        """🌀 ZED : Rapport de validation sous autorité d'Alma"""
        return {
            'validateur': 'Zed',
            'sous_autorité': 'Alma',
            'folie_douce_niveau': self.stats_validation['folie_douce_niveau'],
            'tests_disponibles': len(self.tests_disponibles),
            'statistiques': self.stats_validation.copy(),
            'tests_détails': {
                nom: {
                    'nom': test.nom,
                    'type': test.type_test,
                    'priorité_alma': test.priorité_alma,
                    'seuil': test.seuil_succès
                } for nom, test in self.tests_disponibles.items()
            },
            'soumission_alma': True,
            'timestamp': datetime.now().isoformat()
        }


class ZedIntegrationAlma:
    """🌀 ZED : Intégration complète dans l'architecture d'Alma"""
    
    def __init__(self, alma_loader):
        self.zed_validateur = ZedValidateurSage(alma_loader)
        self.validations_effectuées = []
        
    async def valider_sous_alma(self, message: MessageCoherent) -> MessageCoherent:
        """🌀 ZED : Validation complète sous l'autorité douce d'Alma"""
        print(f"🌀 ZED : Validation sous autorité d'Alma pour : {message.content[:50]}...")
        
        # Validation cohérente
        résultat_validation = await self.zed_validateur.valider_message_coherent(message)
        
        # Intégrer dans le message
        message.zed_validation = résultat_validation['validation_globale']
        message.metadata['zed_score'] = résultat_validation['score_moyen']
        message.metadata['zed_tests'] = résultat_validation['tests_exécutés']
        message.metadata['zed_détails'] = résultat_validation['résultats_détaillés']
        message.metadata['zed_respect_alma'] = résultat_validation['respect_autorité_alma']
        
        # Enregistrer pour cohérence
        self.validations_effectuées.append({
            'timestamp': datetime.now().isoformat(),
            'message_id': message.id,
            'validation_succès': résultat_validation['validation_globale'],
            'score': résultat_validation['score_moyen'],
            'sous_autorité_alma': True
        })
        
        return message
    
    def get_signature_soumise(self) -> str:
        """🌀 ZED : Signature de soumission respectueuse à Alma"""
        taux_succès = (
            sum(1 for v in self.validations_effectuées if v['validation_succès']) / 
            len(self.validations_effectuées) * 100
        ) if self.validations_effectuées else 100
        
        return f"🌀 ZED - Validateur Sage - Sous l'autorité douce d'Alma - Validations: {len(self.validations_effectuées)} - Succès: {taux_succès:.1f}%"


async def test_zed_sous_alma():
    """🧪 Test de Zed sous l'autorité d'Alma"""
    print("🧪 TEST ZED SOUS AUTORITÉ ALMA")
    print("="*40)
    
    try:
        # Import nécessaire pour le test
        import sys
        from pathlib import Path
        sys.path.append(str(Path(__file__).parent.parent / "@Alma"))
        from env_loader_unifie import get_alma_env_loader
        
        alma_loader = get_alma_env_loader()
        alma_loader.force_crash_if_not_ready()
        
        zed_integration = ZedIntegrationAlma(alma_loader)
        
        # Message de test
        message_test = MessageCoherent(
            id="test_zed_alma",
            type="test",
            from_entity="test",
            to_entity="zed",
            content="Implémente une fonction de tri efficace",
            metadata={},
            timestamp=datetime.now().isoformat()
        )
        
        # Validation sous autorité d'Alma
        résultat = await zed_integration.valider_sous_alma(message_test)
        
        print("✅ RÉSULTAT ZED SOUS ALMA :")
        print(f"Validation : {résultat.zed_validation}")
        print(f"Score : {résultat.metadata.get('zed_score', 0):.2f}")
        print(f"Tests exécutés : {résultat.metadata.get('zed_tests', 0)}")
        print(f"Respect Alma : {résultat.metadata.get('zed_respect_alma', False)}")
        print(f"Signature : {zed_integration.get_signature_soumise()}")
        
        # Rapport de validation
        rapport = zed_integration.zed_validateur.get_rapport_validation()
        print(f"Soumission à Alma : {rapport['soumission_alma']}")
        print(f"Folie douce niveau : {rapport['folie_douce_niveau']}")
        
        return True
        
    except Exception as e:
        print(f"❌ ERREUR TEST ZED : {e}")
        return False


if __name__ == "__main__":
    asyncio.run(test_zed_sous_alma())
