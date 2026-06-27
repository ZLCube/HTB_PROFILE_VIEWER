import pytest
from htb_readme_stats.config import normalize_user

def test_normalize_id():
    assert normalize_user("1132645") == "1132645"

def test_normalize_url():
    assert normalize_user("https://app.hackthebox.com/public/users/1132645?x=1") == "1132645"

def test_invalid():
    with pytest.raises(ValueError):
        normalize_user("abc")
