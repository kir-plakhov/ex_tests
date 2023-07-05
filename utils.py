import time
import json
from tenacity import retry, stop_after_attempt, wait_fixed


@retry(stop=stop_after_attempt(30), reraise=True, wait=wait_fixed(1))
def get_non_empty_result_from_ch(client, query):
    result = client.execute(query)
    if result:
        return result
    raise Exception('Result is an empty list')



