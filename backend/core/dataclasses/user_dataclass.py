from dataclasses import dataclass
from datetime import datetime


@dataclass
class ProfileDataClass:
    id: int
    name: str
    surname: str
    age: int
    phone: str
    created_at: datetime
    updated_at: datetime


@dataclass
class UserDataClass:
    id: int
    email: str
    password: str
    is_active: bool
    is_premium: bool
    is_staff: bool
    is_superuser: bool
    created_at: datetime
    updated_at: datetime
    profile: ProfileDataClass
