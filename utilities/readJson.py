import json


def read_json(filepath):
    file_path = open(filepath, 'r')
    json_data = file_path.read()
    return json_data


def read_json_obj(filepath):
    file_path = open(filepath, 'r')
    json_data = file_path.read()
    obj = json.loads(json_data)
    return obj
