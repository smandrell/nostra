from pydantic import BaseModel


class AggregatedMetrics(BaseModel):

    mean: float
    median: float
    p75: float


class AggregatedKeyMetrics(BaseModel):

    ttfb: AggregatedMetrics
    dom_content_load_time: AggregatedMetrics
    page_load_time: AggregatedMetrics
