import csv
import json

def extract(path):
  with open(path, newline="") as file_handler:
    return list(csv.reader(file_handler, delimiter=","))[1:]

def transform(employees):
  return {
      e[1] for e in employees
  }

def load(names, path):
  with open(path, mode="w") as file_handler:
    json_data = [
        json.dumps({"Imię": name}) + "\n" for name in names
    ]
    file_handler.writelines(json_data)
