import json

data = '{"name": "Bard"}'

json_object = json.loads(data)

print(json_object['name'])