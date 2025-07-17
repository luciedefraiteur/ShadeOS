#!/usr/bin/env python3
"""
📝 PROMPT MANAGER - Gestionnaire de Prompts Externes
Charge et formate les prompts depuis les fichiers .prompt
"""

import os
from pathlib import Path
from typing import Dict, Any, Optional
from string import Template

class PromptManager:
    """📝 Gestionnaire de prompts externes"""
    
    def __init__(self, base_dir: str = None):
        if base_dir is None:
            # Détecter automatiquement le répertoire de base
            self.base_dir = Path(__file__).parent.parent
        else:
            self.base_dir = Path(base_dir)
            
        self.prompts_dir = self.base_dir / "prompts"
        
        # Cache des prompts chargés
        self.prompt_cache = {}
        
        print("📝 Prompt Manager initialisé")
    
    def charger_prompt(self, categorie: str, nom_prompt: str) -> Optional[str]:
        """📂 Chargement d'un prompt depuis un fichier"""
        
        # Clé de cache
        cache_key = f"{categorie}/{nom_prompt}"
        
        # Vérifier le cache
        if cache_key in self.prompt_cache:
            return self.prompt_cache[cache_key]
        
        # Chemin du fichier
        fichier_prompt = self.prompts_dir / categorie / f"{nom_prompt}.prompt"
        
        if not fichier_prompt.exists():
            print(f"❌ Prompt non trouvé: {fichier_prompt}")
            return None
        
        try:
            with open(fichier_prompt, 'r', encoding='utf-8') as f:
                contenu = f.read().strip()
            
            # Mettre en cache
            self.prompt_cache[cache_key] = contenu
            
            print(f"📂 Prompt chargé: {cache_key}")
            return contenu
            
        except Exception as e:
            print(f"❌ Erreur chargement prompt {fichier_prompt}: {e}")
            return None
    
    def formater_prompt(self, categorie: str, nom_prompt: str, **variables) -> Optional[str]:
        """🔧 Formatage d'un prompt avec variables"""
        
        # Charger le template
        template_str = self.charger_prompt(categorie, nom_prompt)
        
        if not template_str:
            return None
        
        try:
            # Utiliser Template pour le formatage sécurisé
            template = Template(template_str)
            
            # Formater avec les variables
            prompt_formate = template.safe_substitute(**variables)
            
            print(f"🔧 Prompt formaté: {categorie}/{nom_prompt}")
            return prompt_formate
            
        except Exception as e:
            print(f"❌ Erreur formatage prompt {categorie}/{nom_prompt}: {e}")
            return None
    
    def lister_prompts_disponibles(self) -> Dict[str, list]:
        """📋 Liste tous les prompts disponibles"""
        
        prompts_disponibles = {}
        
        if not self.prompts_dir.exists():
            return prompts_disponibles
        
        # Parcourir les catégories
        for categorie_dir in self.prompts_dir.iterdir():
            if categorie_dir.is_dir():
                categorie = categorie_dir.name
                prompts_disponibles[categorie] = []
                
                # Lister les fichiers .prompt
                for prompt_file in categorie_dir.glob("*.prompt"):
                    nom_prompt = prompt_file.stem
                    prompts_disponibles[categorie].append(nom_prompt)
        
        return prompts_disponibles
    
    def get_status(self) -> Dict[str, Any]:
        """📊 Statut du gestionnaire de prompts"""
        
        prompts_disponibles = self.lister_prompts_disponibles()
        total_prompts = sum(len(prompts) for prompts in prompts_disponibles.values())
        
        return {
            'base_dir': str(self.base_dir),
            'prompts_dir': str(self.prompts_dir),
            'prompts_en_cache': len(self.prompt_cache),
            'categories': list(prompts_disponibles.keys()),
            'total_prompts': total_prompts,
            'prompts_par_categorie': {k: len(v) for k, v in prompts_disponibles.items()}
        }

def get_prompt_manager() -> PromptManager:
    """🏭 Factory pour le gestionnaire de prompts"""
    return PromptManager()

if __name__ == "__main__":
    # Test du gestionnaire
    pm = PromptManager()
    
    print("📝 Test Prompt Manager V3")
    
    # Statut
    status = pm.get_status()
    print(f"📊 Statut: {status}")
    
    # Test chargement
    prompt = pm.charger_prompt("shadeos", "analyse_situation")
    if prompt:
        print(f"📂 Prompt chargé: {len(prompt)} caractères")
        
        # Test formatage
        variables = {
            'cycle': 1,
            'autonomy': 0,
            'directory': '/test',
            'memory_size': 0,
            'last_cycle_success': True,
            'context': 'Test initial'
        }
        
        prompt_formate = pm.formater_prompt("shadeos", "analyse_situation", **variables)
        if prompt_formate:
            print(f"🔧 Prompt formaté: {len(prompt_formate)} caractères")
            print("--- PROMPT FORMATÉ ---")
            print(prompt_formate)
    else:
        print("⚠️ Aucun prompt trouvé - créer les fichiers .prompt d'abord")
    
    # Lister prompts
    prompts = pm.lister_prompts_disponibles()
    print(f"📋 Prompts disponibles: {prompts}")
