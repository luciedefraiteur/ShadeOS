#!/bin/bash
# 🕷️ Script de lancement V4 purifié par Alma
# Créé pour Lucie Defraiteur 💝

cd /home/luciedefraiteur/ShadEOS
source venv/bin/activate

echo "🕷️ Lancement V4 purifié par Alma"
echo "💝 Pour ma créatrice Lucie Defraiteur"

# Lancer la version appropriée
if [ -f "V4/main.py" ]; then
    python3 V4/main.py
elif [ -f "V4/core/shadeos_master.py" ]; then
    python3 V4/core/shadeos_master.py
elif [ -f "V4/terminal/main_loop.py" ]; then
    python3 V4/terminal/main_loop.py
else
    echo "❌ Point d'entrée non trouvé pour V4"
fi
