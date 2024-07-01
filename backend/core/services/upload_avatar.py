import os
from uuid import uuid1

from core.dataclasses.user_dataclass import ProfileDataClass


def upload_avatar(instance: ProfileDataClass, filename: str) -> str:
    ext = filename.split('.')[-1]
    return os.path.join(instance.surname, 'avatar', f'{uuid1().hex}.{ext}')
