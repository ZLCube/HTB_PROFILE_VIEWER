import argparse, json
from pathlib import Path
from htb_readme_stats.config import normalize_user
from htb_readme_stats.providers.resolver import fetch_profile
from htb_readme_stats.renderers.svg import render_svg

def main() -> None:
    parser = argparse.ArgumentParser(description="Generate static HTB README stats SVG")
    parser.add_argument("--user", required=True, help="HTB public user ID or profile URL")
    parser.add_argument("--theme", default="purple", help="purple, htb, dark")
    parser.add_argument("--output-dir", default="public/htb", help="Output directory")
    args = parser.parse_args()

    user_id = normalize_user(args.user)
    output = Path(args.output_dir)
    output.mkdir(parents=True, exist_ok=True)
    profile = fetch_profile(user_id)
    svg = render_svg(profile, args.theme)
    (output / f"{user_id}.svg").write_text(svg, encoding="utf-8")
    (output / f"{user_id}.json").write_text(json.dumps(profile.to_dict(), indent=2, ensure_ascii=False), encoding="utf-8")
    (output / "card.svg").write_text(svg, encoding="utf-8")
    (output / "profile.json").write_text(json.dumps(profile.to_dict(), indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Generated HTB card for {user_id}")
    if profile.error:
        print(f"Warning: {profile.error}")
