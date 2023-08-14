import requests


def register_client(
        wl_uid,
        partner_uid,
        client_uid,
        registered_at,
        app_platform=None,
        device_os=None,
        country_code=None,
        appsflyer_id=None,
        appsflyer_app_id=None,
        os_version=None,
        sub_id=None,
):
    body = dict(
        wl_uid=wl_uid,
        partner_uid=partner_uid,
        client_uid=client_uid,
        registered_at=registered_at,
        app_platform=app_platform,
        device_os=device_os,
        country_code=country_code,
        appsflyer_id=appsflyer_id,
        appsflyer_app_id=appsflyer_app_id,
        os_version=os_version,
        sub_id=sub_id,
    )
    return requests.request(method='POST', url='/api/clients/', json=body).json()
