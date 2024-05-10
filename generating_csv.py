import csv

hosts = [["workstation.local","192.168.25.46"],["webserver.cloud","10.2.5.6"]]

def generate_csv(csv_file_path):
    with open(csv_file_path,'w', newline='') as hosts_csv:
        writer = csv.writer(hosts_csv)
        writer.writerow(["name", "address"])
        writer.writerows(hosts)
        
        
generate_csv("hosts.csv")

def reading_csv(csv_file):
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            print("{}'s IP Address is {}.".format(row["name"], row["address"]))
            
reading_csv("hosts.csv")