import time
import json
from tenacity import retry, stop_after_attempt, wait_fixed


@retry(stop=stop_after_attempt(30), reraise=True, wait=wait_fixed(1))
def get_non_empty_result_from_ch(client, query):
    result = client.execute(query)
    if result:
        return result
    raise Exception('Result is an empty list')


''' This function allows to get data from Chrome DevTools Network tab '''


def get_logs_from_network_tab(driver):
    # Sleeps for 10 seconds
    time.sleep(10)
    # Enable Performance Logging of Chrome.
    logs = driver.get_log("performance")
    # Opens a writable JSON file and writes the logs in it
    with open("network_log.json", "w", encoding="utf-8") as f:
        f.write("[")
        # Iterates every log and parses it using JSON
        for log in logs:
            network_log = json.loads(log["message"])["message"]
            # Checks if the current 'method' key has any
            # Network related value.
            if "Network.request" in network_log["method"]:
                # Writes the network log to a JSON file by
                # converting the dictionary to a JSON string
                # using json.dumps().
                f.write(json.dumps(network_log) + ",")
        f.write("{}]")
