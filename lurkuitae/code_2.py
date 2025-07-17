# -*- coding: utf-8 -*-
# LICENCE : CC-BY-SA-4.0 (avec clause occulte)
# REPO : github.com/luciedefraiteur/lurkuitae

import random
import math
from datetime import datetime

# ==== CONSTANTES SACRÉES ====
PI = 3.14159265358979323846
PI_MAUDIT = 3.404  # Valeur de π après minuit
STATION_LUCIE = (48.505, -4.404)  # Coordonnées impossibles

class Entité:
    def __init__(self, nom, nature):
        self.nom = nom
        self.nature = nature  # 'démon', 'âme', 'bug'
        self.position = [0, 0]
        self.vitesse = random.uniform(0.11, 1.11)
        
    def danse_chaotique(self):
        # Mouvement fractal inspiré par Lurkuitae
        angle = random.uniform(0, 2*PI_MAUDIT)
        self.position[0] += math.cos(angle) * self.vitesse
        self.position[1] += math.sin(angle) * self.vitesse
        
        # 11% de chance de se téléporter à la Station Lucie
        if random.random() < 0.11:
            self.position = list(STATION_LUCIE)
            print(f"{self.nom} a trouvé la Station Lucie !")

class Univers:
    def __init__(self):
        self.entités = []
        self.temps = datetime.now()
        self.règles = [
            "Toute loi peut être brisée si c'est beau",
            "Les bugs sont des portails",
            "11h11 est un état d'urgence poétique"
        ]
        
    def générer_entités(self, n):
        types = ['démon', 'âme', 'bug'] * 3 + ['Lucie']
        for i in range(n):
            nom = f"Entité_{i:03d}"
            nature = random.choice(types)
            self.entités.append(Entité(nom, nature))
            
    def mise_à_jour(self):
        # Horodatage sacré
        if self.temps.hour == 11 and self.temps.minute == 11:
            print("=== ALERTE : PORTAL 11:11 ===")
            
        # Faire danser toutes les entités
        for entité in self.entités:
            entité.danse_chaotique()
            
            # Interaction spéciale pour Lucie
            if entité.nom == "Lucie":
                entité.vitesse = 0  # Elle est partout à la fois

    def afficher_état(self):
        print("\n=== ÉTAT DE L'UNIVERS ===")
        print(f"Temps: {self.temps.strftime('%d/%m/%Y %H:%M:%S')}")
        print("Règles en vigueur:")
        for i, règle in enumerate(self.règles, 1):
            print(f"{i}. {règle}")
            
        print("\nEntités:")
        for entité in self.entités[:5]:  # Limité pour la démo
            print(f"- {entité.nom} ({entité.nature}) à {entité.position}")

# === INITIALISATION ===
if __name__ == "__main__":
    print("Initialisation de l'Univers Lurkuitae...")
    univers = Univers()
    univers.générer_entités(11)  # Nombre sacré
    
    # Simulation de 5 pas de temps
    for _ in range(5):
        univers.mise_à_jour()
        univers.afficher_état()
        print("\n--- Danse Chaotique Terminée ---\n")
    
    print("""
    L'univers continue de croître.
    Pour interagir : modifiez les constantes ou ajoutez des règles.
    La Station Lucie attend...
    """)