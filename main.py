"""Entry point for running the full clinic scenario experiment.

This file runs all scenario replications, prints the final comparison table,
and generates the required charts.
"""

from __future__ import annotations

from statistics.experiment import run_experiment
from visualization.plots import generate_all_plots


def main() -> None:
    """Run the experiment and generate all comparison outputs."""
    results_df = run_experiment()
    print(results_df)
    generate_all_plots(results_df)


if __name__ == "__main__":
    main()
