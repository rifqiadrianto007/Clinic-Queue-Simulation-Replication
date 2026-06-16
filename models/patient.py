from __future__ import annotations
from dataclasses import dataclass

@dataclass
class Patient:
    patient_id: int
    arrival_time: float
    route_id: int
