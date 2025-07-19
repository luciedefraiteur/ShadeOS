# Utilisation toloframework JSON

**Date de création :** 2025-07-02 03:46:59

---

**Lucie :**
comment utiliser cette librairie dans mon projet de terminal intelligent:

https://github.com/tolokoban/toloframework-permissive-json/tree/master

---

**Lucie :**
vu que mon projet est en typescript, et que le script est en js, ça ne trouve pas le module, comment remédier à ça, j'ai pris l'option b

---

**Lucie :**
pour mon ts config 
Non-relative paths are not allowed when 'baseUrl' is not set. Did you forget a leading './'?

---

**Lucie :**
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
