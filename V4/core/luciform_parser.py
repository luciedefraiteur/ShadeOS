#!/usr/bin/env python3
"""
🔮 PARSEUR LUCIFORM V4 - Data-Driven
Parse les réponses XML et extrait les structures de données
"""

import xml.etree.ElementTree as ET
from typing import List, Dict, Any, Optional
import re
from datetime import datetime

from .data_models import (
    SendMessage, Etape, Planification, CommandeShell, ExecutionWorker,
    AnalyseGemini, EvaluationWorker, StatutEtape, StatutExecution,
    PrioriteRecommandation
)

class LuciformParser:
    """Parser pour les réponses luciform XML"""
    
    def __init__(self):
        print("🔮 LuciformParser V4 initialisé")
    
    def parse_reponse(self, reponse_xml: str, source_entite: str) -> Dict[str, Any]:
        """Parse une réponse luciform et extrait toutes les données"""
        try:
            # Nettoyer le XML
            xml_clean = self._nettoyer_xml(reponse_xml)
            root = ET.fromstring(xml_clean)
            
            resultats = {
                'send_messages': [],
                'planification': None,
                'execution': None,
                'analyse': None,
                'evaluation': None,
                'shell_commands': [],
                'metadata': {}
            }
            
            # Extraire les sendMessage
            resultats['send_messages'] = self._extraire_send_messages(root, source_entite)
            
            # Extraire selon le type de réponse
            if source_entite == "lucie":
                resultats['planification'] = self._extraire_planification(root)
                resultats['evaluation'] = self._extraire_evaluation(root)
            elif source_entite == "worker":
                resultats['execution'] = self._extraire_execution(root)
                resultats['shell_commands'] = self._extraire_shell_commands(root)
            elif source_entite == "gemini":
                resultats['analyse'] = self._extraire_analyse(root)
            
            # Métadonnées générales
            resultats['metadata'] = self._extraire_metadata(root)
            
            return resultats
            
        except Exception as e:
            print(f"❌ Erreur parsing luciform: {e}")
            return {'error': str(e)}
    
    def _nettoyer_xml(self, xml_str: str) -> str:
        """Nettoie le XML pour le parsing"""
        # Enlever les commentaires XML
        xml_str = re.sub(r'<!--.*?-->', '', xml_str, flags=re.DOTALL)
        
        # S'assurer qu'on a une racine luciform
        if not xml_str.strip().startswith('<luciform'):
            # Chercher le bloc luciform
            match = re.search(r'<luciform.*?</luciform>', xml_str, re.DOTALL)
            if match:
                xml_str = match.group(0)
            else:
                raise ValueError("Pas de bloc luciform trouvé")
        
        return xml_str
    
    def _extraire_send_messages(self, root: ET.Element, source: str) -> List[SendMessage]:
        """Extrait tous les sendMessage"""
        messages = []
        
        for commande in root.findall('.//commande'):
            texte = commande.text or ""
            
            # Parser sendMessage("destinataire", "message")
            pattern = r'sendMessage\s*\(\s*["\']([^"\']+)["\']\s*,\s*["\']([^"\']+)["\']\s*\)'
            matches = re.findall(pattern, texte)
            
            for destinataire, message in matches:
                messages.append(SendMessage(
                    destinataire=destinataire,
                    message=message,
                    source_entite=source
                ))
        
        return messages
    
    def _extraire_planification(self, root: ET.Element) -> Optional[Planification]:
        """Extrait la planification de Lucie"""
        planif_elem = root.find('.//planification')
        if planif_elem is None:
            return None
        
        etapes = []
        for etape_elem in planif_elem.findall('etape'):
            etape_id = etape_elem.get('id', '')
            description = etape_elem.text or ""
            
            etapes.append(Etape(
                id=etape_id,
                description=description,
                statut=StatutEtape.EN_ATTENTE
            ))
        
        return Planification(etapes=etapes)
    
    def _extraire_execution(self, root: ET.Element) -> Optional[ExecutionWorker]:
        """Extrait les résultats d'exécution du Worker"""
        exec_elem = root.find('.//execution')
        if exec_elem is None:
            return None
        
        commandes = []
        for shell_elem in exec_elem.findall('shell'):
            commande_text = shell_elem.text or ""
            commandes.append(CommandeShell(commande=commande_text))
        
        # Extraire les résultats
        resultats_elem = root.find('.//resultats')
        rapport = ""
        if resultats_elem is not None:
            resultats = []
            for res_elem in resultats_elem.findall('resultat'):
                resultats.append(res_elem.text or "")
            rapport = "\n".join(resultats)
        
        return ExecutionWorker(
            commandes=commandes,
            rapport=rapport,
            statut_global=StatutExecution.EN_COURS
        )
    
    def _extraire_shell_commands(self, root: ET.Element) -> List[CommandeShell]:
        """Extrait les commandes shell"""
        commandes = []
        
        for shell_elem in root.findall('.//shell'):
            commande_text = shell_elem.text or ""
            if commande_text.strip():
                commandes.append(CommandeShell(commande=commande_text))
        
        return commandes
    
    def _extraire_analyse(self, root: ET.Element) -> Optional[AnalyseGemini]:
        """Extrait l'analyse de Gemini"""
        analyse_elem = root.find('.//analyse')
        if analyse_elem is None:
            return None
        
        # Extraire les éléments d'analyse
        contexte = self._get_text_safe(analyse_elem.find('contexte'))
        
        observations = []
        obs_elem = analyse_elem.find('observations')
        if obs_elem is not None:
            observations = [obs_elem.text or ""]
        
        tendances = []
        tend_elem = analyse_elem.find('tendances')
        if tend_elem is not None:
            tendances = [tend_elem.text or ""]
        
        risques = []
        risq_elem = analyse_elem.find('risques')
        if risq_elem is not None:
            risques = [risq_elem.text or ""]
        
        # Extraire recommandations
        recommandations = {}
        reco_elem = root.find('.//recommandations')
        if reco_elem is not None:
            for priorite in PrioriteRecommandation:
                elem = reco_elem.find(priorite.value)
                if elem is not None:
                    recommandations[priorite] = [elem.text or ""]
        
        return AnalyseGemini(
            contexte=contexte,
            observations=observations,
            tendances=tendances,
            risques=risques,
            recommandations=recommandations
        )
    
    def _extraire_evaluation(self, root: ET.Element) -> Optional[EvaluationWorker]:
        """Extrait l'évaluation de Lucie"""
        eval_elem = root.find('.//evaluation')
        if eval_elem is None:
            return None
        
        statut_text = self._get_text_safe(eval_elem.find('statut_worker'))
        statut = StatutExecution.SUCCES if statut_text == "SUCCÈS" else StatutExecution.ECHEC
        
        analyse = self._get_text_safe(eval_elem.find('analyse_resultats'))
        
        # Extraire plan correctif si échec
        etapes_correctives = []
        plan_elem = root.find('.//nouveau_plan')
        if plan_elem is not None:
            etapes_elem = plan_elem.find('etapes_correctives')
            if etapes_elem is not None:
                for etape_elem in etapes_elem.findall('etape'):
                    etape_id = etape_elem.get('id', '')
                    description = etape_elem.text or ""
                    etapes_correctives.append(Etape(
                        id=etape_id,
                        description=description
                    ))
        
        return EvaluationWorker(
            statut_worker=statut,
            analyse_resultats=analyse,
            etapes_correctives=etapes_correctives
        )
    
    def _extraire_metadata(self, root: ET.Element) -> Dict[str, Any]:
        """Extrait les métadonnées du luciform"""
        metadata = {}
        
        # Attributs de la racine
        metadata['id'] = root.get('id', '')
        metadata['type'] = root.get('type', '')
        metadata['niveau'] = root.get('niveau', '')
        
        # Éléments de base
        metadata['entite'] = self._get_text_safe(root.find('entité'))
        metadata['role'] = self._get_text_safe(root.find('rôle'))
        metadata['but'] = self._get_text_safe(root.find('but'))
        metadata['style'] = self._get_text_safe(root.find('style'))
        
        return metadata
    
    def _get_text_safe(self, element: Optional[ET.Element]) -> str:
        """Récupère le texte d'un élément de manière sécurisée"""
        return element.text or "" if element is not None else ""
