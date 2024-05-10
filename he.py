import csv

file = open ("txt.csv")
csv_f = csv.reader(file)

for row in csv_f:
    name,phone,role = row
    print("Name:{}, Phone:{}, Role:{}".format(name,phone,role))
file.close()