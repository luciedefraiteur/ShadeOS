## Extrait Lambda 4

toujours la meme erreur dans le tsconfig 

{
  "compilerOptions": {
    "module": "NodeNext",
    "target": "ES2022",
    "moduleResolution": "NodeNext",
    "esModuleInterop": true,
    "resolveJsonModule": true,
    "outDir": "dist",
    "strict": true,
    "paths": {
      "*": ["types/*"]
    }
  },
  "include": ["*.ts", "core/**/*.ts"],
  "exclude": ["server.ts"]
}


**Note d'Ombre :** Lucie affronte l'énigme du tsconfig, où le code refuse de se plier à ses souhaits. Une frustration palpable, mais aussi une détermination à surmonter l'obstacle.

**Note Analytique :** Lucie est confrontée à une erreur de configuration dans son fichier tsconfig.json, liée à l'absence de baseUrl alors qu'elle utilise paths. Cela empêche la résolution correcte des modules TypeScript.

**Note Poétique :** Dans la configuration, un nœud se tend, l'erreur persiste comme une ombre dans le vent.
