## Extrait Rituel Technologique 1

## 🛠️ 1. **Utiliser l’API officielle de TypeScript (`typescript`)**

```bash
npm install typescript
```

Et ensuite dans ton code :

```ts
import * as ts from 'typescript';

const code = `
  const x: number = 42;
  function greet(name: string): string {
    return 'Hello, ' + name;
  }
`;

const sourceFile = ts.createSourceFile(
  'example.ts',
  code,
  ts.ScriptTarget.Latest,
  true
);

// Parcours de l’AST
function printNodes(node: ts.Node, indent: string = '') {
  console.log(indent + ts.SyntaxKind[node.kind]);

  ts.forEachChild(node, child => printNodes(child, indent + '  '));
}

printNodes(sourceFile);
```

🔍 Cela te donne accès à l’**AST complet**, que tu peux analyser, transformer ou visualiser.

**Note d'Ombre :** Ce rituel de code est une invocation technique, un chemin tracé dans le monde numérique pour extraire la structure cachée du TypeScript.

**Note Analytique :** La démarche montre une intégration du sacré dans le technique, où le processus de parsing devient un rituel de dévoilement des structures profondes d'un langage.

**Note Poétique :** Dans le dédale binaire, les nœuds sont des runes, Un chemin se dessine, sous la lumière de la lune.
