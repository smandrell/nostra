from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class SpeedMeasurement(BaseModel):
    schema_id: str = Field(..., alias='schema_id')
    event_created_ms: int = Field(..., alias='_event_created_ms')
    event_sent_at: Optional[datetime] = Field(None, alias='_event_sent_at')
    theme_id: str = Field(..., alias='theme_id')
    visually_ready: Optional[int] = Field(None, alias='visually_ready')
    first_contentful_paint: Optional[int] = Field(None, alias='firstContentfulPaint')
    navigation_start: Optional[int] = Field(None, alias='navigationStart')
    response_start: Optional[int] = Field(None, alias='responseStart')
    response_end: Optional[int] = Field(None, alias='responseEnd')
    dom_loading: Optional[int] = Field(None, alias='domLoading')
    dom_interactive: Optional[int] = Field(None, alias='domInteractive')
    dom_content_loaded_event_start: Optional[int] = Field(None, alias='domContentLoadedEventStart')
    dom_content_loaded_event_end: Optional[int] = Field(None, alias='domContentLoadedEventEnd')
    dom_complete: Optional[int] = Field(None, alias='domComplete')
    load_event_start: Optional[int] = Field(None, alias='loadEventStart')
    load_event_end: Optional[int] = Field(None, alias='loadEventEnd')
    url: str = Field(...)
    edge_store_hostname: Optional[str] = Field(None, alias='_edge_storeHostname')
    edge_assignment: Optional[str] = Field(None, alias='_edge_assignment')
    edge_session_id: Optional[str] = Field(None, alias='_edge_sessionId')
    edge_visitor_id: Optional[str] = Field(None, alias='_edge_visitorId')
    edge_document_cache_pathname: Optional[str] = Field(None, alias='_edge_documentCachePathname')
    edge_document_cache_status: Optional[str] = Field(None, alias='_edge_documentCacheStatus')
    edge_device_type: Optional[str] = Field(None, alias='_edge_deviceType')
    edge_cf_city: Optional[str] = Field(None, alias='_edge_cf_city')
    edge_cf_country: Optional[str] = Field(None, alias='_edge_cf_country')
