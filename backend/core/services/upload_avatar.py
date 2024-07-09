import os
from uuid import uuid1

from core.dataclasses.advert_dataclass import AdvertDataClass
from core.dataclasses.user_dataclass import ProfileDataClass


def upload_avatar(instance: ProfileDataClass, filename: str) -> str:
    ext = filename.split('.')[-1]
    return os.path.join(instance.surname, 'avatar', f'{uuid1().hex}.{ext}')


def upload_car_photo(instance: AdvertDataClass, filename: str) -> str:
    ext = filename.split('.')[-1]
    return os.path.join(f'{instance.id}', 'car_photo', f'{uuid1().hex}.{ext}')
