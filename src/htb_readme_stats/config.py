import re

def normalize_user(value: str) -> str:
    value = (value or "").strip().rstrip("/")
    if not value:
        raise ValueError("Missing HTB user ID or profile URL")
    if "/" in value:
        value = value.split("/")[-1]
    if "?" in value:
        value = value.split("?")[0]
    if not re.fullmatch(r"\d+", value):
        raise ValueError(f"Invalid HTB user ID: {value!r}")
    return value
