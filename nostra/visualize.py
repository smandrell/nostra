import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Plots and displays histograms for each metric in 'metrics', grouped by _edge_assignment
# Input is a DF that contains payload data + key metrics (i.e. ttfb, dom_content_load_time, etc.)
def plot_histograms_for_key_metrics_by_edge(df: pd.DataFrame, metrics: list[str]):
    for metric in metrics:
        _plot_histogram_by_edge_assignment(df=df, metric=metric)


def _plot_histogram_by_edge_assignment(df: pd.DataFrame, metric: str):
    plt.figure(figsize=(10, 6))
    sns.histplot(data=df, x=metric, hue="edge_assignment", kde=True, element="step", palette="Set2")
    plt.title(f'Histogram of {metric} by edge_assignment')
    plt.xlabel(metric)
    plt.ylabel('Frequency')
    plt.show()


# Plots and displays box plots for each metric in 'metrics', grouped by _edge_assignment
# Input is a DF that contains payload data + key metrics (i.e. ttfb, dom_content_load_time, etc.)
def plot_box_for_metrics_by_edge(df: pd.DataFrame, metrics: list[str]):
    for metric in metrics:
        _plot_box_by_edge_assignment(df=df, metric=metric)


def _plot_box_by_edge_assignment(df: pd.DataFrame, metric: str):
    plt.figure(figsize=(12, 8))
    sns.boxplot(data=df, x="edge_assignment", y=metric, palette="Set3")
    plt.title(f'Boxplot of {metric} by edge_assignment')
    plt.xlabel('_edge_assignment')
    plt.ylabel(metric)
    plt.show()
