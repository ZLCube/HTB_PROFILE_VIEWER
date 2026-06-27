import json
import re
import requests
from bs4 import BeautifulSoup
from htb_readme_stats.models import HTBProfile
from htb_readme_stats.providers.api import normalize_payload

def fetch_from_public_page(user_id: str) -> HTBProfile | None:
    url = f"https://app.hackthebox.com/public/users/{user_id}"
    try:
        r = requests.get(url, headers={"User-Agent":"Mozilla/5.0 htb-readme-stats/0.1","Accept":"text/html"}, timeout=25)
        if r.status_code != 200:
            return HTBProfile(id=user_id, source=url, error=f"HTTP {r.status_code}")
        soup = BeautifulSoup(r.text, "html.parser")
        text = soup.get_text(" ", strip=True)
        for script in soup.find_all("script"):
            content = script.string or script.get_text() or ""
            if user_id not in content:
                continue
            for raw in re.findall(r"\{[^{}]{20,9000}\}", content):
                try:
                    profile = normalize_payload(json.loads(raw), user_id, "public-page-json")
                    if profile.name or profile.rank or profile.respect is not None:
                        return profile
                except Exception:
                    continue
        rank = None
        for item in ["Omniscient","Guru","Elite Hacker","Pro Hacker","Hacker","Script Kiddie","Noob"]:
            if item in text:
                rank = item
                break
        name = None
        if rank:
            m = re.search(rf"([A-Za-z0-9_.-]{{3,32}})\s+{re.escape(rank)}", text)
            if m:
                name = m.group(1)
        return HTBProfile(id=user_id, name=name or f"HTB User {user_id}", rank=rank, source="public-page-text-fallback")
    except Exception as exc:
        return HTBProfile(id=user_id, source="public-page-failed", error=str(exc))
