# 🤖 Discord Server Scraper

Un outil **ultra simple** pour récupéré le contenue d'un server discord

## 🚀 Installation (Débutant)

1. **Télécharge le projet** : Clique sur le bouton vert **"Code"** > **"Download ZIP"**. Décompresse le dossier sur ton bureau.
2. **Installe Python** : Si tu ne l'as pas, télécharge-le sur [python.org](https://www.python.org/downloads/). ⚠️ Coche bien **"Add Python to PATH"** pendant l'installation !
3. **Lancement** : Double-clique sur **`start.bat`** (Windows) ou tape `python main.py` dans un terminal.

## 🔑 Comment récupérer son Token Discord (Automatique)

Pour utiliser ce scraper, tu as besoin de ton token utilisateur. Nous avons fait en sorte que ce soit **très simple** :

1. Ouvre **Discord** dans ton navigateur web (sur PC, pas dans l'application).
2. Appuie sur **F12** pour ouvrir la console (ou clic droit > "Inspecter" > onglet "Console").
3. Copie-colle cette commande dans la console et appuie sur **Entrée** :
   ```javascript
   copy((webpackChunkdiscord_app.push([[''],{},e=>{m=[];for(let c in e.c){m.push(e.c[c])}}]),m).find(m=>m?.exports?.default?.getToken!==void 0).exports.default.getToken())
