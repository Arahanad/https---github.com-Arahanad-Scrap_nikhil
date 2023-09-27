import csv
import json

with open ('data.json','r') as json_file:
    data = json.dump(json_file)

csv_file = "franchisegrade_data.csv"
csv_header = data[0].keys()
with open(csv_file, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=csv_header)
    writer.writeheader()
    for row in data:
        writer.writerow(row)

print(f"CSV file '{csv_file}' has been created.")
