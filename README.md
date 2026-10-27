# Discord Server Scraper

Selfbot simple pour extraire la liste des membres des serveurs où le compte est présent.


## Fonctionnalités

- Récupération de la liste des serveurs de l'utilisateur et son contenue
- Scraping paginé des membres (par paquets de 1000)
- Gestion automatique du rate limit (attente `Retry-After`)
- Export JSON structuré (`scrape.json`)

## Installation

1. Clone le dépôt :
   ```bash
   git clone https://github.com/shelveofficiel/selfbot.git
   cd botscrapper
   pip install -r requirements.txt
   met ton token de ton compte discord : TOKEN = ... (dans le fichier botscrapper)
   python botscrapper.py
