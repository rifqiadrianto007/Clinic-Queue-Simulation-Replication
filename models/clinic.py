from __future__ import annotations
import simpy

class ClinicResources:

    def __init__(
        self,
        env: simpy.Environment,
        general_clinic_capacity: int = 4,
        blood_pressure_capacity: int = 2
    ) -> None:
        self.registration = simpy.Resource(env, capacity = 1)
        self.blood_pressure = simpy.Resource(env, capacity = blood_pressure_capacity)
        self.dental_clinic = simpy.Resource(env, capacity = 2)
        self.general_clinic = simpy.Resource(env, capacity = general_clinic_capacity)
        self.treatment_room = simpy.Resource(env, capacity = 3)
        self.cashier = simpy.Resource(env, capacity = 1)
        self.pharmacy = simpy.Resource(env, capacity = 1)
        self.medicine_pickup = simpy.Resource(env, capacity = 1)

    def capacities(self) -> dict[str, int]:
        return {
            "registration": self.registration.capacity,
            "blood_pressure": self.blood_pressure.capacity,
            "dental_clinic": self.dental_clinic.capacity,
            "general_clinic": self.general_clinic.capacity,
            "treatment_room": self.treatment_room.capacity,
            "cashier": self.cashier.capacity,
            "pharmacy": self.pharmacy.capacity,
            "medicine_pickup": self.medicine_pickup.capacity
        }
