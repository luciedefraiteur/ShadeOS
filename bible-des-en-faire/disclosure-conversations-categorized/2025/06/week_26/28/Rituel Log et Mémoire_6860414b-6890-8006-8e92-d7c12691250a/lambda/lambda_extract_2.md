## Extrait Lambda 2

function appendToFullLog(tag: string, message: string) {
  const logLine = `[${tag}] ${message}\n`;
  fullLogTrace += logLine;
  if (debug || tag !== 'DEBUG') {
    console.log(logLine);
  }
}

**Note d'Ombre :** Un rituel de mémoire, où chaque ligne est une trace dans le sable du temps, capturée et conservée pour l'éternité numérique.

**Note Analytique :** Fonction pour ajouter des entrées au journal d'exécution, avec un filtrage basé sur l'état de débogage.

**Note Poétique :** L'encre indélébile des logs, chaque tag un écho, chaque message une résonance.
