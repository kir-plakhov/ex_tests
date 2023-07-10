import time
import random
from pprint import pprint
from random import randint
from uuid import uuid4

from message_factory import IAFSourceMessage


p_url = 'http://iaf-collector-dev-2.test.env/#page1'

r_url= 'http://iaf-collector-dev-2.test.env/#page1'

event_types = ['page_open', 'caf_form', 'caf_nav', 'scroll', 'page_close', 'form_send', 'go_to_pa']


def generate_ip_address():
    return str(randint(0, 255)) + '.' + str(randint(0, 255)) + '.' + str(randint(0, 255)) + '.' + str(randint(0, 255))


def generate_msg():
    obj = IAFSourceMessage(
        track_uid=str(uuid4()),
        user_uid=str(uuid4()),
        session_uid=str(uuid4()),
        google_id='339000000.1111111733',
        ip_address=str(generate_ip_address()),
        user_fingerprint='728693b64341fc324fb99d79f45dfd12',
        page_url=p_url,
        event_type=random.choice(event_types),
        referrer_url=r_url,
        unstructured_data={},
        # server_timestamp=time.time_ns(),
        timestamp=time.time_ns(),
        location='Asia/Nicosia',
        language='ru'
    )

    msg = obj.model_dump_json()

    return msg


print(generate_msg())
