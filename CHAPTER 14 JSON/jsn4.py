stringofJSONDATA = '{"name":"Rajesh", "age": 30}'
import json
pythondata = json.loads(stringofJSONDATA)
print(pythondata)
print(type(pythondata))
print(pythondata['name'])