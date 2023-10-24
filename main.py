import os
import csv

input_directory = os.path.dirname(os.path.abspath(__file__))
has_done = []
no_done = []

for path, subdirs, files in os.walk(input_directory):
    if any(name in path for name in has_done):
        continue
    if any(name.endswith('.done') for name in files):
        has_done.append(path)
    else:
        no_done.append(path)

output_name = 'Missing Done Directories.csv'
with open(output_name, 'w', newline='') as f:
    writer = csv.writer(f)
    output = [[x.replace(input_directory, '').removeprefix('\\')] for x in no_done if x.replace(input_directory, '')]
    writer.writerow(['Directories missing .done files'])
    writer.writerows(output)

print(f"Scan complete. CSV File written to: {input_directory}/{output_name}")