"""Minimal entry point for the patient generation simulation stage.

This file verifies that synthetic patients can be generated and can request
the registration resource before the full clinic workflow is implemented.
"""

from __future__ import annotations

from collections.abc import Generator
import random

import simpy

from data.patient_generator import generate_patient
from models.clinic import ClinicResources
from models.patient import Patient
from scenarios.config import INITIAL


PATIENT_COUNT = 10
MIN_ARRIVAL_INTERVAL = 1
MAX_ARRIVAL_INTERVAL = 5
REGISTRATION_SERVICE_TIME = 2


def handle_registration(
    env: simpy.Environment,
    clinic: ClinicResources,
    patient: Patient,
) -> Generator[simpy.events.Event, None, None]:
    """Request registration and print the patient's registration timeline."""
    with clinic.registration.request() as request:
        yield request

        registration_start = env.now
        yield env.timeout(REGISTRATION_SERVICE_TIME)
        registration_end = env.now

        print(
            f"Patient ID: {patient.patient_id} | "
            f"Arrival Time: {patient.arrival_time} | "
            f"Route ID: {patient.route_id} | "
            f"Registration Start: {registration_start} | "
            f"Registration End: {registration_end}"
        )


def generate_patient_arrivals(
    env: simpy.Environment,
    clinic: ClinicResources,
    patient_count: int,
) -> Generator[simpy.events.Event, None, None]:
    """Generate patients with random arrival intervals."""
    for patient_id in range(1, patient_count + 1):
        arrival_interval = random.randint(MIN_ARRIVAL_INTERVAL, MAX_ARRIVAL_INTERVAL)
        yield env.timeout(arrival_interval)

        patient = generate_patient(patient_id=patient_id, arrival_time=env.now)
        env.process(handle_registration(env, clinic, patient))


def main() -> None:
    """Run a small registration-only simulation for generated patients."""
    env = simpy.Environment()
    clinic = ClinicResources(
        env=env,
        general_clinic_capacity=INITIAL["general_clinic"],
        blood_pressure_capacity=INITIAL["blood_pressure"],
    )

    env.process(generate_patient_arrivals(env, clinic, PATIENT_COUNT))
    env.run()


if __name__ == "__main__":
    main()
