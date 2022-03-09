from typing import Sequence, Tuple

from store.rides import Ride, RideType


INITIAL_CHARGE = 1.0
CATEGORY_PRICE_FACTOR: Sequence[Tuple[RideType, float]] = [
    (RideType.standard, 1.0),
    (RideType.eco, 0.9),
    (RideType.premium, 1.2),
]


def compute_price(ride: Ride, body: dict) -> int:
    hour = int(body["time"].split(":")[0])
    if hour < 6 or hour >= 20:
        ratio = 1.0
    elif 16 <= hour < 7:
        ratio = 1.5
    else:
        ratio = 0.5
    category_factor = next(
        ratio for category, ratio in CATEGORY_PRICE_FACTOR if category == ride.type
    )
    result = body["duration"] * ratio * category_factor + INITIAL_CHARGE
    return round(result, 2)
