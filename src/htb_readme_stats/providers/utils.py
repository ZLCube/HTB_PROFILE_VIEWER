from collections.abc import Mapping
from typing import Any

def deep_flatten(obj: Any) -> dict[str, Any]:
    out = {}
    def walk(x):
        if isinstance(x, Mapping):
            for k, v in x.items():
                lk = str(k).lower()
                if lk not in out and not isinstance(v, (dict, list, tuple)):
                    out[lk] = v
                walk(v)
        elif isinstance(x, (list, tuple)):
            for item in x:
                walk(item)
    walk(obj)
    return out

def pick(data: dict[str, Any], flat: dict[str, Any], *keys: str) -> Any:
    lowered = {str(k).lower(): v for k, v in data.items()}
    for key in keys:
        lk = key.lower()
        if key in data and data[key] not in (None, ""):
            return data[key]
        if lk in lowered and lowered[lk] not in (None, ""):
            return lowered[lk]
        if lk in flat and flat[lk] not in (None, ""):
            return flat[lk]
    return None
