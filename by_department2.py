import csv

users = [ {"name": "Sol Mansi", "username": "solm", "department": "IT infrastructure"},
          {"name": "Lio Nelson", "username": "lion", "department": "User Experience Research"},
          {"name": "Charlie Grey", "username": "greyc", "department": "Development"}]
keys = ["name", "username", "department"]

def csv_writer(csv_file):
    with open (csv_file, 'w', newline='') as by_department:
        writer = csv.DictWriter(by_department, fieldnames= keys)
        writer.writeheader()
        writer.writerows(users)

        for user in users:
           print("The username and department of {} are {} and {} respectively.".format(user['name'], user['username'], user['department'])) 
           
csv_writer("dept.csv")