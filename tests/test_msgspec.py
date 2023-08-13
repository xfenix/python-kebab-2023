import typing

import pytest
import msgspec
from polyfactory.factories.msgspec_factory import MsgspecFactory

from src.models_msgspec import FakeUser


class FactoryOfFakerUsers(MsgspecFactory):
    __model__: typing.Final[FakeUser] = FakeUser


def _parse_fake_user(payload_data: dict) -> FakeUser:
    return FakeUser(**payload_data)


@pytest.mark.benchmark(
    group="simple-validation-test",
    min_rounds=3,
)
def test_msgspec_parse(benchmark):
    benchmark(_parse_fake_user, msgspec.structs.asdict(FactoryOfFakerUsers.build()))
