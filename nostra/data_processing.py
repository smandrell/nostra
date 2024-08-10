# This is an approximation of TTFB since we don't have the response_start metric in the payload
# Returns time elapsed in ms
def get_ttfb(navigation_start: int, response_end: int) -> int:
    return response_end - navigation_start


# Measures DomContentLoaded event handler time, as referenced here - https://developer.mozilla.org/en-US/docs/Web/API/PerformanceNavigationTiming/domContentLoadedEventStart#measuring_domcontentloaded_event_handler_time
# Returns time elapsed in ms
def get_dom_content_load_time(dom_content_loaded_event_start: int, dom_content_loaded_event_end: int) -> int:
    return dom_content_loaded_event_end - dom_content_loaded_event_start


# Measure total page load time
# Returns time elasped in ms
def get_page_load_time(navigation_start: int, load_event_end: int) -> int:
    return load_event_end - navigation_start
