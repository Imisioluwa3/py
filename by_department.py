import csv

file = open ("txt.csv")
csv_f = csv.reader(file)

for row in csv_f:
    name,phone,department = row
    print("Name:{}, Phone:{}, Department:{}".format(name,phone,department))
file.close()