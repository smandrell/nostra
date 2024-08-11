from data_processing import add_key_metrics_columns
from visualize import plot_histograms_for_key_metrics_by_edge, plot_box_for_metrics_by_edge
from objects import _get_payloads


PAYLOADS = _get_payloads()
METRICS_TO_PLOT = ['ttfb', 'dom_content_load_time', 'page_load_time']


# Question 5 - generates histograms of core web vitals for each edge assignment
def test_plot_histograms_for_key_metrics_by_edge():
    # Get dataframe of aggregated metrics (TTFB, etc.)
    df = add_key_metrics_columns(PAYLOADS)
    plot_histograms_for_key_metrics_by_edge(df=df, metrics=METRICS_TO_PLOT)


# Question 5 - generates box plots of core web vitals for each edge assignment
def test_plot_box_for_metrics_by_edge():
    # Get dataframe of aggregated metrics (TTFB, etc.)
    df = add_key_metrics_columns(PAYLOADS)
    plot_box_for_metrics_by_edge(df=df, metrics=METRICS_TO_PLOT)
