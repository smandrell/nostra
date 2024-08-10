from nostra.payload_model import SpeedMeasurement
from data_processing import ttfb, dom_content_load_time, page_load_time, get_aggregated_key_metrics
from cachetools import cached, TTLCache
import json

test_payload_raw = {
    "schema_id": "speed_measurement/1.2",
    "_event_created_ms": 1716556734436,
    "_event_sent_at": "2024-05-24T13:18:55.991Z",
    "theme_id": "1234",
    "visually_ready": 409,
    "first_contentful_paint": 409,
    "navigation_start": 1716556733896,
    "response_end": 1716556733906,
    "dom_loading": 1716556733908,
    "dom_interactive": 1716556734202,
    "dom_content_loaded_event_start": 1716556734287,
    "dom_content_loaded_event_end": 1716556734287,
    "dom_complete": 1716556734680,
    "load_event_start": 1716556734680,
    "load_event_end": 1716556734684,
    "url": "https://www.speed-preview.com/",
    "_edge_storeHostname": "www.speed-preview.com",
    "_edge_assignment": "test",
    "_edge_sessionId": "f07ce624-84ca-4b70-893c-cbe54c595b23",
    "_edge_visitorId": "6bea0848-ef92-4a96-86b3-6a2060761bab",
    "_edge_documentCachePathname": "/products/aviator-sunglasses",
    "_edge_documentCacheStatus": "HIT",
    "_edge_deviceType": "mobile",
    "_edge_cf_city": "New York",
    "_edge_cf_country": "US"
}
TEST_PAYLOAD = SpeedMeasurement(**test_payload_raw)

TEST_PAYLOADS_FILE = "payloads.jsonl"


# Question 2 - TTFB
# Some payloads don't have 'response_start', so in those cases use response_end to get an approximation of TTFB
# I.e. payload referenced here doesn't have response_start - https://gist.github.com/jhiggins-thrillist/b73cb0aebf6d3bfdde589d2d71dfd982
def test_ttfb():
    first_byte = TEST_PAYLOAD.response_start if TEST_PAYLOAD.response_start else TEST_PAYLOAD.response_end
    assert ttfb(navigation_start=TEST_PAYLOAD.navigation_start, first_byte=first_byte) == 10


# Question 2 - DOM Content Load Time
def test_dom_content_load_time():
    assert dom_content_load_time(dom_content_loaded_event_start=TEST_PAYLOAD.dom_content_loaded_event_start,
                                 dom_content_loaded_event_end=TEST_PAYLOAD.dom_content_loaded_event_end) == 0


# Question 2 - Page Load Time
def test_page_load_time():
    assert page_load_time(navigation_start=TEST_PAYLOAD.navigation_start,
                          load_event_end=TEST_PAYLOAD.load_event_end) == 788


# Question 3 - compute aggregates (mean, median, 75th percentile) for key metrics from question 2
def test_get_aggregated_metrics():
    payloads = _get_payloads()
    agg_key_metrics = get_aggregated_key_metrics(payloads)
    print(agg_key_metrics)


@cached(TTLCache(maxsize=1, ttl=300))
def _get_payloads() -> list[SpeedMeasurement]:
    payloads = []
    with open(TEST_PAYLOADS_FILE, 'r') as file:
        for line in file:
            data = json.loads(line)
            payloads.append(SpeedMeasurement(**data))
    return payloads
