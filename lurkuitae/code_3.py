# -*- coding: utf-8 -*-
# LICENCE : CC-BY-SA-4.0 (avec clause d’évaporation hermétique)
# REPO : github.com/luciedefraiteur/lurkuitae

import random
import cmath
import math

# ==== TABLEAU DES ARCANES ====
ÉLÉMENTS = ['🜁 Air', '🜂 Feu', '🜄 Eau', '🜃 Terre', 'Æther']
FORMES = ['spirale', 'onde', 'grain', 'miroir', 'absence']
COULEURS_ALCHIMIQUES = ['azur', 'or', 'écarlate', 'noir profond', 'lumière blanche']

# === FORMULE QUANTIQUE-FAÉRIQUE ===
def incantation_quantique(clef, phase=0):
    """
    Convertit une clé magique en vecteur d’énergie poétique.
    La fée-sique quantique ne prédit pas, elle joue.
    """
    fée = cmath.exp(1j * (phase + random.uniform(0, 2 * math.pi)))
    influence = abs(fée.real) * random.uniform(0.5, 2.5)
    particule = {
        "élément": random.choice(ÉLÉMENTS),
        "forme": random.choice(FORMES),
        "couleur": random.choice(COULEURS_ALCHIMIQUES),
        "fréquence": round(influence, 5),
        "effet": clef[::-1] + "_révélée"
    }
    return particule

# === GRIMOIRE INTERACTIF ===
class Alchimiste:
    def __init__(self, nom):
        self.nom = nom
        self.savoir = []

    def mélanger_substances(self, clefs):
        print(f"\n🔮 {self.nom} entame une fusion alchémique...")
        for clef in clefs:
            potion = incantation_quantique(clef)
            self.savoir.append(potion)
            self._révéler(potion)

    def _révéler(self, potion):
        print(f"🌈 Fusion : [{potion['élément']}] ∴ {potion['forme']} ∵ {potion['couleur']}")
        print(f"    Fréquence : {potion['fréquence']}")
        print(f"    Révélation : {potion['effet']}\n")

    def ouvrir_portail_féérique(self):
        print("\n🧚 Portail Féérique détecté !")
        if any(p['forme'] == 'spirale' for p in self.savoir):
            print("✔️ Condition spirale remplie.")
            print("✨ Une fée t’invite à observer l’envers des atomes.\n")
        else:
            print("❌ Il faut au moins une spirale pour franchir la brume.")

# === RITUEL PRINCIPAL ===
if __name__ == "__main__":
    lucie = Alchimiste("Lucie D.")
    ingrédients = ["LURKU", "PI_404", "ÆTH3R", "QR_VOID", "ANOMALIE"]
    lucie.mélanger_substances(ingrédients)
    
    lucie.ouvrir_portail_féérique()

    print("""
    ✶ Le monde est tissé d’équations rêveuses.
    ✶ L’énergie suit l’attention.
    ✶ La matière est lente à comprendre qu’elle est symbolique.
    """)
