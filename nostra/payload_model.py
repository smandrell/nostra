from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
import re


class SpeedMeasurement(BaseModel):
    schema_id: str
    event_created_ms: int = Field(..., alias='_event_created_ms')
    event_sent_at: Optional[datetime] = Field(None, alias='_event_sent_at')
    theme_id: str
    visually_ready: Optional[int] = None
    first_contentful_paint: Optional[int] = None
    navigation_start: Optional[int] = None
    response_start: Optional[int] = None
    response_end: Optional[int] = None
    dom_loading: Optional[int] = None
    dom_interactive: Optional[int] = None
    dom_content_loaded_event_start: Optional[int] = None
    dom_content_loaded_event_end: Optional[int] = None
    dom_complete: Optional[int] = None
    load_event_start: Optional[int] = None
    load_event_end: Optional[int] = None
    url: str
    edge_store_hostname: Optional[str] = Field(None, alias='_edge_storeHostname')
    edge_assignment: Optional[str] = Field(None, alias='_edge_assignment')
    edge_session_id: Optional[str] = Field(None, alias='_edge_sessionId')
    edge_visitor_id: Optional[str] = Field(None, alias='_edge_visitorId')
    edge_document_cache_pathname: Optional[str] = Field(None, alias='_edge_documentCachePathname')
    edge_document_cache_status: Optional[str] = Field(None, alias='_edge_documentCacheStatus')
    edge_device_type: Optional[str] = Field(None, alias='_edge_deviceType')
    edge_cf_city: Optional[str] = Field(None, alias='_edge_cf_city')
    edge_cf_country: Optional[str] = Field(None, alias='_edge_cf_country')


def preprocess_payload(payload):
    new_payload = {}
    for key, value in payload.items():
        # Convert camelCase to snake_case
        snake_key = re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', key)
        new_payload[snake_key.lower()] = value
    return new_payload
