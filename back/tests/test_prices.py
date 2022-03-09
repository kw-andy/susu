import pytest

from prices import compute_price
from store.rides import Ride, RideType


@pytest.mark.parametrize(
    ("ride", "body", "expected"),
    (
        (
            Ride(id=1, type=RideType.eco, available=True),
            {"time": "12:23", "duration": 40},
            19.00,
        ),
        (
            Ride(id=1, type=RideType.standard, available=True),
            {"time": "12:23", "duration": 40},
            21.00,
        ),
        (
            Ride(id=1, type=RideType.premium, available=True),
            {"time": "12:23", "duration": 40},
            25.00,
        ),
        (
            Ride(id=1, type=RideType.standard, available=True),
            {"time": "17:42", "duration": 60},
            31.00,
        ),
        (
            Ride(id=1, type=RideType.standard, available=True),
            {"time": "23:38", "duration": 60},
            61.00,
        ),
    ),
)
def test_compute_prices(ride: Ride, body: dict, expected: float) -> None:
    result = compute_price(ride, body)
    assert result == expected
