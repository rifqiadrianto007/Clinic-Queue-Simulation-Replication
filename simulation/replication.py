from __future__ import annotations
from collections.abc import Generator
import random
import numpy as np
import simpy

from data.patient_generator import generate_patient
from data.service_times import get_service_time
from models.clinic import ClinicResources
from models.patient import Patient
from models.routes import ROUTES
from simulation.metrics import SimulationMetrics

# Simulation parameters
PATIENT_COUNT = 1000
SIMULATION_TIME = 480
MIN_ARRIVAL_INTERVAL = 0
MAX_ARRIVAL_INTERVAL = 2

def process_patient_route(
    env: simpy.Environment,
    clinic: ClinicResources,
    patient: Patient,
    metrics: SimulationMetrics
) -> Generator[simpy.events.Event, None, None]:
    for station_name in ROUTES[patient.route_id]:
        resource = getattr(clinic, station_name)
        service_time = get_service_time(station_name)
        queue_length = len(resource.queue)
        request_time = env.now
        if station_name in ("blood_pressure", "general_clinic"):
            metrics.record_station_queue(station_name, queue_length)

        with resource.request() as request:
            yield request

            start_service = env.now
            waiting_time = start_service - request_time
            if station_name in ("blood_pressure", "general_clinic"):
                metrics.record_station_waiting(station_name, waiting_time)

            yield env.timeout(service_time)

    metrics.patients_completed += 1

def generate_patient_arrivals(
    env: simpy.Environment,
    clinic: ClinicResources,
    patient_count: int,
    metrics: SimulationMetrics
) -> Generator[simpy.events.Event, None, None]:
    for patient_id in range(1, patient_count + 1):
        arrival_interval = np.random.exponential(scale = 1.2)
        yield env.timeout(arrival_interval)

        patient = generate_patient(patient_id = patient_id, arrival_time = env.now)
        env.process(process_patient_route(env, clinic, patient, metrics))

def run_replication(scenario: dict[str, int], seed: int) -> SimulationMetrics:
    random.seed(seed)
    np.random.seed(seed)

    env = simpy.Environment()
    clinic = ClinicResources(
        env=env,
        general_clinic_capacity=scenario["general_clinic"],
        blood_pressure_capacity=scenario["blood_pressure"]
    )
    metrics = SimulationMetrics()

    env.process(generate_patient_arrivals(env, clinic, PATIENT_COUNT, metrics))
    env.run(until = SIMULATION_TIME)
    
    return metrics
