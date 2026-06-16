from __future__ import annotations
from dataclasses import dataclass, field

@dataclass
class SimulationMetrics:
    bp_waiting_times: list[float] = field(default_factory = list)
    bp_queue_lengths: list[int] = field(default_factory = list)
    general_waiting_times: list[float] = field(default_factory = list)
    general_queue_lengths: list[int] = field(default_factory = list)
    patients_completed: int = 0

    def record_station_waiting(self, station_name: str, waiting_time: float) -> None:
        if station_name == "blood_pressure":
            self.bp_waiting_times.append(waiting_time)

        elif station_name == "general_clinic":
            self.general_waiting_times.append(waiting_time)

    def record_station_queue(self, station_name: str, queue_length: int) -> None:
        if station_name == "blood_pressure":
            self.bp_queue_lengths.append(queue_length)

        elif station_name == "general_clinic":
            self.general_queue_lengths.append(queue_length)

    @property
    def average_bp_waiting_time(self) -> float:
        if not self.bp_waiting_times:
            return 0.0

        return sum(self.bp_waiting_times) / len(self.bp_waiting_times)

    @property
    def average_general_waiting_time(self) -> float:
        if not self.general_waiting_times:
            return 0.0

        return sum(self.general_waiting_times) / len(self.general_waiting_times)

    @property
    def average_bp_queue_length(self) -> float:
        if not self.bp_queue_lengths:
            return 0.0

        return sum(self.bp_queue_lengths) / len(self.bp_queue_lengths)

    @property
    def average_general_queue_length(self) -> float:
        if not self.general_queue_lengths:
            return 0.0

        return sum(self.general_queue_lengths) / len(self.general_queue_lengths)
