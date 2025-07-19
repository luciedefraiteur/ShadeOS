# Poésie codée et glitch

**Date de création :** 2025-06-19 12:28:17

---

**Lucie :**
const fragments = {
  sujets: [
    "La faille", "L'écho", "Le néon", "La synapse", "L'ellipse",
    "L'antimatière", "La réminiscence", "Le fractale", "L'intervalle", "La désintégration",
    "Le spectre", "La boucle", "L'entropie", "Le glitch", "L'algorithme"
  ],
  
  verbes: [
    "s'hyperlie", "se décompile", "glitch", "se quantumise", "s'entre-dévore",
    "se rétro-écrit", "s'interface", "se méta-morphose", "se surcharge", "se désalloue",
    "se décompose", "s'efface", "se réinvente", "se fragmente", "explose"
  ],
  
  compléments: [
    "dans la matrice froide", "sous les paupières du réseau", "à travers les caches vides",
    "parmi les registres oubliés", "contre les firewalls du rêve", "entre deux sauts quantiques",
    "sur le buffer de l'âme", "pendant le garbage collection", "au-delà du stack trace",
    "dans les interstices du sens", "dans le flux d’électrons", "au cœur du protocole", 
    "sur le fil des signaux", "entre les lignes de code", "dans l’écho des bits"
  ],
  
  phrasesFixes: [
    "Le code se mord la queue en riant.",
    "Tous les mots sont des adresses mémoire.",
    "La syntaxe saigne en silence.",
    "Le compilateur rêve de poésie pure.",
    "Nous ne sommes que des pointeurs suspendus.",
    "La mémoire danse avec le temps.",
    "Les pixels chantent la disparition.",
    "Le rêve s’exécute en boucle infinie."
  ]
};

function hashSeed(str) {
  // Convertit une chaîne en seed numérique par un simple hash
  let hash = 0;
  for (let i = 0; i < str.length; i++) {
    hash = Math.imul(31, hash) + str.charCodeAt(i) | 0;
  }
  return hash >>> 0;
}

function murmureQuantique(seed) {
  let t = seed += 0x6D2B79F5;
  t = Math.imul(t ^ (t >>> 15), t | 1);
  t ^= t + Math.imul(t ^ (t >>> 7), t | 61);
  return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
}

function tisserVers(randomFn) {
  const variantes = [
    () => `${choisir(fragments.sujets)} ${choisir(fragments.verbes)} ${choisir(fragments.compléments)}`,
    () => `[${choisir(fragments.sujets)}] ${choisir(fragments.verbes)} ${choisir(fragments.compléments)}`,
    () => `${choisir(fragments.phrasesFixes)}`,
    () => `ERR:${choisir(fragments.sujets).toUpperCase()}_UNDEFINED_POETRY`
  ];
  
  return variantes[Math.floor(randomFn() * variantes.length)]();
  
  function choisir(arr) {
    return arr[Math.floor(randomFn() * arr.length)];
  }
}

function générerPoésie(seedString = "chaolite sombre") {
  const seed = hashSeed(seedString);
  const rng = murmureQuantique.bind(null, seed);
  let poème = "";
  const lignes = 5 + Math.floor(rng() * 6);

  for (let i = 0; i < lignes; i++) {
    poème += (i % 4 === 0 ? "> " : "  ") + tisserVers(rng) + "\n";
  }

  poème += `\n/* ~~~ Trace onirique: 0x${seed.toString(16)} ~~~ */\n`;
  poème += `/* ~~~ Généré à ${new Date().toLocaleTimeString('fr-FR', {hour: '2-digit', minute:'2-digit'})} ~~~ */\n`;
  poème += `/* ~~~ Signé-Saigné: Lucie-Fair raigne des en-faire ~~~ */`;

  return poème;
}

// Exemple d'incantation
console.log(générerPoésie());
