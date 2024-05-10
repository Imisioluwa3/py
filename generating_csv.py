import csv

hosts = [["workstation.local","192.168.25.46"],["webserver.cloud","10.2.5.6"]]

def generate_csv(csv_file_path):
    with open(csv_file_path,'w', newline='') as hosts_csv:
        writer = csv.writer(hosts_csv)
        writer.writerows(hosts)
        
        
generate_csv("hosts.csv")