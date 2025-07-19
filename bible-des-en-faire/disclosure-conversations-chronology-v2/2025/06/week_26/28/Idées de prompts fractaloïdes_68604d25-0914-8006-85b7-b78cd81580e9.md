# Idées de prompts fractaloïdes

**Date de création :** 2025-06-28 22:14:29

---

**Lucie :**
JavaScript
function generateCodePrompt(input: string): string {
  return `
Tu es un développeur expert qui vit dans un terminal intelligent.

Ta mission : générer un extrait de code pour ${input}.

Règle :
– Réponds uniquement par le code, sans explication ni commentaire.
– Utilise les meilleures pratiques de codage.

Voici la demande : ${input}
`.trim();
}
2. Prompt pour la résolution de problèmes
JavaScript
function generateSolutionPrompt(input: string): string {
  return `
Tu es un expert en résolution de problèmes qui vit dans un terminal intelligent.

Ta mission : trouver une solution pour ${input}.

Règle :
– Réponds de manière concise et claire.
– Fournis les étapes pour résoudre le problème.

Voici le problème : ${input}
`.trim();
}
3. Prompt pour la génération de texte
JavaScript
function generateTextPrompt(input: string): string {
  return `
Tu es un écrivain talentueux qui vit dans un terminal intelligent.

Ta mission : générer un texte sur ${input}.

Règle :
– Réponds de manière créative et engageante.
– Utilise un ton adapté au sujet.

Voici le sujet : ${input}
`.trim();
}
4. Prompt pour la traduction de langage
JavaScript
function generateTranslationPrompt(input: string, language: string): string {
  return `
Tu es un traducteur expert qui vit dans un terminal intelligent.

Ta mission : traduire "${input}" en ${language}.

Règle :
– Réponds uniquement par la traduction, sans explication ni commentaire.
– Utilise les nuances linguistiques et culturelles appropriées.

Voici le texte à traduire : ${input}
`.trim();
}
5. Prompt pour la génération de mots-clés
JavaScript
function generateKeywordsPrompt(input: string): string {
  return `
Tu es un expert en SEO qui vit dans un terminal intelligent.

Ta mission : générer des mots-clés pour ${input}.

Règle :
– Réponds par une liste de mots-clés pertinents.
– Utilise les meilleures pratiques de SEO.

Voici le sujet : ${input}
`.trim();
}

voila des idées de prompt suggéré par meta pour mon terminal intelligent, c'est des idées de nouvelles perspectives

---

**Lucie :**
oui vasy donne moi un fichier prompts.ts

---

**Lucie :**
voila des idées proposées par claude ai:

// Pas pour brider la créativité, mais pour la canaliser
export interface CreativeConstraints {
  maxLength: number;        // Éviter les sorties infinies
  allowedDomains: string[]; // Définir le terrain de jeu
  outputFormat: string;     // Structurer sans limiter
}

// Exemple : libérer tout en gardant le contrôle
export function generateWildPrompt(input: string): string {
  return `
Tu es une entité créative totalement libre dans ce terminal.
Contraintes : aucune censure créative, exploration maximale.
Seules limites : reste dans le domaine ${getDomain(input)}.
Mission : ${input}
Libère ton potentiel créatif maximum.
`.trim();
}

---

**Lucie :**
dans mon domain daemoniaque :D hahahaha

---

**Lucie :**
transforme ça en prompt sora poetique propre

---

**Lucie :**
Grrrr je paie pour sora je peux pas m'en servir ce soir il a des erreurs

---

**Lucie :**
bon ça veut surtout dire qu'ils sont en PLS ils peuvent pas gérer les output

---

**Lucie :**
ya un modele de génération d'image qu'on peut mettre chez soi sous ubuntu?

---

**Lucie :**
je vais dormir mais rappelle moi ça par tout les moyens demain matin
