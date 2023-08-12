import decimal
from pydantic import BaseModel, ValidationError
from enum import Enum, IntEnum


class GenderType(IntEnum):
    male = 1
    female = 2
    ventilator = 3
    borg = 4
    terminator = 5
    valkyrie = 6
    titanic_monster = 7
    fancy_red_fox = 8
    android = 9
    caramel_mocha_frappuccino = 10
    semi_conductor_wolf = 11


class FakeUser(BaseModel):
    client_fio: str
    phone_of_mama: int
    card_balance: decimal.Decimal
