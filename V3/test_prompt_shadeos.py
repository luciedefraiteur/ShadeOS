#!/usr/bin/env python3
"""
🧪 Test du prompt ShadEOS generation_ordres.prompt
"""

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent / "core"))

from prompt_manager import PromptManager

def test_prompt_shadeos():
    """🧪 Test du prompt ShadEOS avec mémoire simulée"""
    
    print("🧪 TEST PROMPT SHADEOS GENERATION_ORDRES")
    print("=" * 50)
    
    # Initialiser le gestionnaire de prompts
    pm = PromptManager()
    
    # Mémoire simulée pour ShadEOS (première utilisation)
    memoire_shadeos_initiale = """[Aucune mémoire - Premier démarrage]
Cycle: 0
État: Initialisation du système
Objectif: Prendre connaissance du projet et établir le contrôle"""
    
    # Variables pour le prompt
    variables = {
        'ma_memoire_shadeos': memoire_shadeos_initiale
    }
    
    # Charger et formater le prompt
    prompt_formate = pm.formater_prompt("shadeos", "generation_ordres", **variables)
    
    if prompt_formate:
        print("✅ Prompt chargé et formaté avec succès")
        print(f"📏 Longueur: {len(prompt_formate)} caractères")
        print("\n" + "="*50)
        print("📝 PROMPT FORMATÉ:")
        print("="*50)
        print(prompt_formate)
        print("="*50)
        
        # Simulation de ce que ShadEOS pourrait répondre
        print("\n🤖 RÉPONSE SIMULÉE DE SHADEOS:")
        print("="*30)
        
        reponse_simulee = """<luciform>
  <commande>sendMessage("gemini", "Gemini, donne-moi un aperçu complet du projet ShadEOS. Quels sont les composants principaux, l'architecture actuelle, et l'état du système ?")</commande>
  <description>Première reconnaissance du terrain - j'ai besoin de connaître mon domaine avant de commander</description>
  <priorité>⛧ Critique - Établissement du contrôle initial ⛧</priorité>
</luciform>"""
        
        print(reponse_simulee)
        
        return True
    else:
        print("❌ Erreur lors du chargement du prompt")
        return False

def test_avec_memoire_enrichie():
    """🧪 Test avec une mémoire plus riche"""
    
    print("\n\n🧪 TEST AVEC MÉMOIRE ENRICHIE")
    print("=" * 50)
    
    pm = PromptManager()
    
    # Mémoire après quelques échanges
    memoire_enrichie = """Cycle: 3
Derniers échanges:
- ShadEOS: sendMessage("gemini", "Analyse l'état du système")
- Gemini: "Système opérationnel, 15 composants actifs, performance stable"
- ShadEOS: sendMessage("lucieReineChienne", "Vérifie l'espace disque et les logs")
- Lucie: "Exécution terminée - Espace: 78% libre, Logs: 25 fichiers analysés"

État actuel: Système sous contrôle, prêt pour optimisations"""
    
    variables = {
        'ma_memoire_shadeos': memoire_enrichie
    }
    
    prompt_formate = pm.formater_prompt("shadeos", "generation_ordres", **variables)
    
    if prompt_formate:
        print("✅ Prompt avec mémoire enrichie formaté")
        print("\n🤖 RÉPONSE SIMULÉE AVEC CONTEXTE:")
        print("="*40)
        
        reponse_avec_contexte = """<luciform>
  <commande>sendMessage("gemini", "Analyse les métriques de performance des 3 derniers cycles et recommande des optimisations prioritaires")</commande>
  <description>Optimisation stratégique basée sur l'historique - le système est stable, passons à l'amélioration</description>
  <évolution>⛧ Niveau 2 - Optimisation tactique ⛧</évolution>
</luciform>"""
        
        print(reponse_avec_contexte)
        
        return True
    else:
        print("❌ Erreur lors du test avec mémoire enrichie")
        return False

if __name__ == "__main__":
    # Tests
    test1 = test_prompt_shadeos()
    test2 = test_avec_memoire_enrichie()
    
    print(f"\n📊 RÉSULTATS: Test 1: {'✅' if test1 else '❌'} | Test 2: {'✅' if test2 else '❌'}")
    
    if test1 and test2:
        print("🎉 Prompt ShadEOS fonctionne parfaitement !")
    else:
        print("⚠️ Des ajustements sont nécessaires")
