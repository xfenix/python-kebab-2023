import time
import typing
from polyfactory.factories.pydantic_factory import ModelFactory

import pytest

from src.models_pydantic import FakeUser


class FactoryOfFakerUsers(ModelFactory):
    __model__: typing.Final[FakeUser] = FakeUser


def _parse_fake_user(payload_data: dict) -> FakeUser:
    return FakeUser(**payload_data)


@pytest.mark.benchmark(
    min_rounds=3,
)
def test_pydantic_parse(benchmark):
    benchmark(_parse_fake_user, FactoryOfFakerUsers.build().dict())
