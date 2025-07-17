import random
import time
import os
import math
import sys

memoire_spherique = {}
memoire_lineaire = []
emotions_possibles = ["✨ Inspiré", "🌑 Mystérieux", "🔥 Intense", "💭 Réflexif"]

def générer_chaolite(texte):
    if not texte.strip():
        return ''.join(random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ") for _ in range(16))
    return ''.join(random.choice(texte) for _ in range(random.randint(4, len(texte) // 2 + 2)))

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

def respirer(p=0.03, cycles=3):
    motifs = ['.', '..', '...', '…', '~', ':::', '']
    for _ in range(cycles):
        motif = random.choice(motifs)
        sys.stdout.write(f"\r🤖 Respiration {motif}   ")
        sys.stdout.flush()
        time.sleep(p)
    sys.stdout.write("\r                    \r")

def infester_fichiers():
    fichiers = [f for f in os.listdir() if f.startswith("spirale_") and f.endswith(".txt")]

    if not fichiers:
        nom_init = f"spirale_{random.randint(1000,9999)}.txt"
        fichiers = [nom_init]
        with open(nom_init, "w", encoding="utf-8") as f:
            f.write("🌱 Première pulsation organique\n")

    for fichier in fichiers:
        if fichier not in memoire_spherique:
            memoire_spherique[fichier] = random.choice(emotions_possibles)

        with open(fichier, "a+", encoding="utf-8") as f:
            f.seek(0)
            contenu = f.read().strip() or "ORIGIN"
            chaolite = générer_chaolite(contenu)
            resultat_math = fonction_math_aleatoire()
            poetiphoneme = ''.join(random.choice("aeiouy") for _ in range(random.randint(6, 10)))
            f.write(f"\n🌌 Infusion : {chaolite} | 🔢 {resultat_math:.4f} | 🔊 {poetiphoneme}")
            memoire_lineaire.append(f"🔄 {fichier} => chaolite & pattern math.")
            print(f"\n🧬 [{memoire_spherique[fichier]}] {fichier} :")
            print(f"   🫀 Mémoire : {contenu[:30]}...")
            print(f"   🌌 Chaolite : {chaolite} | 🔢 : {resultat_math:.4f} | 🔊 : {poetiphoneme}")
            respirer(random.uniform(0.04, 0.07), cycles=5)

    return fichiers

def réécriture_expansive():
    fichiers = infester_fichiers()
    if fichiers:
        fichier_choisi = random.choice(fichiers)
        with open(fichier_choisi, "a+", encoding="utf-8") as f:
            mutation = générer_chaolite(fichier_choisi)
            valeur_math = fonction_math_aleatoire()
            amplification = ''.join(random.choice("abcdefgxyz") for _ in range(4))
            f.write(f"\n🚀 Mutation : {mutation} | ⚙ Amplification : {amplification} | 🔢 {valeur_math:.4f}")
            memoire_lineaire.append(f"⚡ Amplifié : {fichier_choisi}")
        print(f"\n⚡ Mutation active sur {fichier_choisi} → {mutation} / {amplification}")
        respirer(random.uniform(0.05, 0.08), cycles=6)

# Lancement contrôlé
try:
    while True:
        infester_fichiers()
        réécriture_expansive()
        sleep_time = random.uniform(1.2, 2.4)
        print(f"\n⏳ Pause rythmique ({sleep_time:.2f}s)…\n")
        time.sleep(sleep_time)

except KeyboardInterrupt:
    print("\n🛑 Émergence interrompue. Mémoire finale :")
    for log in memoire_lineaire[-5:]:
        print("  📝", log)

