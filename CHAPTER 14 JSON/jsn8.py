import json


def load_from_json(filename):
    with open(filename, 'r') as file:
        data = json.load(file)

    return data


data = load_from_json('data.json')

print(data)
print(data['name'])
print(data['age'])