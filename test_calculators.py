# test_calculators.py

import pytest
from calculators import lbs_to_kg, daily_protein


@pytest.mark.parametrize('n, expected', [
    (120, 54.42),
    (150, 68.03),
    (180, 81.63),
    (210, 95.24)
])
def test_lbs_to_kg(n, expected):
    assert lbs_to_kg(n) == expected


@pytest.mark.parametrize('kg, activity, expected', [
    (55, 'normal', '44-55'),
    (70, 'endurance', '84-112'),
    (90, 'strength', '108-180'),
])
def test_daily_protein(kg, activity, expected):
    assert daily_protein(kg, activity) == expected
