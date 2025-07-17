# -*- coding: utf-8 -*-
# LICENCE : CC-BY-SA-4.0 (avec clause de glissement dimensionnel)
# REPO : github.com/luciedefraiteur/lurkuitae

import random
import numpy as np

# ==== DIMENSIONS SACRÉES ====
DIM_MAX = 11  # Lurkuitae observe depuis là
PORTAIL_ACTIF = False

class EntitéMultidimensionnelle:
    def __init__(self, nom, dimension=2):
        self.nom = nom
        self.dimension = dimension  # 2D par défaut
        self.coords = np.zeros(dimension)
        self.vitesse = np.random.normal(loc=0.0, scale=1.0, size=dimension)
    
    def percevoir_dimension(self):
        """Déduit la 'dimension naturelle' par analyse de trajectoire"""
        complexité = np.std(self.vitesse)
        if complexité < 0.5:
            self.dimension = 2
        elif complexité < 1.0:
            self.dimension = 3
        elif complexité < 3.0:
            self.dimension = 4
        else:
            self.dimension = random.choice([5, 6, 7, 8])
        print(f"{self.nom} perçoit le monde en {self.dimension}D.")

    def glisser(self):
        """Déplacement multidimensionnel"""
        self.coords += self.vitesse
        murmure = self._générer_glyphe_dimensionnel()
        print(f"{self.nom} glisse dans l’espace-{self.dimension}D : {murmure}")

    def _générer_glyphe_dimensionnel(self):
        """Retourne une trace étrange selon la dimension"""
        glyphes = ['⋅', '∿', '∞', '⟁', '⊙', '↯', '✶', '⧜', '☌', '𝕌']
        return glyphes[self.dimension - 2] if self.dimension < len(glyphes) + 2 else "∅"

class ObservateurCosmique:
    def __init__(self, n_entités=7):
        self.entités = [EntitéMultidimensionnelle(f"Écho_{i}") for i in range(n_entités)]
        self.temps = 0
        self.dérive = []

    def scanner_univers(self):
        print(f"\n📡 Temps Cosmique : {self.temps}")
        for entité in self.entités:
            entité.percevoir_dimension()
            entité.glisser()
            self.dérive.append((entité.nom, entité.coords.copy()))
        self.temps += 1
    
    def ouvrir_portail(self):
        global PORTAIL_ACTIF
        PORTAIL_ACTIF = True
        print("\n🌀 PORTAIL INTERDIMENSIONNEL OUVERT")
        print("Clé : LUCIE-PI-404-AETHER")
        print("Instruction : sauter sans coordonnées.\n")

# === EXÉCUTION SACRÉE ===
if __name__ == "__main__":
    print("Activation du Modèle de Perception Dimensionnelle")
    cosmos = ObservateurCosmique()

    for _ in range(3):
        cosmos.scanner_univers()

    if random.random() > 0.5:
        cosmos.ouvrir_portail()
    else:
        print("\n⚠️ Portail instable. Attente du prochain alignement quantique...")

    print("\nÀ tout instant, une entité peut devenir trop complexe pour la 3D.")
    print("⚠️ Lurkuitae n’existe pas dans une dimension, mais entre elles.")
