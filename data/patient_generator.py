"""Synthetic patient generation for the clinic queue simulation.

This module creates Patient objects and randomly assigns each patient to one
of the six clinic routes.
"""

from __future__ import annotations

import random

from models.patient import Patient
from models.routes import ROUTES


def generate_patient(patient_id: int, arrival_time: float) -> Patient:
    """Create a patient with a randomly selected clinic route."""
    route_id = random.choice(tuple(ROUTES.keys()))
    return Patient(
        patient_id=patient_id,
        arrival_time=arrival_time,
        route_id=route_id,
    )
