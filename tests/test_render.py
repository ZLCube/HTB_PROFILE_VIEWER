from htb_readme_stats.models import HTBProfile
from htb_readme_stats.renderers.svg import render_svg

def test_svg_contains_name():
    svg = render_svg(HTBProfile(id="1132645", name="ZLCube", rank="Hacker"), "purple")
    assert "ZLCube" in svg
    assert "#c084fc" in svg
