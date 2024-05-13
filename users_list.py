import csv

def csv_reader(csv_file_path):
    with open(csv_file_path, 'r') as software_file:
        reader = csv.DictReader(software_file)
        for row in reader:
            print(("{} has {} users").format(row["name"], row["users"]))

csv_reader("software.csv")
