THEMES = {
    "purple": {"bg":"#0d1117","border":"#a855f7","accent":"#c084fc","accent2":"#7e22ce","muted":"#9ca3af","text":"#f8fafc","box":"#161b22","box_border":"#4c1d95"},
    "htb": {"bg":"#0d1117","border":"#9fef00","accent":"#9fef00","accent2":"#77c900","muted":"#9ca3af","text":"#f8fafc","box":"#161b22","box_border":"#263800"},
    "dark": {"bg":"#0d1117","border":"#30363d","accent":"#ffffff","accent2":"#64748b","muted":"#8b949e","text":"#f0f6fc","box":"#161b22","box_border":"#30363d"},
}
def get_theme(name: str | None) -> dict[str, str]:
    return THEMES.get((name or "purple").lower(), THEMES["purple"])
