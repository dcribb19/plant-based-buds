# test_fdc.py
# Provides tests for food_data_central.py

import pytest
from food_data_central import Food, get_food_nutrients


@pytest.mark.parametrize('n, expected', [
    (170379, True),
    (173946, True),
])
def test_instance(n, expected):
    assert isinstance(get_food_nutrients(n), Food) == expected


@pytest.mark.parametrize('n, expected', [
    (170379, 'Broccoli, Raw'),
    (173946, 'Blackberries, Raw'),
])
def test_name(n, expected):
    assert get_food_nutrients(n).name == expected


@pytest.mark.parametrize('n, expected', [
    (170379, 3),
    (173946, 1),
])
def test_protein(n, expected):
    assert get_food_nutrients(n).protein == expected


@pytest.mark.parametrize('n, expected', [
    (170379, 7),
    (173946, 10),
])
def test_carbs(n, expected):
    assert get_food_nutrients(n).carbs == expected


@pytest.mark.parametrize('n, expected', [
    (170379, 0.0),
    (173946, 0.0),
])
def test_cholesterol(n, expected):
    assert get_food_nutrients(n).cholesterol == expected
