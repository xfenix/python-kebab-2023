import datetime
import pathlib
import typing
import decimal
from pydantic import BaseModel

from ._common import GenderType


class GenderRules(BaseModel):
    schedule: str
    fluent: bool
    gender_type: GenderType


class GiganticFakeMonster(BaseModel):
    lovely_name: str
    damage_area_sq_km: int
    probability_of_fire_resist: float  # very low
    intergalatic_powers: set[str]
    samosbor_pk2312_uvbshn123: typing.Any


class FakeUser(BaseModel):
    client_fio: str
    client_gender: tuple[GenderRules, ...]
    phone_of_mama: int
    card_balance: decimal.Decimal
    probability_of_fail: float
    ready_to_move_on: bool
    traits: tuple[
        typing.Literal["immortality", "omniprecense", "omnipower", "superspeed"], ...
    ]
    music_he_hates: frozenset[
        typing.Literal["kallyanni_rap", "hookah_pop", "rock", "jazz", "folk"]
    ]
    lovely_cat_names: list[str]
    monsters_he_likes: list[GiganticFakeMonster]
    avatar_path: pathlib.Path
    time_of_birth: datetime.datetime
    current_level: int | str
