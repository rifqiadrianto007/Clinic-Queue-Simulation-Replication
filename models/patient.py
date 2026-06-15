"""Patient data model for the clinic queue simulation.

This module stores the minimal patient attributes needed for the route
generation stage of the simulation.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Patient:
    """Represent one synthetic patient in the clinic simulation."""

    patient_id: int
    arrival_time: float
    route_id: int
