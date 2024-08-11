from payload_model import SpeedMeasurement
import numpy as np
import pandas as pd


# Input is a list of SpeedMeasurement models
# Output is a dataframe containing aggregated metrics grouped by edge assignment
def aggregate_key_metrics_by_edge(payloads: list[SpeedMeasurement]) -> pd.DataFrame:
    # Modify DF to include new columns for key metrics
    add_in_key_metrics: pd.DataFrame = add_key_metrics_columns(payloads=payloads)
    # Group DF by edge assignment
    group_by_edge_assignment = add_in_key_metrics.groupby('edge_assignment')
    # Apply aggregate on grouped DF
    return group_by_edge_assignment.apply(_aggregate_metrics_for_group).reset_index()


def add_key_metrics_columns(payloads: list[SpeedMeasurement]) -> pd.DataFrame:
    # Filter payload, removing payloads that don't have required fields needed to compute key metrics
    filter_payload = list(filter(_has_required_agg_fields, payloads))
    # Create dataframe from filtered payloads
    df = pd.DataFrame([p.dict() for p in filter_payload])
    # Add new columns to the dataframe - key metrics columns
    df['ttfb'] = ttfb(df['navigation_start'], df['response_start'])
    df['dom_content_load_time'] = dom_content_load_time(df['dom_loading'], df['dom_content_loaded_event_start'])
    df['page_load_time'] = page_load_time(df['navigation_start'], df['load_event_end'])
    return df


def _aggregate_metrics_for_group(df) -> pd.Series:
    return pd.Series({
        'ttfb_mean': df['ttfb'].mean(),
        'ttfb_median': df['ttfb'].median(),
        'ttfb_p75': np.percentile(df['ttfb'], 75),
        'dom_content_load_time_mean': df['dom_content_load_time'].mean(),
        'dom_content_load_time_median': df['dom_content_load_time'].median(),
        'dom_content_load_time_p75': np.percentile(df['dom_content_load_time'], 75),
        'page_load_time_mean': df['page_load_time'].mean(),
        'page_load_time_median': df['page_load_time'].median(),
        'page_load_time_p75': np.percentile(df['page_load_time'], 75),
    })


# Returns whether fields needed to compute AggregatedKeyMetrics are not None
def _has_required_agg_fields(payload: SpeedMeasurement) -> bool:
    first_byte = payload.response_start if payload.response_start else payload.response_end
    required_fields = [first_byte, payload.navigation_start, payload.dom_content_loaded_event_start,
                       payload.dom_content_loaded_event_end, payload.load_event_end]
    return all(field is not None for field in required_fields)


# Returns time elapsed in ms
def ttfb(navigation_start: int, first_byte: int) -> int:
    return first_byte - navigation_start


# Measures how long it takes the DOM Content to load. I'm interpreting this as the time between when the DOM first starts
#  loading and when the DOMContentLoaded event fires.
# Returns time elapsed in ms
def dom_content_load_time(dom_loading: int, dom_content_loaded_event_start: int) -> int:
    return dom_content_loaded_event_start - dom_loading


# Measure total page load time
# Returns time elasped in ms
def page_load_time(navigation_start: int, load_event_end: int) -> int:
    return load_event_end - navigation_start
