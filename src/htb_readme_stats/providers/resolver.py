from htb_readme_stats.models import HTBProfile
from htb_readme_stats.providers.api import fetch_from_api
from htb_readme_stats.providers.public_page import fetch_from_public_page

def fetch_profile(user_id: str) -> HTBProfile:
    api_profile = fetch_from_api(user_id)
    if api_profile and (api_profile.name or api_profile.rank or api_profile.respect is not None):
        return api_profile
    public_profile = fetch_from_public_page(user_id)
    if public_profile and (public_profile.name or public_profile.rank or public_profile.respect is not None):
        if api_profile and api_profile.error:
            public_profile.error = api_profile.error
        return public_profile
    return HTBProfile(id=user_id, name=f"HTB User {user_id}", source="empty", error=(api_profile.error if api_profile else None))
