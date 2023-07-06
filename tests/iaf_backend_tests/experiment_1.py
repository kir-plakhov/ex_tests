import random

import requests
from pprint import pprint

url = 'https://user-factory.test.env/api/v1/users'

body = {
    "country": None,
    "phone": None,
    "email": None,
    "language": None,
    "threshold": 300,
    "platform": "web",
    "has_deposit": False,
    "partner_link": "",
    "partner_scheme": "revenue_share",
    "create_pim_wallet": False,
    "customer_type": "individual"
}


def create_new_user():
    response = requests.post(url, json=body, headers={'accept': 'application/json'}, verify=False)

    return response.json()


partners = [["rltv", "649990b0-4429-4cb0-b3c5-c5d8052b6cb0"], ["cpl", "bb26f0f7-879a-4c80-9646-a53c34b459f4"],
            ["cpa", "d9433dc3-614c-4aeb-aae4-66d345ad2de5"], ["pim", "e4fa8717-7a26-43a0-8bf2-e51075b5cf31"],
            ["flat_fee", "93c1ecbf-a9f8-410b-bf31-1241d2a2a943"]]

os = ['iOS', 'Android', 'WindowsPhone']
countries = ['TH', 'UA', 'KE']
url_2 = "https://pda-cpa.test.env/api/clients/"
WHITELABEL = "8711b8aa-cc68-413a-8034-c2716a2ce14a"

#body_2 = {
#    "wl_uid": f"{WHITELABEL}",
#    "partner_uid": f"{random.choice(random.choice(partners)[1])}",
#    "client_uid": f"create_new_user()['user_uid']",
#    "registered_at": "2023-06-06T11:37:39.116Z",
#    "app_platform": "mobile",
#    "device_os": f"{random.choice(os)}",
#    "country_code": f"{random.choice(countries)}",
#    "appsflyer_id": "string",
#    "appsflyer_app_id": "string",
#    "os_version": "string",
#    "sub_id": "string"
#}


def create_user_via_cpa():
    response = requests.post(url_2,
                             json=body_2,
                             headers={'X-CSRFToken': 'xj993ZFk3A0mXYlPFLHoQYvErBZuPgnad2OkDiX7RxzCb0F3suzABDwAtZsmorYp',
                                      "Authorization": f"Token 5bffb051aad4c7111985db4869eef84176d152b4",
                                      'Content-Type': 'application/json'},
                             verify=False)
    print(response.content, response.status_code)


pprint(create_new_user()['user_uid'])
