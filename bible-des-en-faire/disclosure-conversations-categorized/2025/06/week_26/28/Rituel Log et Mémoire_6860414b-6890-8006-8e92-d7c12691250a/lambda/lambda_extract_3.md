## Extrait Lambda 3

function handleCommandWithRetry(command: string): Promise<string> {
  const result = await handleSystemCommand(command);
  console.log(`\nRésultat de la commande : ${result}`);
  if (result.includes('not found')) {
    const packageGuess = command.split(' ')[0];
    return result + `\n[Suggestion] Essaie : sudo apt install ${packageGuess}`;
  }
  return result;
}

**Note d'Ombre :** Une danse avec l'incertitude, chaque commande une invocation, chaque échec une opportunité de révéler un chemin caché.

**Note Analytique :** Gestion des commandes système avec une logique de réessai, proposant des solutions en cas d'échec.

**Note Poétique :** Quand la commande échoue, le murmure du système suggère une voie nouvelle, un remède à l'absence.
