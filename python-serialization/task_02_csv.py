"""From CSV to JSON"""
import csv
import json


def convert_csv_to_json(filename):
    """Convert CSV file to JSON file"""
    csv_list = []

    try:
        with open(filename, encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for rows in reader:
                csv_list.append(rows)
    except Exception:
        return False
    try:
        with open("data.json", 'w') as file:
            json.dump(csv_list, file)
    except Exception:
        return False
    return True
