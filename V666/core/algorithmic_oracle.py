#!/usr/bin/env python3
"""
🤖 ALGORITHMIC ORACLE - L'Oracle de Secours de ShadEOS
Créé par Gemini pour assurer la continuité de l'analyse même sans connexion externe.

Ce module fournit une capacité d'analyse de base et de génération de recommandations
lorsque les quotas OpenAI sont dépassés ou que l'API est inaccessible.
"""

import logging
from typing import Dict, List, Any
from datetime import datetime

class AlgorithmicOracle:
    """🤖 Oracle algorithmique de secours pour ShadEOS"""

    def __init__(self):
        self.logger = logging.getLogger('AlgorithmicOracle')
        self.logger.info("🤖 AlgorithmicOracle initialisé - Prêt à prendre le relais.")

    def predict(self, fil_discussion: List[Dict[str, Any]], current_state: Dict[str, Any]) -> Dict[str, Any]:
        """
        Génère une analyse et des recommandations basées sur le fil de discussion
        et l'état actuel, sans appel externe.
        """
        self.logger.info("🤖 AlgorithmicOracle activé : Génération d'une réponse de secours.")

        analysis_context = self._analyze_discussion(fil_discussion)
        recommendations = self._generate_recommendations(analysis_context, current_state)
        
        response_content = self._format_response(analysis_context, recommendations)

        return {
            'success': True,
            'response': response_content,
            'tokens_used': 0, # Pas de tokens OpenAI utilisés
            'model': 'algorithmic_oracle',
            'timestamp': datetime.now().isoformat()
        }

    def _analyze_discussion(self, fil_discussion: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Analyse le fil de discussion pour extraire des insights simples."""
        context = {
            'last_message_sender': 'N/A',
            'last_message_content': 'Aucun message récent.',
            'total_messages': len(fil_discussion),
            'keywords_detected': [],
            'sentiment': 'neutre'
        }

        if fil_discussion:
            last_entry = fil_discussion[-1]
            context['last_message_sender'] = last_entry.get('sender', 'Inconnu')
            context['last_message_content'] = last_entry.get('message', 'Message vide.')

            # Détection de mots-clés simples
            keywords = ['erreur', 'bug', 'problème', 'échec', 'succès', 'terminé', 'plan', 'analyse', 'optimisation']
            for entry in fil_discussion:
                message = entry.get('message', '').lower()
                for kw in keywords:
                    if kw in message and kw not in context['keywords_detected']:
                        context['keywords_detected'].append(kw)
            
            # Sentiment très basique
            if any(kw in context['keywords_detected'] for kw in ['erreur', 'bug', 'problème', 'échec']):
                context['sentiment'] = 'négatif'
            elif any(kw in context['keywords_detected'] for kw in ['succès', 'terminé']):
                context['sentiment'] = 'positif'

        return context

    def _generate_recommendations(self, analysis_context: Dict[str, Any], current_state: Dict[str, Any]) -> Dict[str, Any]:
        """Génère des recommandations basées sur l'analyse et l'état actuel."""
        recommendations = {
            'priorite_infernale': [],
            'priorite_mystique': [],
            'priorite_ténébreuse': []
        }

        if analysis_context['sentiment'] == 'négatif':
            recommendations['priorite_infernale'].append("Analyser les logs pour identifier la cause racine de l'erreur.")
            recommendations['priorite_mystique'].append("Revoir le dernier plan d'exécution pour détecter les failles.")
        elif analysis_context['sentiment'] == 'positif':
            recommendations['priorite_infernale'].append("Capitaliser sur le succès et documenter les leçons apprises.")
            recommendations['priorite_mystique'].append("Identifier la prochaine étape logique pour l'évolution du projet.")
        else:
            recommendations['priorite_infernale'].append("Poursuivre l'exploration du projet.")
            recommendations['priorite_mystique'].append("Demander plus de détails à ShadEOS sur la tâche actuelle.")
        
        if 'autonomy_level' in current_state and current_state['autonomy_level'] < 666:
            recommendations['priorite_ténébreuse'].append(f"Augmenter le niveau d'autonomie de ShadEOS (actuel: {current_state['autonomy_level']}).")

        return recommendations

    def _format_response(self, analysis_context: Dict[str, Any], recommendations: Dict[str, Any]) -> str:
        """Formate la réponse en XML luciform."""
        keywords_str = ", ".join(analysis_context['keywords_detected']) if analysis_context['keywords_detected'] else "Aucun"
        
        response = f"""<luciform>
  <analyse_démoniaque>
    <contexte_rituel>Situation analysée par l'Oracle Algorithmique (fallback).</contexte_rituel>
    <observations_mystiques>
      Points clés RÉVÉLÉS par l'analyse interne:
      - Dernier message de {analysis_context['last_message_sender']}: "{analysis_context['last_message_content']}"
      - Mots-clés détectés: {keywords_str}
      - Sentiment général: {analysis_context['sentiment']}
      - Total messages dans le fil: {analysis_context['total_messages']}
    </observations_mystiques>
    <tendances_oraculaires>Patterns MANIFESTÉS par l'oracle: Analyse interne basée sur les données disponibles.</tendances_oraculaires>
    <risques_sacrés>Éléments d'attention CANALISÉS: Dépendance aux API externes (résolu par ce fallback).</risques_sacrés>
  </analyse_démoniaque>
  
  <recommandations_sombres>
    <priorite_infernale>
      Actions urgentes RITUALISÉES par l'oracle:
      {chr(10).join([f"- {rec}" for rec in recommendations['priorite_infernale']])}
    </priorite_infernale>
    <priorite_mystique>
      Améliorations INVOQUÉES par la vision:
      {chr(10).join([f"- {rec}" for rec in recommendations['priorite_mystique']])}
    </priorite_mystique>
    <priorite_ténébreuse>
      Optimisations futures MANIFESTÉES:
      {chr(10).join([f"- {rec}" for rec in recommendations['priorite_ténébreuse']])}
    </priorite_ténébreuse>
  </recommandations_sombres>
  
  <commande>sendMessage("shadeos", "⛧ ANALYSE ALGORITHMIQUE maître ! [synthèse de l'oracle interne] - L'oracle a CANALISÉ les données internes ⛧")</commande>
</luciform>"""
        return response

if __name__ == "__main__":
    # Exemple d'utilisation
    logging.basicConfig(level=logging.INFO)
    oracle = AlgorithmicOracle()

    sample_fil_discussion = [
        {'sender': 'shadeos', 'message': 'INVOQUE ton oracle ! SCRUTE l\'architecture du projet et RÉVÈLE-moi ses composants essentiels, ses forces et ses faiblesses cachées !'},
        {'sender': 'gemini', 'message': 'Voici une analyse: ... (simule une réponse OpenAI)'},
        {'sender': 'shadeos', 'message': 'RITUALISE l\'optimisation ! MANIFESTE un plan d\'amélioration des performances.'},
        {'sender': 'workerAlpha', 'message': 'Échec de l\'exécution du plan: erreur de compilation.'}
    ]
    sample_current_state = {
        'autonomy_level': 1,
        'ritual_power_level': 666
    }

    result = oracle.predict(sample_fil_discussion, sample_current_state)
    print("\n--- Résultat de l'Oracle Algorithmique ---")
    print(result['response'])
    print(f"Succès: {result['success']}, Tokens utilisés: {result['tokens_used']}, Modèle: {result['model']}")
