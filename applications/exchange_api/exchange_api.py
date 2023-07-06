import requests


def exchange_api(method: str, url: str, data: dict = None):
    return requests.request(method, url=url, json=data)
