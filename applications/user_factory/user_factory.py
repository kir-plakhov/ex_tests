import requests
from constants import COUNTRIES_FOR_DEPOSIT, url


def create_new_user():
    return requests.request('POST', url, json=None, verify=False)










