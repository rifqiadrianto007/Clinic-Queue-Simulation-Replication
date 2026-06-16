from __future__ import annotations
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

OUTPUT_CHARTS_DIR = Path("outputs") / "charts"

def save_bar_chart(
    results_df: pd.DataFrame,
    value_column: str,
    title: str,
    y_label: str,
    file_name: str
) -> None:
    plt.figure(figsize = (8, 5))
    plt.bar(results_df["scenario"], results_df[value_column], color = "#4C78A8")
    plt.title(title)
    plt.xlabel("Scenario")
    plt.ylabel(y_label)
    plt.grid(axis = "y", linestyle = "--", alpha = 0.4)
    plt.tight_layout()
    plt.savefig(OUTPUT_CHARTS_DIR / file_name, dpi=300)
    plt.close()


def save_grouped_bar_chart(
    results_df: pd.DataFrame,
    value_columns: list[str],
    labels: list[str],
    title: str,
    y_label: str,
    file_name: str
) -> None:
    axis = results_df.plot(
        x="scenario",
        y=value_columns,
        kind="bar",
        figsize = (9, 5),
        color = ["#4C78A8", "#F58518"]
    )
    axis.set_title(title)
    axis.set_xlabel("Scenario")
    axis.set_ylabel(y_label)
    axis.set_xticklabels(results_df["scenario"], rotation = 0)
    axis.legend(labels)
    axis.grid(axis = "y", linestyle = "--", alpha = 0.4)
    plt.tight_layout()
    plt.savefig(OUTPUT_CHARTS_DIR / file_name, dpi = 300)
    plt.close()


def generate_all_plots(results_df: pd.DataFrame) -> None:
    OUTPUT_CHARTS_DIR.mkdir(parents = True, exist_ok = True)
    if {"bp_waiting_time", "general_waiting_time"}.issubset(results_df.columns):
        save_grouped_bar_chart(
            results_df = results_df,
            value_columns = ["bp_waiting_time", "general_waiting_time"],
            labels = ["Blood Pressure", "General Clinic"],
            title = "Average Waiting Time by Scenario",
            y_label = "Average Waiting Time (minutes)",
            file_name = "waiting_time_comparison.png"
        )
        save_grouped_bar_chart(
            results_df = results_df,
            value_columns = ["bp_queue_length", "general_queue_length"],
            labels = ["Blood Pressure", "General Clinic"],
            title = "Average Queue Length by Scenario",
            y_label = "Average Queue Length (patients)",
            file_name = "queue_length_comparison.png"
        )
    else:
        save_bar_chart(
            results_df = results_df,
            value_column = "avg_waiting_time",
            title = "Average Waiting Time by Scenario",
            y_label = "Average Waiting Time (minutes)",
            file_name = "waiting_time_comparison.png"
        )
        save_bar_chart(
            results_df = results_df,
            value_column = "avg_queue_length",
            title = "Average Queue Length by Scenario",
            y_label = "Average Queue Length (patients)",
            file_name = "queue_length_comparison.png"
        )

    save_bar_chart(
        results_df = results_df,
        value_column = "patients_completed",
        title = "Throughput by Scenario",
        y_label = "Patients Completed",
        file_name = "throughput_comparison.png"
    )
