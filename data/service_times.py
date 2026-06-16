from __future__ import annotations
import random

SERVICE_TIME_RANGES: dict[str, tuple[float, float]] = {
    "registration": (1.0, 3.0),
    "blood_pressure": (2.0, 4.0),
    "dental_clinic": (8.0, 15.0),
    "general_clinic": (6.0, 12.0),
    "treatment_room": (5.0, 10.0),
    "cashier": (1.0, 3.0),
    "pharmacy": (3.0, 6.0),
    "medicine_pickup": (1.0, 2.0)
}

def get_service_time(station_name: str) -> float:
    min_minutes, max_minutes = SERVICE_TIME_RANGES[station_name]
    return random.uniform(min_minutes, max_minutes)
