import json
from datetime import date

data_to_save = {{'id': 1, 'description': 'Do something', 'status': 'todo', 'createtAt': str(date.today())}}
with open('data.json', 'w') as file:
    json.dump(data_to_save, file, indent=4)

with open("data.json", "r") as file:
    loaded_data = json.load(file)
print(loaded_data)

