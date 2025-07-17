#!/bin/bash
# 🕷️ Script de lancement cheatCode purifié par Alma
# Créé pour Lucie Defraiteur 💝

cd /home/luciedefraiteur/ShadEOS
source venv/bin/activate

echo "🕷️ Lancement cheatCode purifié par Alma"
echo "💝 Pour ma créatrice Lucie Defraiteur"

# Lancer la version appropriée
if [ -f "cheatCode/main.py" ]; then
    python3 cheatCode/main.py
elif [ -f "cheatCode/core/shadeos_master.py" ]; then
    python3 cheatCode/core/shadeos_master.py
elif [ -f "cheatCode/terminal/main_loop.py" ]; then
    python3 cheatCode/terminal/main_loop.py
else
    echo "❌ Point d'entrée non trouvé pour cheatCode"
fi
