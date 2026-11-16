import json
def save_as_json(data, filename):
    with open(filename,'w') as file:
        json.dump(data, file)

data = {
    'name':'Raj',
    'age': 30
}

save_as_json(data, 'data.json')