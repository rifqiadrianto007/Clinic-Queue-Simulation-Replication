from __future__ import annotations
import random
from models.patient import Patient
from models.routes import ROUTES

ROUTE_WEIGHTS: dict[int, float] = {
    1: 0.10,
    2: 0.35,
    3: 0.20,
    4: 0.15,
    5: 0.10,
    6: 0.10
}

def generate_patient(
    patient_id: int,
    arrival_time: float
) -> Patient:
    route_id = random.choices(
        population = list(ROUTE_WEIGHTS.keys()),
        weights = list(ROUTE_WEIGHTS.values()),
        k = 1
    )[0]

    return Patient(
        patient_id = patient_id,
        arrival_time = arrival_time,
        route_id = route_id
    )