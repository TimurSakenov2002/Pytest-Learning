import pytest
from src.generators.player import Player

def _calculate(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a + b
    else:
        return None


@pytest.fixture
def calculate():
    return _calculate

@pytest.fixture
def get_player_generator():
    return Player()
