import requests
import csv

# Download the CSV file
url = "https://d37ci6vzurychx.cloudfront.net/misc/taxi_zone_lookup.csv"
response = requests.get(url)

# Save the CSV file locally
csv_path = "C:/Users/Riya/OneDrive/Desktop/taxi_zone_lookup.csv"

with open(csv_path, 'wb') as file:
    file.write(response.content)

# Open and read the CSV file
records = []
with open(csv_path, 'r') as file:
    reader = csv.reader(file)
    header = next(reader)  # Skip the header
    for row in reader:
        records.append(row)

# a. Total number of records sorted in ascending order
sorted_records = sorted(records, key=lambda x: x[2])  # Sort by 'Zone' (3rd column)
total_records = len(sorted_records)

# b. Find unique boroughs
boroughs = set([row[1] for row in records])  # 2nd column is 'Borough'
unique_boroughs = list(boroughs)

# c. Number of records for Brooklyn Borough
brooklyn_records = [row for row in records if row[1] == 'Brooklyn']
brooklyn_count = len(brooklyn_records)

# d. Save the results to a file
output_path = "C:/Users/Riya/OneDrive/Desktop/taxi_zone_output.txt"

with open(output_path, 'w') as output_file:
    output_file.write(f"Total Records (sorted ascending): {total_records}\n")
    output_file.write(f"Unique Boroughs: {', '.join(unique_boroughs)}\n")
    output_file.write(f"Number of Records for Brooklyn: {brooklyn_count}\n")

print("Processing complete! Output saved to /root/taxi_zone_output.txt")
