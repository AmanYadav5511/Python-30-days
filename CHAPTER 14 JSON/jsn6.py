person = {'name':'Aman', 'age': 22, 'city': 'gurugram'}
import json
jsonData= json.dumps(person, indent=4)
print(jsonData)
print(type(jsonData))