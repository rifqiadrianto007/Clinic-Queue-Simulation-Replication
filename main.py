from __future__ import annotations
from statistics.experiment import run_experiment
from visualization.plots import generate_all_plots

def main() -> None:
    results_df = run_experiment()
    print(results_df)
    generate_all_plots(results_df)


if __name__ == "__main__":
    main()
