pythonlist = ['apple','banana','cherry']
import json
jsonlist = json.dumps(pythonlist)
print(jsonlist)
jsonlist2 = json.loads(jsonlist)
print(jsonlist2)
print(pythonlist == jsonlist2)