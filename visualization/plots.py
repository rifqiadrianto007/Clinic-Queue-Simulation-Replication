"""Academic chart generation for clinic scenario comparison.

This module creates clean Matplotlib charts from experiment results so the
figures can be used in academic reports.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


plt.style.use("ggplot")

OUTPUT_CHARTS_DIR = Path("outputs") / "charts"
FIGURE_SIZE = (10, 6)
FIGURE_DPI = 300
BAR_WIDTH = 0.36
COLORS = {
    "blood_pressure": "#2F6B9A",
    "general_clinic": "#E07A5F",
    "throughput": "#3D7D4F",
}
SCENARIO_LABELS = {
    "INITIAL": "Initial",
    "SCENARIO_1": "Scenario 1",
    "SCENARIO_2": "Scenario 2",
    "SCENARIO_3": "Scenario 3",
}


def prepare_results(results_df: pd.DataFrame) -> pd.DataFrame:
    """Return a plotting copy with readable scenario labels."""
    prepared_df = results_df.copy()
    prepared_df["scenario_label"] = prepared_df["scenario"].replace(SCENARIO_LABELS)
    return prepared_df


def format_axis(axis: plt.Axes, title: str, y_label: str) -> None:
    """Apply consistent academic chart formatting."""
    axis.set_title(title, fontsize=14, fontweight="bold", pad=14)
    axis.set_xlabel("Scenario", fontsize=11)
    axis.set_ylabel(y_label, fontsize=11)
    axis.tick_params(axis="x", labelrotation=0)
    axis.grid(axis="y", linestyle="--", linewidth=0.8, alpha=0.45)
    axis.grid(axis="x", visible=False)
    axis.spines["top"].set_visible(False)
    axis.spines["right"].set_visible(False)


def add_value_labels(axis: plt.Axes, decimal_places: int = 2) -> None:
    """Add numeric labels above every bar in a chart."""
    for container in axis.containers:
        axis.bar_label(
            container,
            fmt=f"%.{decimal_places}f",
            padding=4,
            fontsize=9,
        )


def save_figure(file_name: str) -> None:
    """Save the active Matplotlib figure to the charts output directory."""
    OUTPUT_CHARTS_DIR.mkdir(parents=True, exist_ok=True)
    plt.tight_layout()
    plt.savefig(OUTPUT_CHARTS_DIR / file_name, dpi=FIGURE_DPI, bbox_inches="tight")
    plt.close()


def save_grouped_bar_chart(
    results_df: pd.DataFrame,
    value_columns: tuple[str, str],
    labels: tuple[str, str],
    title: str,
    y_label: str,
    file_name: str,
) -> None:
    """Create a grouped bar chart for blood pressure and general clinic metrics."""
    prepared_df = prepare_results(results_df)
    x_positions = range(len(prepared_df))

    figure, axis = plt.subplots(figsize=FIGURE_SIZE)
    axis.bar(
        [position - BAR_WIDTH / 2 for position in x_positions],
        prepared_df[value_columns[0]],
        width=BAR_WIDTH,
        label=labels[0],
        color=COLORS["blood_pressure"],
    )
    axis.bar(
        [position + BAR_WIDTH / 2 for position in x_positions],
        prepared_df[value_columns[1]],
        width=BAR_WIDTH,
        label=labels[1],
        color=COLORS["general_clinic"],
    )

    axis.set_xticks(list(x_positions))
    axis.set_xticklabels(prepared_df["scenario_label"])
    format_axis(axis, title, y_label)
    axis.legend(frameon=True, facecolor="white", edgecolor="#CCCCCC")
    add_value_labels(axis)
    figure.subplots_adjust(top=0.88)
    save_figure(file_name)


def save_single_bar_chart(
    results_df: pd.DataFrame,
    value_column: str,
    title: str,
    y_label: str,
    file_name: str,
) -> None:
    """Create a single-series scenario comparison bar chart."""
    prepared_df = prepare_results(results_df)

    figure, axis = plt.subplots(figsize=FIGURE_SIZE)
    axis.bar(
        prepared_df["scenario_label"],
        prepared_df[value_column],
        color=COLORS["throughput"],
        width=0.55,
    )

    format_axis(axis, title, y_label)
    add_value_labels(axis, decimal_places=0)
    figure.subplots_adjust(top=0.88)
    save_figure(file_name)


def generate_all_plots(results_df: pd.DataFrame) -> None:
    """Generate waiting time, queue length, and throughput comparison charts."""
    save_grouped_bar_chart(
        results_df=results_df,
        value_columns=("bp_waiting_time", "general_waiting_time"),
        labels=("Blood Pressure Check", "General Clinic"),
        title="Average Waiting Time Comparison Across Scenarios",
        y_label="Average Waiting Time (minutes)",
        file_name="waiting_time_comparison.png",
    )
    save_grouped_bar_chart(
        results_df=results_df,
        value_columns=("bp_queue_length", "general_queue_length"),
        labels=("Blood Pressure Check", "General Clinic"),
        title="Average Queue Length Comparison Across Scenarios",
        y_label="Average Queue Length (patients)",
        file_name="queue_length_comparison.png",
    )
    save_single_bar_chart(
        results_df=results_df,
        value_column="patients_completed",
        title="Throughput Comparison Across Scenarios",
        y_label="Patients Completed",
        file_name="throughput_comparison.png",
    )
