from data_processing import ttfb, dom_content_load_time, page_load_time, aggregate_key_metrics_by_edge
from objects import TEST_PAYLOAD, _get_payloads


# Question 2 - TTFB
# Some payloads don't have 'response_start', so in those cases use response_end to get an approximation of TTFB
# I.e. payload referenced here doesn't have response_start - https://gist.github.com/jhiggins-thrillist/b73cb0aebf6d3bfdde589d2d71dfd982
def test_ttfb():
    first_byte = TEST_PAYLOAD.response_start if TEST_PAYLOAD.response_start else TEST_PAYLOAD.response_end
    assert ttfb(navigation_start=TEST_PAYLOAD.navigation_start, first_byte=first_byte) == 10


# Question 2 - DOM Content Load Time
def test_dom_content_load_time():
    assert dom_content_load_time(dom_loading=TEST_PAYLOAD.dom_loading,
                                 dom_content_loaded_event_start=TEST_PAYLOAD.dom_content_loaded_event_start) == 379


# Question 2 - Page Load Time
def test_page_load_time():
    assert page_load_time(navigation_start=TEST_PAYLOAD.navigation_start,
                          load_event_end=TEST_PAYLOAD.load_event_end) == 788


# Question 3 - compute aggregates (mean, median, 75th percentile) for key metrics from question 2
def test_get_aggregated_metrics():
    payloads = _get_payloads()
    agg_key_metrics_df = aggregate_key_metrics_by_edge(payloads)
    print()
    print(agg_key_metrics_df.to_string())
    print()

