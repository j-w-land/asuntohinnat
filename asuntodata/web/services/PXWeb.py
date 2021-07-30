import os
import requests
import json
from .parseResponse import parseResponse

url_get_prices = 'https://pxnet2.stat.fi/PXWeb/api/v1/fi/StatFin/asu/ashi/vv/statfin_ashi_pxt_112q.px'


def api(url, query):

    headers = {
        "method": "POST",  # *GET, POST, PUT, DELETE, etc.
        "mode": "cors",  # no-cors, *cors, same-origin
        "cache": "no-cache",  # *default, no-cache, reload, force-cache, only-if-cached
        "credentials": "same-origin",  # include, *same-origin, omit
        "Content-Type": "application/json",
        "redirect": "follow",  # manual, *follow, error
        # no-referrer, *no-referrer-when-downgrade, origin, origin-when-cross-origin, same-origin, strict-origin, strict-origin-when-cross-origin, unsafe-url
        "referrerPolicy": "no-referrer",
    }

    body = {
        "query": query,
        "response": {
            "format": "json-stat",
        }
    }

    r = requests.post(url, json=body, headers=headers)

    if r.status_code != 200:
        return ""
    data = r.json()
    """ droplet_list = []
    for i in range(len(droplets['droplets'])):
        droplet_list.append(droplets['droplets'][i]) """
    return data


def get_prices_by_zip(zip):
    print("get_prices_by_zip")
    print(zip)
    query = [{
        "code": "Postinumero",
        "selection": {
            "filter": "item",
            "values": zip,
        },
    }]
    prices_data = api(url_get_prices, query)
    # print(prices_data)
    # print("prices_data")
    parsedData = parseResponse(prices_data)
    # print(parsedData)
    # print("parsedData")
    return parsedData
