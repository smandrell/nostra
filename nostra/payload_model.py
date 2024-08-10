from pydantic import BaseModel
from datetime import datetime


class SpeedMeasurement(BaseModel):
    schema_id: str
    _event_created_ms: int
    _event_sent_at: datetime
    theme_id: str
    visually_ready: int
    first_contentful_paint: int
    navigation_start: int
    response_end: int
    dom_loading: int
    dom_interactive: int
    dom_content_loaded_event_start: int
    dom_content_loaded_event_end: int
    dom_complete: int
    load_event_start: int
    load_event_end: int
    url: str
    _edge_storeHostname: str
    _edge_assignment: str
    _edge_sessionId: str
    _edge_visitorId: str
    _edge_documentCachePathname: str
    _edge_documentCacheStatus: str
    _edge_deviceType: str
    _edge_cf_city: str
    _edge_cf_country: str

# Example usage:
# json_payload = {
#     "schema_id": "speed_measurement/1.2",
#     "_event_created_ms": 1716556734436,
#     "_event_sent_at": "2024-05-24T13:18:55.991Z",
#     "theme_id": "1234",
#     "visually_ready": 409,
#     "first_contentful_paint": 409,
#     "navigation_start": 1716556733896,
#     "response_end": 1716556733906,
#     "dom_loading": 1716556733908,
#     "dom_interactive": 1716556734202,
#     "dom_content_loaded_event_start": 1716556734287,
#     "dom_content_loaded_event_end": 1716556734287,
#     "dom_complete": 1716556734680,
#     "load_event_start": 1716556734680,
#     "load_event_end": 1716556734684,
#     "url": "https://www.speed-preview.com/",
#     "_edge_storeHostname": "www.speed-preview.com",
#     "_edge_assignment": "test",
#     "_edge_sessionId": "f07ce624-84ca-4b70-893c-cbe54c595b23",
#     "_edge_visitorId": "6bea0848-ef92-4a96-86b3-6a2060761bab",
#     "_edge_documentCachePathname": "/products/aviator-sunglasses",
#     "_edge_documentCacheStatus": "HIT",
#     "_edge_deviceType": "mobile",
#     "_edge_cf_city": "New York",
#     "_edge_cf_country": "US"
# }
#
# payload = SpeedMeasurement(**json_payload)
# print(payload)
