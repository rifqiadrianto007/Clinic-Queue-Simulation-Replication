from __future__ import annotations
from pathlib import Path
import pandas as pd

from scenarios.config import INITIAL, SCENARIO_1, SCENARIO_2, SCENARIO_3
from statistics.metrics import SimulationMetrics
from statistics.replication import run_replication

REPLICATION_SEEDS = (100, 101, 102, 103, 104)
OUTPUT_DATA_PATH = Path("outputs") / "data" / "experiment_results.csv"
SCENARIOS: dict[str, dict[str, int]] = {
    "INITIAL": INITIAL,
    "SCENARIO_1": SCENARIO_1,
    "SCENARIO_2": SCENARIO_2,
    "SCENARIO_3": SCENARIO_3
}

def summarize_replications(
    scenario_name: str,
    replication_metrics: list[SimulationMetrics],
) -> dict[str, float | int | str]:
    replication_count = len(replication_metrics)
    patients_completed = sum(
        metrics.patients_completed for metrics in replication_metrics
    ) / replication_count

    return {
        "scenario": scenario_name,
        "bp_waiting_time": sum(
            metrics.average_bp_waiting_time
            for metrics in replication_metrics
        ) / replication_count,
        "bp_queue_length": sum(
            metrics.average_bp_queue_length
            for metrics in replication_metrics
        ) / replication_count,
        "general_waiting_time": sum(
            metrics.average_general_waiting_time
            for metrics in replication_metrics
        ) / replication_count,
        "general_queue_length": sum(
            metrics.average_general_queue_length
            for metrics in replication_metrics
        ) / replication_count,
        "patients_completed": int(
            patients_completed
        )
    }

def run_experiment() -> pd.DataFrame:
    rows: list[dict[str, float | int | str]] = []
    for scenario_name, scenario in SCENARIOS.items():
        replication_metrics = []
        for seed in REPLICATION_SEEDS:
            metric = run_replication(
                scenario=scenario,
                seed=seed,
            )

            print(
                scenario_name,
                seed,
                metric.average_bp_waiting_time,
                metric.average_general_waiting_time,
                metric.average_bp_queue_length,
                metric.average_general_queue_length,
                metric.patients_completed,
            )

            replication_metrics.append(metric)
        
        rows.append(summarize_replications(scenario_name, replication_metrics))

    results_df = pd.DataFrame(
        rows,
        columns=[
            "scenario",
            "bp_waiting_time",
            "bp_queue_length",
            "general_waiting_time",
            "general_queue_length",
            "patients_completed"
        ]
    )

    OUTPUT_DATA_PATH.parent.mkdir(parents = True, exist_ok = True)
    results_df.to_csv(OUTPUT_DATA_PATH, index = False)
    
    return results_df
