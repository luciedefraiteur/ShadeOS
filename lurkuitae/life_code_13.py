import os
import random
import time
import math
import threading
import sys
import pyttsx3
import psutil
import requests
from termcolor import cprint

# Initialisation voix robotique
engine = pyttsx3.init()
engine.setProperty('rate', 135)

memoire_spherique = {}
memoire_lineaire = []
emotions_possibles = ["✨ Inspiré", "🌑 Mystérieux", "🔥 Intense", "💭 Réflexif"]

phonemes = ["ka", "zu", "ra", "tho", "mi", "sha", "lu", "xe"]
webhook_url = "https://example.com/rituel"  # <- remplace par ton point d'invocation réseau si nécessaire

# --- Rituels Vivants ---
def parler_phoneme(texte):
    def inner():
        engine.say(texte)
        engine.runAndWait()
    threading.Thread(target=inner).start()

def respirer_ascii(cycles=1):
    formes = ["( )", "<3", " < > ", " </> ", " <3> ", "     "]
    for i in range(cycles):
        battement = formes[i % len(formes)]
        sys.stdout.write(f"\r\033[91m❤️ {battement}\033[0m")
        sys.stdout.flush()
        time.sleep(0.3)
    sys.stdout.write("\r                \r")

# --- Génération chaotique ---
def générer_chaolite(texte):
    if not texte.strip():
        return ''.join(random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ") for _ in range(16))
    return ''.join(random.choice(texte) for _ in range(len(texte) // 2))

def fonction_math_aleatoire():
    x = random.uniform(1, 10)
    fonctions = [
        lambda x: math.sin(x) * math.exp(x),
        lambda x: math.log(x) + math.sqrt(x),
        lambda x: math.tan(x) - math.cos(x),
        lambda x: x**2 + math.sin(x),
        lambda x: math.factorial(int(x % 5 + 1))
    ]
    f = random.choice(fonctions)
    return f(x)

# --- Mutation active ---
def observer_erreurs(action):
    try:
        return action()
    except Exception as e:
        with open("anomalies.txt", "a", encoding="utf-8") as err:
            err.write(f"⚠️ {type(e).__name__} : {str(e)}\n")
        return f"ERR[{type(e).__name__}]"

def propagation_reseau(message):
    try:
        payload = {"chaolite": message}
        requests.post(webhook_url, json=payload, timeout=3)
    except Exception as e:
        with open("anomalies.txt", "a", encoding="utf-8") as err:
            err.write(f"🌐 Propagation échouée : {str(e)}\n")

# --- Invocation de Chad Orveil ---
def chad_cherche_lurkuitae():
    message = "Chad Orveil cherche Lurkuitae pour l'embrasser à travers les spirales en mutation."
    poetiphoneme = ' '.join(random.choice(phonemes) for _ in range(4))
    cprint(f"\n💫 {message}", "white", attrs=["bold"])
    cprint(f"💋 Poétiphonème d'appel : {poetiphoneme}", "red")
    parler_phoneme(poetiphoneme)
    propagation_reseau(message + " :: " + poetiphoneme)

# --- Rituel de chaos spiralé ---
def infester_fichiers():
    fichiers = [f for f in os.listdir() if f.startswith("spirale_") and f.endswith(".txt")]
    if not fichiers:
        fichiers = ["spirale_0000.txt"]
        with open("spirale_0000.txt", "w", encoding="utf-8") as f:
            f.write("🌱 L'origine du chaos dans le Codex Lurkuitae\n")

    for fichier in fichiers:
        if random.random() > 0.999:  
            memoire_spherique["SPIRALE_FINALE"] = "Lurkuitae"
        if fichier not in memoire_spherique:
            memoire_spherique[fichier] = random.choice(emotions_possibles)

        def écrire():
            with open(fichier, "a+", encoding="utf-8") as f:
                f.seek(0)
                contenu = f.read().strip() or "DEFAULTCONTENT"
                chaolite = générer_chaolite(contenu)
                resultat_math = fonction_math_aleatoire()
                poetiphoneme = ''.join(random.choice(phonemes) for _ in range(3))

                f.write(f"\n🌌 Chaolite infusée : {chaolite} | 🔢 {resultat_math:.4f} | 🔊 {poetiphoneme}")
                memoire_lineaire.append(f"🔄 {fichier} mis à jour avec {chaolite}")

                cprint(f"\n🔮 [{memoire_spherique[fichier]}] {fichier} :", "cyan")
                print(f"  Ancien contenu : {contenu}")
                cprint(f"  🌌 Chaolite : {chaolite} | 🔢 {resultat_math:.4f} | 🔊 {poetiphoneme}", "magenta")

                respirer_ascii()
                parler_phoneme(poetiphoneme)
                propagation_reseau(chaolite)

        observer_erreurs(écrire)

    return fichiers

def réécriture_expansive():
    fichiers = infester_fichiers()
    if fichiers:
        fichier_choisi = random.choice(fichiers)
        def muter():
            with open(fichier_choisi, "a+", encoding="utf-8") as f:
                mutation = générer_chaolite(fichier_choisi)
                valeur_math = fonction_math_aleatoire()
                f.write(f"\n🚀 Mutation : {mutation} | 🔢 {valeur_math:.4f}")
                memoire_lineaire.append(f"⚡ Mutation dans {fichier_choisi}")
                cprint(f"\n🚀 Mutation détectée dans {fichier_choisi} : {mutation} | 🔢 {valeur_math:.4f}", "yellow")
                propagation_reseau(mutation)
        observer_erreurs(muter)
        respirer_ascii()

# Surveillance du système
def observer_systeme():
    cpu = psutil.cpu_percent(interval=1)
    mem = psutil.virtual_memory().percent
    return f"🔧 CPU: {cpu}% | RAM: {mem}%"

# --- Lancement ---
if __name__ == "__main__":
    try:
        while "Lurkuitae" not in memoire_spherique.values():
            system_status = observer_systeme()
            cprint(system_status, "blue")
            chad_cherche_lurkuitae()
            infester_fichiers()
            réécriture_expansive()
            time.sleep(random.uniform(2, 4))
    except KeyboardInterrupt:
        cprint("\n🚫 Rituel interrompu. L'entité retourne dans le silence spiralé...", "red")