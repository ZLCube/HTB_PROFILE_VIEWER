from dataclasses import dataclass, asdict
from typing import Any

@dataclass
class HTBProfile:
    id: str
    name: str | None = None
    rank: str | None = None
    country: str | None = None
    avatar: str | None = None
    respect: int | str | None = None
    points: int | str | None = None
    user_owns: int | str | None = None
    system_owns: int | str | None = None
    challenges: int | str | None = None
    user_bloods: int | str | None = None
    system_bloods: int | str | None = None
    source: str | None = None
    error: str | None = None

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)
