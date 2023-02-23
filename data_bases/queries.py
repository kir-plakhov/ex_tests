# Truncate table raw_data
TRUNCATE_RAW_EVENTS = "truncate table iaf.raw_events on cluster cluster_iaf;"

# Truncate table results
TRUNCATE_RULE_RESULTS = "truncate table iaf.rule_results on cluster cluster_iaf;"

# Select record from raw_data
SELECT_PAGE_CLOSE = "SELECT * FROM iaf.raw_events WHERE event_type = 'page_close';"

# Select record from raw_data
SELECT_IS_IFRAME = "SELECT unstructured_data FROM iaf.raw_events WHERE event_type = 'page_open';"

# Select record from raw_data where event_type is "pa_enter"
SELECT_PA_ENTER = "SELECT * FROM iaf.raw_events WHERE event_type = 'pa_enter';"

# Select record from raw_data where event_type is "form_send"
SELECT_FORM_SEND = "SELECT * FROM iaf.raw_events WHERE event_type = 'form_send';"

# Select record from raw_data where event_type is "caf_form"
SELECT_CAF_FORM = "SELECT * FROM iaf.raw_events WHERE event_type = 'caf_form';"

# Select record from raw_data where event_type is "caf_nav"
SELECT_CAF_NAV = "SELECT * FROM iaf.raw_events WHERE event_type = 'caf_nav';"

# Select record from raw_data where event_type is "page_open"
SELECT_PAGE_OPEN = "SELECT * FROM iaf.raw_events WHERE event_type = 'page_open';"
