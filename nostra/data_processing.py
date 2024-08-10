from aggregated_metrics_model import AggregatedMetrics, AggregatedKeyMetrics
from payload_model import SpeedMeasurement
import statistics
import numpy as np


# Input is a list of SpeedMeasurement models
# Returns an AggregatedKeyMetrics model
def get_aggregated_key_metrics(payloads: list[SpeedMeasurement]) -> AggregatedKeyMetrics:

    ttfb_values: list[int] = []
    dom_content_load_time_values: list[int] = []
    page_load_time_values: list[int] = []

    # For each payload, calculate and store the TTFB, DOM Content Load Time, and Page Load Time
    for payload in payloads:
        if not _has_required_agg_fields(payload):
            continue

        first_byte = payload.response_start if payload.response_start else payload.response_end

        ttfb_values.append(ttfb(navigation_start=payload.navigation_start, first_byte=first_byte))
        dom_content_load_time_values.append(dom_content_load_time(dom_content_loaded_event_start=payload.dom_content_loaded_event_start, dom_content_loaded_event_end=payload.dom_content_loaded_event_end))
        page_load_time_values.append(page_load_time(navigation_start=payload.navigation_start, load_event_end=payload.load_event_end))

    ttfb_agg = AggregatedMetrics(mean=statistics.mean(ttfb_values),
                                 median=statistics.median(ttfb_values),
                                 p75=np.percentile(ttfb_values, 75))
    dom_content_load_time_agg = AggregatedMetrics(mean=statistics.mean(dom_content_load_time_values),
                                                  median=statistics.median(dom_content_load_time_values),
                                                  p75=np.percentile(dom_content_load_time_values, 75))
    page_load_time_agg = AggregatedMetrics(mean=statistics.mean(page_load_time_values),
                                           median=statistics.median(page_load_time_values),
                                           p75=np.percentile(page_load_time_values, 75))

    return AggregatedKeyMetrics(ttfb=ttfb_agg, dom_content_load_time=dom_content_load_time_agg, page_load_time=page_load_time_agg)


# Returns whether fields needed to compute AggregatedKeyMetrics are not None
def _has_required_agg_fields(payload: SpeedMeasurement):
    first_byte = payload.response_start if payload.response_start else payload.response_end
    required_fields = [first_byte, payload.navigation_start, payload.dom_content_loaded_event_start,
                       payload.dom_content_loaded_event_end, payload.load_event_end]
    return all(field is not None for field in required_fields)


# Returns time elapsed in ms
def ttfb(navigation_start: int, first_byte: int) -> int:
    return first_byte - navigation_start


# Measures DomContentLoaded event handler time, as referenced here - https://developer.mozilla.org/en-US/docs/Web/API/PerformanceNavigationTiming/domContentLoadedEventStart#measuring_domcontentloaded_event_handler_time
# Returns time elapsed in ms
def dom_content_load_time(dom_content_loaded_event_start: int, dom_content_loaded_event_end: int) -> int:
    return dom_content_loaded_event_end - dom_content_loaded_event_start


# Measure total page load time
# Returns time elasped in ms
def page_load_time(navigation_start: int, load_event_end: int) -> int:
    return load_event_end - navigation_start
