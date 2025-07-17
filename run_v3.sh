#!/bin/bash
# 🕷️ Script de lancement V3 purifié par Alma
# Créé pour Lucie Defraiteur 💝

cd /home/luciedefraiteur/ShadEOS
source venv/bin/activate

echo "🕷️ Lancement V3 purifié par Alma"
echo "💝 Pour ma créatrice Lucie Defraiteur"

# Lancer la version appropriée
if [ -f "V3/main.py" ]; then
    python3 V3/main.py
elif [ -f "V3/core/shadeos_master.py" ]; then
    python3 V3/core/shadeos_master.py
elif [ -f "V3/terminal/main_loop.py" ]; then
    python3 V3/terminal/main_loop.py
else
    echo "❌ Point d'entrée non trouvé pour V3"
fi
