import requests


def ipay88Complete(payment_number, headers):
    path = "https://gateway-banana-dev.chunsutech.com/web/d/ipay88Complete"
    requests.packages.urllib3.disable_warnings()
    res = requests.get(path, params={
        "payment_number":payment_number
    },headers=headers,verify=False)
    return res