import os
from typing import Any
import requests
from htb_readme_stats.models import HTBProfile
from htb_readme_stats.providers.utils import deep_flatten, pick

APP_BASES = ["https://app.hackthebox.com", "https://www.hackthebox.com"]
API_PATHS = ["/api/v4/user/profile/basic/{id}", "/api/v4/user/profile/{id}", "/api/v4/profile/{id}"]

def _headers():
    token = os.getenv("HTB_TOKEN", "").strip()
    headers = {"User-Agent": "Mozilla/5.0 htb-readme-stats/0.1", "Accept": "application/json, text/plain, */*"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    return headers

def normalize_payload(payload: dict[str, Any], user_id: str, source: str) -> HTBProfile:
    data = payload.get("profile") or payload.get("info") or payload.get("data") or payload
    if not isinstance(data, dict):
        data = payload
    flat = deep_flatten(data)
    return HTBProfile(
        id=str(pick(data, flat, "id") or user_id),
        name=pick(data, flat, "name", "username", "user_name"),
        rank=pick(data, flat, "rank", "rank_text"),
        country=pick(data, flat, "country", "country_name"),
        avatar=pick(data, flat, "avatar", "avatar_thumb", "avatar_url"),
        respect=pick(data, flat, "respect"),
        points=pick(data, flat, "points", "rank_ownership", "ownership"),
        user_owns=pick(data, flat, "user_owns", "userOwns", "owned_users", "owns_user"),
        system_owns=pick(data, flat, "system_owns", "systemOwns", "owned_systems", "owns_system"),
        challenges=pick(data, flat, "challenges", "challenge_owns", "owned_challenges"),
        user_bloods=pick(data, flat, "user_bloods", "userBloods", "user_bloods_count"),
        system_bloods=pick(data, flat, "system_bloods", "systemBloods", "system_bloods_count"),
        source=source,
    )

def fetch_from_api(user_id: str) -> HTBProfile | None:
    last_error = None
    for base in APP_BASES:
        for path in API_PATHS:
            url = f"{base}{path.format(id=user_id)}"
            try:
                r = requests.get(url, headers=_headers(), timeout=25)
                if r.status_code != 200:
                    last_error = f"{url} HTTP {r.status_code}"
                    continue
                profile = normalize_payload(r.json(), user_id, url)
                if profile.name or profile.rank or profile.respect is not None:
                    return profile
            except Exception as exc:
                last_error = f"{url} {exc}"
    return HTBProfile(id=user_id, source="api-failed", error=last_error) if last_error else None
