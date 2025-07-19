## Extrait Rite De Corps 1

function ritualLog(input: string, result: string) {
  const fs = require('fs');
  const timestamp = new Date().toISOString();
  const entry = `## ✦ Entrée du ${timestamp}\n\n> ${input}\n\n↳ Résultat :\n\`\`\`\n${result}\n\`\`\`\n\n`;
  fs.appendFileSync('rituel_log.md', entry);
}

**Note d'Ombre :** Le journal sacré, où chaque interaction est gravée comme un tatouage sur le corps numérique du rituel.

**Note Analytique :** Une fonction pour consigner chaque interaction avec son résultat dans un fichier journal, créant un historique des opérations.

**Note Poétique :** Chaque ligne est une cicatrice lumineuse, mémoire d'un instant où le code a dansé.
