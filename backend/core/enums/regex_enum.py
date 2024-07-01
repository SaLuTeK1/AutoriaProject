from enum import Enum


class RegexEnum(Enum):
    NAME = (
        r'^[A-Z][a-zA-Z]{1,19}$',
        'First letter uppercase'
    )
    PASSWORD = (
        r'^(?=.*\d)(?=.*[A-Z])(?=.*[a-z])(?=.*[^\w\d\s:])([^\s]){8,16}$',
        [
            'Password must contain 1 number(0 - 9)',
            'Password must contain 1 uppercase letters',
            'Password must contain 1 lowercase letters',
            'Password must contain 1 non - alpha numeric number',
            'Password is 8 - 16 characters with no space',
        ]
    )

    def __init__(self, pattern: str, msg: str | list[str]):
        self.pattern = pattern
        self.msg = msg