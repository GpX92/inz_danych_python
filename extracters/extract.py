import csv

def extract(path):
  with open(path, newline="") as file_handler:
    return list(csv.reader(file_handler, delimiter=","))[1:]
