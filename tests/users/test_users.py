import pytest
from src.baseclasses.response import Response
from src.schemas.user import User


@pytest.mark.production
@pytest.mark.development
def test_getting_users_list(get_users):
    Response(get_users).assert_status_code(200).validate(User)


@pytest.mark.production
@pytest.mark.skip('Functional is fixing')
def test_another(make_number):
    print(make_number)


@pytest.mark.development
@pytest.mark.parametrize('first_value, second_value, result', [
    (1, 2, 3),
    (-1, -2, -3),
    (-1, 2, 1),
    ('b', -2, None),
    ('b', 'b', None)
])
def test_calculator(first_value, second_value, result, calculate):
    assert calculate(first_value, second_value) == result
