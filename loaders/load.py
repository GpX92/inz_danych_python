import json

def load(names, path):
  with open(path, mode="w") as file_handler:
    json_data = [
        json.dumps({"Imię": name}) + "\n" for name in names
    ]
    file_handler.writelines(json_data)
