import csv
import os

file_to_load = 'Resources/election_results.csv'
file_to_save = 'analysis/election_analysis.txt'

with open(file_to_save, "w") as txt_file:
    txt_file.write("Arapahoe\nDenver\nJefferson")

with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    print(headers)
