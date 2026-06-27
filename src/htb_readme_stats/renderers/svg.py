from datetime import datetime, timezone
from html import escape
from typing import Any
from htb_readme_stats.models import HTBProfile
from htb_readme_stats.themes.registry import get_theme

def safe(value: Any, default: str = "—") -> str:
    return default if value is None or value == "" else escape(str(value))

def metric_box(x: int, y: int, label: str, value: Any, t: dict[str,str]) -> str:
    return f"""
  <rect x="{x}" y="{y}" width="126" height="54" rx="10" fill="{t['box']}" stroke="{t['box_border']}" />
  <text x="{x+14}" y="{y+20}" fill="{t['muted']}" font-family="Segoe UI, Ubuntu, Arial, sans-serif" font-size="11">{escape(label)}</text>
  <text x="{x+14}" y="{y+41}" fill="{t['text']}" font-family="Segoe UI, Ubuntu, Arial, sans-serif" font-size="18" font-weight="700">{safe(value)}</text>"""

def render_svg(profile: HTBProfile, theme_name: str = "purple") -> str:
    t = get_theme(theme_name)
    updated = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    profile_url = f"https://app.hackthebox.com/public/users/{safe(profile.id)}"
    return f"""<svg width="720" height="250" viewBox="0 0 720 250" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Hack The Box stats">
  <defs>
    <linearGradient id="stroke" x1="0" y1="0" x2="720" y2="250">
      <stop offset="0" stop-color="{t['accent']}"/>
      <stop offset="1" stop-color="{t['border']}" stop-opacity=".45"/>
    </linearGradient>
    <filter id="glow" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur stdDeviation="16" result="blur"/>
      <feBlend in="SourceGraphic" in2="blur"/>
    </filter>
  </defs>
  <rect x="8" y="8" width="704" height="234" rx="18" fill="{t['bg']}" stroke="url(#stroke)" stroke-width="2"/>
  <circle cx="642" cy="56" r="46" fill="{t['accent2']}" opacity=".13" filter="url(#glow)"/>
  <circle cx="642" cy="56" r="24" fill="{t['accent2']}" opacity=".25"/>
  <text x="36" y="47" fill="{t['text']}" font-family="Segoe UI, Ubuntu, Arial, sans-serif" font-size="24" font-weight="800">Hack The Box Stats</text>
  <text x="36" y="73" fill="{t['muted']}" font-family="Segoe UI, Ubuntu, Arial, sans-serif" font-size="12">{profile_url}</text>
  <text x="36" y="108" fill="{t['accent']}" font-family="Segoe UI, Ubuntu, Arial, sans-serif" font-size="28" font-weight="900">{safe(profile.name, f'HTB User {profile.id}')}</text>
  <text x="36" y="133" fill="{t['text']}" font-family="Segoe UI, Ubuntu, Arial, sans-serif" font-size="14">Rank: {safe(profile.rank)}</text>
  <text x="145" y="133" fill="{t['muted']}" font-family="Segoe UI, Ubuntu, Arial, sans-serif" font-size="14">Country: {safe(profile.country)}</text>
  {metric_box(36, 158, "Respect", profile.respect, t)}
  {metric_box(178, 158, "Points", profile.points, t)}
  {metric_box(320, 158, "User owns", profile.user_owns, t)}
  {metric_box(462, 158, "System owns", profile.system_owns, t)}
  <text x="36" y="226" fill="{t['muted']}" font-family="Segoe UI, Ubuntu, Arial, sans-serif" font-size="11">Challenges: {safe(profile.challenges)} · Bloods: {safe(profile.user_bloods)}/{safe(profile.system_bloods)} · Updated: {updated}</text>
</svg>"""
