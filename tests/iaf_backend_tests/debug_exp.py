import requests


msg = {
  "user_fingerprint": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "ip_address": "127.0.0.1",
  "timestamp": "2023-06-28T10:50:12.094Z",
  "page_url": "http://iaf-collector-dev-1.test.env/#page1",
  "location": "Europe/Minsk",
  "event_type": "pa_enter",
  "unstructured_data": {},
  "track_uid": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "user_uid": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "session_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "referrer_url": "http://iaf-collector-dev-1.test.env/form-sent.html",
  "ga_id": "",
  "device": {},
  "browser": {},
  "os": {},
  "language": "ru"
}

url = 'http://iaf-exchange.test.env/debug_user_event'

response = requests.post(url, json=msg)

print(response.status_code)
























