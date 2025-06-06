#!/usr/bin/python3
"""
task_02_csv.py - Module containing a function for serializing CSV int JSon.
"""
import csv
import json


def convert_csv_to_json(filename):
    """
    Function serializing data from CSV file into JSON file.
    """
    newList = []
    try:
    	with open(filename, newline='') as f:
            dictReader = csv.DictReader(f)
            for line in dictReader:
                newList.append(line)
    except FileNotFoundError:
        return False

    res = json.dumps(newList, indent=4)

    with open("data.json", 'w', encoding='utf-8') as f:
        f.write(res)

    return True
