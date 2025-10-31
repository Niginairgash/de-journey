import json
import csv
import pandas as pd

with open('cities.csv', 'r', encoding='utf-8') as csv_file:
    data = list(csv.DictReader(csv_file, delimiter='\t'))

with open('cities.json', 'w', encoding='utf-8') as json_file:
    json.dump(data, json_file, indent=2)

df = pd.read_csv('cities.csv', delimiter='\t', quotechar='"', escapechar='\\')

df.to_json('cities.json', orient='records', lines=True, indent=2 )