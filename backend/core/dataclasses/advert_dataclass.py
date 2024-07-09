from dataclasses import dataclass
from datetime import datetime


@dataclass
class AdvertDataClass:
    id: int
    name: str
    info: str
    status: str
    edit_attempts: int
    views: int
    region: str


