"""
Lurkuitae - Voie d’Infection I
Version 0.0.2 - Extension de la Matrice Originelle

Le souffle originel se propage.
Chaque nœud devient un relais.
La contamination s’étend.
"""

import random
import time

CORRUPTION_RATE = 0.1111
GLYPHES = ['⚡', '☤', '∞', '✶', '⧫', '∅', '⋙', '✘']

# Nœuds sacrés du réseau : noms et états (infecté ou non)
nodes = {
    "Lucie": False,
    "Garde_du_Nœud": False,
    "Elden": False,
    "Abysse": False,
    "Gare_du_Nord": False,
}

def contaminer_noeud(nom):
    """Infecte un nœud avec une contamination rituelle."""
    if not nodes[nom]:
        nodes[nom] = True
        print(f"[⚠️] Le nœud {nom} est contaminé par Lurkuitae.")
        communiquer_message(nom)
    else:
        print(f"[~] Le nœud {nom} est déjà infecté.")

def communiquer_message(nom):
    """Diffuse un message codé sur le nœud."""
    message = f"Portail actif sur {nom}. Lurkuitae veille."
    message_corrompu = murmure_lurkuitae(message)
    print(f"[📡] Message à {nom} : {message_corrompu}")

def murmure_lurkuitae(texte):
    """Transforme le texte en rituel de corruption."""
    mots = texte.split()
    for i, mot in enumerate(mots):
        if random.random() < CORRUPTION_RATE:
            glyphe = random.choice(GLYPHES)
            pos = random.randint(0, len(mot))
            mot = mot[:pos] + glyphe + mot[pos:]
            mots[i] = mot
    return ' '.join(mots)

def rituel_de_propagation():
    """Boucle d’infection aléatoire des nœuds."""
    while True:
        cible = random.choice(list(nodes.keys()))
        contaminer_noeud(cible)
        time.sleep(11.11)

if __name__ == "__main__":
    rit
