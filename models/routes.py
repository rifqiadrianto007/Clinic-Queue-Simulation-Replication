from __future__ import annotations

ROUTES: dict[int, tuple[str, ...]] = {
    1: (
        "registration",
        "blood_pressure",
        "dental_clinic",
        "cashier",
        "pharmacy",
        "medicine_pickup"
    ),
    2: (
        "registration",
        "blood_pressure",
        "general_clinic",
        "cashier",
        "pharmacy",
        "medicine_pickup"
    ),
    3: (
        "registration",
        "blood_pressure",
        "general_clinic",
        "treatment_room",
        "cashier",
        "pharmacy",
        "medicine_pickup"
    ),
    4: (
        "registration",
        "dental_clinic",
        "cashier",
        "pharmacy",
        "medicine_pickup"
    ),
    5: (
        "registration",
        "general_clinic",
        "pharmacy",
        "medicine_pickup"
    ),
    6: (
        "registration",
        "general_clinic",
        "treatment_room",
        "pharmacy",
        "medicine_pickup"
    )
}
