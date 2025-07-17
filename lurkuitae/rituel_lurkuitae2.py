#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import random
import time
import math
import numpy as np
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from collections import deque
import pyttsx3
import psutil
from termcolor import cprint

# === Initialisation ===
engine = pyttsx3.init()
engine.setProperty('rate', 135)

# --- Structures optimisées ---
memoire_spherique = {"SPIRALE_FINALE": None}
memoire_lineaire = deque(maxlen=1000)
phonemes = ["ka", "zu", "ra", "tho", "mi", "sha", "lu", "xe"]
current_ascii_art = ""

# === Double Rendering System ===
class HybridRenderer:
    def __init__(self):
        self.angle = 0
        self.ascii_buffer = deque(maxlen=10)  # Stocke les derniers arts ASCII
        self.ascii_texture_id = None
        self.init_3d_texture()

    def init_3d_texture(self):
        """Crée une texture OpenGL pour le rendu ASCII"""
        self.ascii_texture_id = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, self.ascii_texture_id)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, 256, 256, 0, GL_RGB, GL_UNSIGNED_BYTE, None)

    def generate_ascii_fractal(self, base):
        """Génère une fractale ASCII optimisée"""
        chars = np.array(list(" .:-=+*#%@"))
        x, y = np.meshgrid(np.arange(80), np.arange(40))
        vals = (np.sin(x*0.3 + y*0.2 + len(base)) + 1) * 4.5
        indices = (vals % len(chars)).astype(int)
        ascii_art = "\n".join("".join(row) for row in chars[indices])
        self.ascii_buffer.append(ascii_art)
        return ascii_art

    def render_ascii_to_texture(self):
        """Convertit l'ASCII en texture 3D"""
        if not self.ascii_buffer:
            return

        # Récupère le dernier ASCII art
        ascii_art = self.ascii_buffer[-1]
        lines = ascii_art.split('\n')
        
        # Crée une image RGB à partir de l'ASCII
        img_data = np.zeros((40, 80, 3), dtype=np.uint8)
        for y, line in enumerate(lines):
            for x, char in enumerate(line):
                intensity = ord(char) % 255
                color = (intensity, (intensity + 85) % 255, (intensity + 170) % 255)
                img_data[y, x] = color
        
        # Met à jour la texture
        glBindTexture(GL_TEXTURE_2D, self.ascii_texture_id)
        glTexSubImage2D(GL_TEXTURE_2D, 0, 0, 0, 80, 40, GL_RGB, GL_UNSIGNED_BYTE, img_data)

    def draw_3d_ascii(self):
        """Affiche l'ASCII art dans l'espace 3D"""
        self.render_ascii_to_texture()
        
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, self.ascii_texture_id)
        
        glBegin(GL_QUADS)
        glTexCoord2f(0, 0); glVertex3f(-1, -1, 0)
        glTexCoord2f(1, 0); glVertex3f(1, -1, 0)
        glTexCoord2f(1, 1); glVertex3f(1, 1, 0)
        glTexCoord2f(0, 1); glVertex3f(-1, 1, 0)
        glEnd()
        
        glDisable(GL_TEXTURE_2D)

# === OpenGL Setup ===
renderer = None
window = None

def init_gl(width, height):
    glClearColor(0.1, 0.1, 0.1, 1.0)
    glEnable(GL_DEPTH_TEST)
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45, width/height, 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    
    # Positionnement de la caméra
    gluLookAt(3, 2, 5, 0, 0, 0, 0, 1, 0)
    
    # Rotation continue
    glRotatef(renderer.angle, 0, 1, 0)
    renderer.angle += 0.5
    
    # Dessin de l'ASCII art en 3D
    renderer.draw_3d_ascii()
    
    glutSwapBuffers()

def create_window():
    global window, renderer
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(1200, 800)
    window = glutCreateWindow(b"Lurkuitae Hybrid Renderer")
    init_gl(1200, 800)
    renderer = HybridRenderer()
    glutDisplayFunc(display)
    glutIdleFunc(display)

# === Core Ritual Functions ===
def generate_chaos(base):
    """Génère du chaos à partir d'une base"""
    ascii_art = renderer.generate_ascii_fractal(base)
    cprint("\n🌀 Nouvelle fractale générée:", "cyan")
    print(ascii_art)
    return ascii_art

def ritual_cycle():
    """Cycle complet du rituel"""
    base = random.choice(phonemes) * 10
    for _ in range(3):
        generate_chaos(base + str(random.randint(0, 1000)))
        time.sleep(0.5)

# === Main Execution ===
if __name__ == "__main__":
    try:
        # Lancement du rendu 3D dans un thread séparé
        threading.Thread(target=create_window, daemon=True).start()
        
        # Rituel principal
        while True:
            ritual_cycle()
            time.sleep(2)
            
    except KeyboardInterrupt:
        cprint("\n🔮 Le rituel a été scellé.", "magenta")
        glutDestroyWindow(window)