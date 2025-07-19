# AI non censurées gratuites

**Date de création :** 2025-03-06 23:16:25

---



salut chatgpt, connais tu une ai gratuite comme toi qui soit non censurée?

Salut ! Il existe quelques IA qui se veulent moins censurées que moi, mais elles ont souvent des limites aussi. Voici quelques options :

1. **MythoMax / OpenHermes / Pygmalion** – Ce sont des modèles open-source que tu peux tester sur des plateformes comme **KoboldAI** ou **Oobabooga Text Generation WebUI**.
2. **Claude (Anthropic)** – Plus souple que ChatGPT sur certains sujets, mais reste modéré.
3. **Mistral / Mixtral** – Un modèle open-source performant, trouvable sur **Hugging Face**.
4. **Janitor AI / Venus AI** – Pour les chats plus "libres", mais souvent payants.
5. **Chatbot UI avec OpenAI API** – Si tu as une clé API d’OpenAI, tu peux créer un bot avec tes propres paramètres.

Tu cherches un chatbot pour quoi exactement ?

je voudrais de l'aide pour écrire une histoire un peu perverse et erotique, voire pornographique donc il me faut une ai sans censure si tu sais m'en conseiller une

Je vois ce que tu cherches. Pour ce type de contenu, la plupart des IA grand public (comme moi) ont des restrictions. Mais voici quelques alternatives plus permissives :  

1. **KoboldAI** – Une interface permettant d’utiliser des modèles comme **MythoMax**, **Pygmalion**, et **OpenHermes**, qui sont connus pour être plus libres.  
2. **SillyTavern** – Une version améliorée de KoboldAI qui permet des interactions plus fluides et immersives.  
3. **Janitor AI** (mode non censuré) – Spécialisé dans le **RP NSFW**, avec des bots qui peuvent générer des histoires sans restriction.  
4. **Venus AI** – Un autre chatbot NSFW populaire, mais certaines fonctionnalités peuvent être payantes.  
5. **NovelAI** – Connu pour son écriture fluide et immersive, mais il faut payer pour les meilleures options.  
6. **Text Generation WebUI (Oobabooga)** – Un moyen de faire tourner des modèles comme **Mistral 7B** ou **Llama 2** en local, sans censure.  

Si tu veux quelque chose **d’open-source et gratuit**, je te conseille d’essayer **KoboldAI avec MythoMax** ou **SillyTavern** connecté à un modèle local. Tu peux les installer sur ton PC si tu as une bonne config, ou les utiliser via Google Colab.  

Tu veux un coup de main pour installer ça ou juste des conseils d’écriture pour ton histoire ?

ya t'il une d'elle qui parle français?

Oui, mais le support du français varie selon les modèles. Voici ceux qui fonctionnent bien en français pour du contenu NSFW :  

1. **Mistral 7B / Mixtral** – Open-source et performant en français, disponible via **Text Generation WebUI (Oobabooga)** ou **KoboldAI**.  
2. **Zephyr 7B** – Une variante du modèle Mistral, qui peut être utilisée avec **SillyTavern** ou **KoboldAI**.  
3. **MythoMax / OpenHermes** – Axés sur la fiction et le roleplay, mais majoritairement en anglais. Ils peuvent fonctionner en français, mais la qualité sera un peu moins fluide.  
4. **Chatbot UI avec l’API Mistral** – Tu peux brancher **Mistral AI** sur un front-end comme **SillyTavern** pour un chatbot NSFW en français.  
5. **Janitor AI / Venus AI** – Certains bots créés par la communauté sont en français, mais la majorité du contenu est anglophone.  

Si tu veux du 100 % français, **Mistral 7B / Mixtral** est la meilleure option. Il faut juste savoir comment l’installer. Tu veux que je t’explique comment faire ?

comment je fais pour utiliser sillytavern je ne comprends rien a leur site, ce n'est pas un chat comme ici

Oui, **SillyTavern** n'est pas un chatbot en ligne comme ChatGPT. C'est une interface que tu dois installer et connecter à un modèle d’IA. Je vais t’expliquer comment faire facilement.  

### 🔹 **Option 1 : Utiliser SillyTavern sur Google Colab (Facile et Gratuit)**  
Si tu ne veux pas l’installer sur ton PC, tu peux l’utiliser via Google Colab :  

1. **Va sur ce lien** : [SillyTavern Colab](https://colab.research.google.com/github/Cohee1207/SillyTavern/blob/main/colab/GPU_SillyTavern.ipynb)  
2. **Exécute les cellules** une par une (bouton "▶" en haut à gauche de chaque bloc de code).  
3. À la fin, un lien **SillyTavern** apparaîtra, clique dessus.  
4. Connecte-le à une IA (voir plus bas).  

### 🔹 **Option 2 : Installer SillyTavern sur ton PC (Plus performant, mais demande un peu plus d’effort)**  
1. **Installe Node.js** ([télécharge ici](https://nodejs.org/))  
2. **Télécharge SillyTavern** sur [GitHub](https://github.com/SillyTavern/SillyTavern) et extrais-le dans un dossier.  
3. **Ouvre un terminal (CMD sur Windows) et tape** :  
   ```bash
   cd [le chemin du dossier SillyTavern]
   npm install
   npm start
   ```
4. Une page **SillyTavern** s’ouvrira dans ton navigateur.  

---

### 🔥 **Étape suivante : Connecter une IA à SillyTavern**  
SillyTavern est juste une **interface**, il te faut un modèle d’IA derrière :  

- **Mistral 7B / Mixtral** (en français, tourne sur KoboldAI ou Oobabooga WebUI).  
- **KoboldAI** (peut être utilisé en ligne ou localement).  
- **OpenAI (GPT-4, GPT-3.5)** si tu as une clé API OpenAI.  
- **Janitor AI / Venus AI** (certains bots peuvent être branchés dessus).  

💡 **Si tu veux quelque chose de rapide**, utilise **SillyTavern sur Google Colab + un modèle Mistral 7B**.  

Tu veux que je t’aide à configurer un modèle précis ? 😊

comment je peux faire pour installer mistral si je prend la deuxieme methode

Si tu veux **installer Mistral 7B** sur ton **PC** avec **SillyTavern**, voici un guide étape par étape.  

---

### **🔹 Prérequis (Vérifie ton Matériel)**
✅ **Carte graphique (GPU) NVIDIA avec au moins 8 Go de VRAM** (RTX 3060 ou mieux recommandé)  
✅ **Au moins 16 Go de RAM** (ça peut fonctionner avec 8 Go, mais ce sera lent)  
✅ **Espace disque libre (~20 Go pour le modèle Mistral 7B)**  

Si tu n’as pas un bon PC, il vaut mieux passer par **Google Colab** (je peux aussi te guider pour ça).  

---

## **1️⃣ Installer Oobabooga (Text Generation WebUI)**
C'est l'interface qui va faire tourner **Mistral 7B** sur ton PC.  

### **Méthode simple (Installateur Windows)**
1. **Télécharge Oobabooga ici** → [TextGen WebUI Installer](https://github.com/oobabooga/installer/releases)  
2. **Lance l’installateur**, choisis un dossier d’installation et installe tout.  
3. Une fois installé, **ouvre le dossier d’installation** et lance :  
   - **`start-webui.bat`** (Windows)  
   - **`start-webui.sh`** (Linux/Mac)  

Une interface s’ouvrira dans ton navigateur.  

---

## **2️⃣ Télécharger et Charger le Modèle Mistral 7B**
Une fois que **Oobabooga WebUI** est installé :  

1. **Va dans l’onglet `Model` de l’interface WebUI**  
2. **Clique sur `Download Model`** et choisis :  
   - **`TheBloke/Mistral-7B-Instruct-v0.1-GGUF`** *(GGUF version, plus rapide sur GPU)*  
3. Attends le téléchargement (environ **7-10 Go**).  

Une fois terminé, clique sur **`Reload`**, puis sur **`Load Model`**.  

---

## **3️⃣ Connecter Mistral 7B à SillyTavern**
Maintenant que Mistral tourne dans **Oobabooga WebUI**, tu dois le lier à **SillyTavern** :  

1. **Lance Oobabooga (`start-webui.bat`) et charge Mistral**  
2. **Ouvre SillyTavern (`npm start`)**  
3. Dans SillyTavern, **va dans les paramètres (`⚙` en haut à droite)**  
4. **Va dans `Extensions` > `API`** et choisis **Oobabooga API**  
5. Mets cette URL :  
   ```
   http://127.0.0.1:5000/v1
   ```
6. Clique sur **"Connecter"**  

Et voilà ! Tu peux maintenant **chatter avec Mistral 7B dans SillyTavern** 🎉  

---

### **💡 Alternative : Utiliser Mistral sur Google Colab**
Si ton PC est trop faible, tu peux utiliser **Mistral sur Google Colab** (gratuit).  
Tu veux que je t’envoie un lien et un guide rapide pour ça ? 😊

Tu m'as expliqué ça, mais le lien de fonctionne pas, peux tu m'en fournir un autre?

 Option 1 : Utiliser SillyTavern sur Google Colab (Facile et Gratuit)
Si tu ne veux pas l’installer sur ton PC, tu peux l’utiliser via Google Colab :

Va sur ce lien : SillyTavern Colab
Exécute les cellules une par une (bouton "▶" en haut à gauche de chaque bloc de code).
À la fin, un lien SillyTavern apparaîtra, clique dessus.
Connecte-le à une IA (voir plus bas).



​Je suis désolé pour le lien précédent qui ne fonctionnait pas. Voici une méthode alternative pour utiliser **SillyTavern** via **Google Colab**, sans avoir à l'installer sur votre ordinateur.

### Étapes pour utiliser SillyTavern sur Google Colab

1. **Accédez au notebook Colab dédié :**
   - [SillyTavern - GPU.ipynb](https://colab.research.google.com/github/SillyTavern/SillyTavern/blob/release/colab/GPU.ipynb)

2. **Configurez le notebook :**
   - Ouvrez le lien ci-dessus.
   - Si vous n'avez pas de compte Google, créez-en un pour accéder à Google Colab.

3. **Exécutez les cellules du notebook :**
   - Dans le notebook, vous verrez plusieurs blocs de code appelés "cellules".
   - Pour chaque cellule, cliquez sur le bouton "▶" situé à gauche pour l'exécuter.
   - Commencez par la première cellule et progressez vers le bas, en exécutant chaque cellule une par une.

4. **Lancez SillyTavern :**
   - Après avoir exécuté toutes les cellules, recherchez un lien commençant par `https://` suivi de `.trycloudflare.com`.
   - Cliquez sur ce lien pour ouvrir l'interface de SillyTavern.

5. **Connectez SillyTavern à un modèle d'IA :**
   - Une fois dans l'interface de SillyTavern, allez dans les paramètres (icône en forme d'engrenage).
   - Sélectionnez l'option pour connecter une API ou un backend.
   - Choisissez un modèle disponible ou configurez-en un selon vos préférences.

### Remarques importantes

- **Limitations de Google Colab :** La version gratuite de Google Colab offre des ressources limitées et des sessions temporaires. Pour des performances accrues et des sessions plus longues, envisagez de souscrire à [Google Colab Pro](https://colab.research.google.com/signup).

- **Modèles d'IA compatibles :** Assurez-vous que le modèle d'IA que vous souhaitez utiliser est compatible avec SillyTavern et peut être exécuté sur les ressources fournies par Google Colab.

- **Sauvegarde de votre travail :** Les sessions Colab ne sont pas permanentes. Sauvegardez régulièrement votre travail pour éviter toute perte de données.

Si vous rencontrez des difficultés lors de ces étapes ou si vous avez des questions supplémentaires, n'hésitez pas à me le faire savoir. Je suis là pour vous aider. 