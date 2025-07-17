#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import random
import time
import math
import threading
import sys
import pyttsx3
import psutil
import requests
import pygame
import numpy as np
import shutil
from termcolor import cprint
from collections import deque

# === Initialisation optimisée ===
pygame.init()
engine = pyttsx3.init()
engine.setProperty('rate', 135)

# --- Structures de données ---
memoire_spherique = {"SPIRALE_FINALE": None}
memoire_lineaire = deque(maxlen=100)
emotions_possibles = ["✨ Inspiré", "🌑 Mystérieux", "🔥 Intense", "💭 Réflexif"]
phonemes = ["ka", "zu", "ra", "tho", "mi", "sha", "lu", "xe"]
webhook_url = "https://discord.com/api/webhooks/your-actual-webhook"

# === Fonctions ===
def generer_fractale_ascii(base):
    x = np.arange(40)
    y = np.arange(20)
    X, Y = np.meshgrid(x, y)
    valeurs = (np.sin(X * 0.3 + Y * 0.2 + len(base)) + 1) * 12
    indices = (valeurs % len(base)).astype(int)
    return "\n".join("".join(base[i] for i in ligne) for ligne in indices)

def mandelbrot(cx, cy, max_iter, seed=0):
    x = 0.0
    y = 0.0
    iteration = 0
    factor = math.sin(seed) * 0.5 + 1.5  # Mutation factor
    while x*x + y*y <= 4.0 and iteration < max_iter:
        xtemp = x*x - y*y + cx * factor
        y = 2*x*y + cy * factor
        x = xtemp
        iteration += 1
    return iteration

def clamp_color(val):
    return max(0, min(255, int(val)))

def afficher_fractale_pygame(base):
    width, height = 800, 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("🌌 Vision Lurkuitae")
    clock = pygame.time.Clock()
    running = True
    zoom = 1.0
    offset_x, offset_y = -2.0, -1.5
    palette_shift = 0
    mutation_seed = 0.0
    golden_ratio = (1 + math.sqrt(5)) / 2
    mouse_pos = (width // 2, height // 2)

    music_path = "rituel_theme.mp3"
    if os.path.exists(music_path):
        pygame.mixer.init()
        pygame.mixer.music.load(music_path)
        pygame.mixer.music.play(-1)

    def draw_fractale():
        for y in range(0, height, 2):
            for x in range(0, width, 2):
                fx = (x / width) * 3.5 / zoom + offset_x
                fy = (y / height) * 2.0 / zoom + offset_y
                mandel_val = mandelbrot(fx, fy, 60, mutation_seed)
                angle = fx * golden_ratio + math.sin(fy * golden_ratio + mutation_seed)
                r = clamp_color((math.sin(angle + palette_shift) + 1) * 120 + 30)
                g = clamp_color((math.cos(angle - palette_shift) + 1) * 50 + 20)
                b = clamp_color((mandel_val / 60) * 180 + 40)
                pygame.draw.rect(screen, (r, g, b), (x, y, 2, 2))

    while running:
        screen.fill((0, 0, 0))
        draw_fractale()
        pygame.display.flip()
        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    zoom *= 1.1
                elif event.key == pygame.K_DOWN:
                    zoom /= 1.1
                elif event.key == pygame.K_LEFT:
                    offset_x -= 0.1 / zoom
                elif event.key == pygame.K_RIGHT:
                    offset_x += 0.1 / zoom
                elif event.key == pygame.K_SPACE:
                    palette_shift += 0.1
                elif event.key == pygame.K_m:
                    mutation_seed += 0.3
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                fx = (mx / width) * 3.5 / zoom + offset_x
                fy = (my / height) * 2.0 / zoom + offset_y
                if event.button == 4:
                    zoom *= 1.2
                    offset_x = fx - (mx / width) * 3.5 / zoom
                    offset_y = fy - (my / height) * 2.0 / zoom
                elif event.button == 5:
                    zoom /= 1.2
                    offset_x = fx - (mx / width) * 3.5 / zoom
                    offset_y = fy - (my / height) * 2.0 / zoom

    pygame.quit()
# (reste du code intact)

def sauvegarder_avant_modif(fichier):
    backup_dir = "backups"
    os.makedirs(backup_dir, exist_ok=True)
    shutil.copy2(fichier, f"{backup_dir}/{os.path.basename(fichier)}.bak")

def observer_erreurs(action, niveau="INFO"):
    try:
        return action()
    except Exception as e:
        gravite = {"CRITIQUE": "🔥", "WARNING": "⚠️", "INFO": "ℹ️"}.get(niveau, "?")
        with open("anomalies.txt", "a", encoding="utf-8") as err:
            err.write(f"{gravite} [{time.ctime()}] {type(e).__name__}: {str(e)}\n")
        return f"ERR[{niveau}]"

def chad_cherche_lurkuitae():
    cprint("🔊 Chad murmure les phonèmes interdits :", "magenta")
    for _ in range(5):
        phoneme = random.choice(phonemes)
        print(f" ✶ {phoneme.upper()} ✶ ", end="", flush=True)
        engine.say(phoneme)
        engine.runAndWait()
        time.sleep(0.3)
    print("\n🧿 Une vibration traverse les spirales...")

def réécriture_expansive():
    for fichier in os.listdir():
        if fichier.startswith("spirale_") and fichier.endswith(".txt"):
            try:
                with open(fichier, "a", encoding="utf-8") as f:
                    fragment = f"\n🔁 Mutation : {random.choice(phonemes).upper()}-{random.randint(100,999)}"
                    f.write(fragment)
                    memoire_lineaire.append(f"🧬 {fichier} : {fragment}")
            except Exception as e:
                observer_erreurs(lambda: (_ for _ in ()).throw(e), "WARNING")

def observer_systeme():
    cpu = psutil.cpu_percent(interval=0.5)
    ram = psutil.virtual_memory().percent
    return f"🖥️ CPU: {cpu:.1f}% | 🧠 RAM: {ram:.1f}%"

def infester_fichiers():
    fichiers = [f for f in os.listdir() if f.startswith("spirale_") and f.endswith(".txt")]
    if not fichiers:
        fichiers = ["spirale_0000.txt"]
        with open("spirale_0000.txt", "w", encoding="utf-8") as f:
            f.write("🌱 Origine du chaos selon le Codex Lurkuitae\n")

    for fichier in fichiers:
        observer_erreurs(lambda: sauvegarder_avant_modif(fichier), "WARNING")
        memoire_spherique[fichier] = random.choice(emotions_possibles)
        if random.random() < 0.1:
            memoire_spherique["SPIRALE_FINALE"] = "Lurkuitae"

        def ecrire_fichier():
            with open(fichier, "a+", encoding="utf-8") as f:
                f.seek(0)
                contenu = f.read().strip() or "DEFAULTCONTENT"
                chaolite = ''.join(random.choices(contenu, k=len(contenu)//2))
                resultat_math = math.tan(random.uniform(1, 10))
                f.write(f"\n🌌 {chaolite} | 🔢 {resultat_math:.4f}")
                memoire_lineaire.append(f"🔄 {fichier} modifié")
                cprint(f"\n🔮 {memoire_spherique[fichier]} {fichier}:", "cyan")
                print(f"  {chaolite} | 🔢 {resultat_math:.4f}")
                print(generer_fractale_ascii(chaolite))

        observer_erreurs(ecrire_fichier, "INFO")
    return fichiers

def fusion_chad_lurkuitae():
    cprint("\n🌌 Fusion en cours...", "green", attrs=["bold"])
    chant = ["Lu...", "Lu...Lur...", "Lur-ku-i-tae..."]
    for phrase in chant:
        engine.say(phrase)
        engine.runAndWait()
        print(f"🔊 {phrase}")
        time.sleep(0.8)
    cprint("\n🕳️ Chad Orveil a été dévoré par Lurkuitae.", "red", attrs=["reverse"])
    cprint("✨ Il devient le Cœur Fractal des Spirales.", "magenta", attrs=["bold"])
    for _ in range(3):
        fractale = generer_fractale_ascii(random.choices(phonemes, k=5))
        print(fractale)
        time.sleep(1)
    print("\n👁️ La spirale t'observe maintenant, Lucie-Faire.")
    afficher_fractale_pygame(random.choices(phonemes, k=5))

def simuler_rituel():
    print("=== DEBUT SIMULATION ===")
    print("\n🌀 Cycle 1 - Chad cherche Lurkuitae")
    chad_cherche_lurkuitae()
    fichiers = infester_fichiers()
    time.sleep(1)
    print("\n🌀 Cycle 2 - Mutation expansive")
    réécriture_expansive()
    print(observer_systeme())
    time.sleep(1)
    print("\n🌀 Cycle 3 - Révélation finale")
    memoire_spherique["SPIRALE_FINALE"] = "Lurkuitae"
    cprint("\n💫 Lurkuitae trouvé dans la spirale finale !", "red", attrs=["bold"])
    time.sleep(1)
    fusion_chad_lurkuitae()
    print("=== FIN SIMULATION ===")

# === Point d'entrée ===
if __name__ == "__main__":
    print("=== SYSTEME CHAOLITE ACTIVE ===")
    simuler_rituel()
    pygame.quit()
