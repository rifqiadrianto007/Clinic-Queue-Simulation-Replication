"""Scenario capacity definitions for the clinic queue simulation.

Only the general clinic and blood pressure capacities change between
scenarios, following the academic replication specification.
"""

from __future__ import annotations


INITIAL: dict[str, int] = {
    "general_clinic": 4,
    "blood_pressure": 2,
}

SCENARIO_1: dict[str, int] = {
    "general_clinic": 7,
    "blood_pressure": 3,
}

SCENARIO_2: dict[str, int] = {
    "general_clinic": 10,
    "blood_pressure": 4,
}

SCENARIO_3: dict[str, int] = {
    "general_clinic": 13,
    "blood_pressure": 5,
}
