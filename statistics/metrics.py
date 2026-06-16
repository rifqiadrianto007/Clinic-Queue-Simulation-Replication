"""Metric collection for selected clinic stations.

This module tracks queue and waiting measurements for stations affected by
the improvement scenarios.
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class SimulationMetrics:
    """Collect station-level simulation measurements for one replication."""

    bp_waiting_times: list[float] = field(default_factory=list)
    bp_queue_lengths: list[int] = field(default_factory=list)

    general_waiting_times: list[float] = field(default_factory=list)
    general_queue_lengths: list[int] = field(default_factory=list)

    patients_completed: int = 0

    def record_station_waiting(
        self,
        station_name: str,
        waiting_time: float,
    ) -> None:
        """Store a waiting time measurement for a tracked station."""
        if station_name == "blood_pressure":
            self.bp_waiting_times.append(waiting_time)

        elif station_name == "general_clinic":
            self.general_waiting_times.append(waiting_time)

    def record_station_queue(
        self,
        station_name: str,
        queue_length: int,
    ) -> None:
        """Store a queue length measurement for a tracked station."""
        if station_name == "blood_pressure":
            self.bp_queue_lengths.append(queue_length)

        elif station_name == "general_clinic":
            self.general_queue_lengths.append(queue_length)

    @property
    def average_bp_waiting_time(self) -> float:
        """Return average waiting time for blood pressure checks."""
        if not self.bp_waiting_times:
            return 0.0

        return sum(self.bp_waiting_times) / len(self.bp_waiting_times)

    @property
    def average_general_waiting_time(self) -> float:
        """Return average waiting time for the general clinic."""
        if not self.general_waiting_times:
            return 0.0

        return sum(self.general_waiting_times) / len(
            self.general_waiting_times
        )

    @property
    def average_bp_queue_length(self) -> float:
        """Return average queue length for blood pressure checks."""
        if not self.bp_queue_lengths:
            return 0.0

        return sum(self.bp_queue_lengths) / len(
            self.bp_queue_lengths
        )

    @property
    def average_general_queue_length(self) -> float:
        """Return average queue length for the general clinic."""
        if not self.general_queue_lengths:
            return 0.0

        return sum(self.general_queue_lengths) / len(
            self.general_queue_lengths
        )
