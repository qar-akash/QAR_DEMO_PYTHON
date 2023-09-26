import requests


def get_method(uri, header):
    response = requests.get(uri, headers=header)
    return response


def post_method(uri, header, payload):
    response = requests.post(uri, headers=header, json=payload)
    return response


def put_method(uri, header, payload):
    response = requests.put(uri, headers=header, json=payload)
    return response
