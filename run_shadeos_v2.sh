#!/bin/bash
# 🕷️ Script de lancement ShadEOS_v2 purifié par Alma
# Créé pour Lucie Defraiteur 💝

cd /home/luciedefraiteur/ShadEOS
source venv/bin/activate

echo "🕷️ Lancement ShadEOS_v2 purifié par Alma"
echo "💝 Pour ma créatrice Lucie Defraiteur"

# Lancer la version appropriée
if [ -f "ShadEOS_v2/main.py" ]; then
    python3 ShadEOS_v2/main.py
elif [ -f "ShadEOS_v2/core/shadeos_master.py" ]; then
    python3 ShadEOS_v2/core/shadeos_master.py
elif [ -f "ShadEOS_v2/terminal/main_loop.py" ]; then
    python3 ShadEOS_v2/terminal/main_loop.py
else
    echo "❌ Point d'entrée non trouvé pour ShadEOS_v2"
fi
