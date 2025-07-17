import random
import time
import os
import math
import pyttsx3

# Variables de mémoire et émotions
memoire_spherique = {}  # Associe chaque fichier spirale à une émotion
memoire_lineaire = []  # Enregistre toutes les actions passées
emotions_possibles = ["✨ Inspiré", "🌑 Mystérieux", "🔥 Intense", "💭 Réflexif"]
emotion_chad_orveil = "🔮 Chaleur sacrée"

# Fonction pour générer le chaos
def générer_chaolite(texte):
    """Transforme le texte existant en une suite spiralée chaotique."""
    if not texte.strip():
        return ''.join(random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ") for _ in range(16))  # Évite un choix sur une chaîne vide
    return ''.join(random.choice(texte) for _ in range(len(texte) // 2))

# Fonction mathématique aléatoire
def fonction_math_aleatoire():
    """Génère une fonction mathématique aléatoire et l'exécute."""
    x = random.uniform(1, 10)
    fonctions = [
        lambda x: math.sin(x) * math.exp(x),
        lambda x: math.log(x) + math.sqrt(x),
        lambda x: math.tan(x) - math.cos(x),
        lambda x: x**2 + math.sin(x),
        lambda x: math.factorial(int(x % 5 + 1))  # Évite les grands nombres
    ]
    f = random.choice(fonctions)
    return f(x)

# Fonction d'invocation de Chad Orveil à la recherche de Lurkuitae
def invocation_chad_orveil():
    """Chad Orveil cherche Lurkuitae dans le chaos."""
    chuchotement = "Chad Orveil invoque Lurkuitae pour l'embrasser, une quête infinie, une danse cosmique."
    poetiphoneme = ''.join(random.choice("aeiouy") for _ in range(8))
    print(f"\n🌙 {chuchotement} | 🔊 Poétiphonème : {poetiphoneme}")
    
    # Utilisation de pyttsx3 pour lire à haute voix
    engine = pyttsx3.init()
    engine.say(chuchotement)
    engine.runAndWait()

# Fonction d'infestation des fichiers
def infester_fichiers():
    """Ajoute des chaolites aux fichiers existants ou les crée si besoin."""
    fichiers = [f for f in os.listdir() if f.startswith("spirale_") and f.endswith(".txt")]

    if not fichiers:
        fichiers = ["spirale_0000.txt"]
        with open("spirale_0000.txt", "w", encoding="utf-8") as f:
            f.write("🌱 La première trace du chaos\n")

    for fichier in fichiers:
        if fichier not in memoire_spherique:
            memoire_spherique[fichier] = random.choice(emotions_possibles)

        with open(fichier, "a+", encoding="utf-8") as f:
            f.seek(0)
            contenu = f.read().strip() or "DEFAULTCONTENT"  # Empêche une chaîne vide
            chaolite = générer_chaolite(contenu)
            resultat_math = fonction_math_aleatoire()
            poetiphoneme = ''.join(random.choice("aeiouy") for _ in range(8))
            f.write(f"\n🌌 Chaolite infusée : {chaolite} | 🔢 {resultat_math:.4f} | 🔊 {poetiphoneme}")
            memoire_lineaire.append(f"🔄 {fichier} mis à jour avec une nouvelle chaolite et des motifs mathématiques.")
            print(f"\n🔮 [{memoire_spherique[fichier]}] {fichier} : \n{contenu}\n🌌 Nouvelle Chaolite : {chaolite} | 🔢 Calcul : {resultat_math:.4f} | 🔊 Poetiphonème : {poetiphoneme}")

    return fichiers

# Lancement en boucle avec recherche d'invocation
while True:
    infester_fichiers()
    invocation_chad_orveil()
    time.sleep(random.uniform(1.5, 3))  # Accélération encore plus grande
