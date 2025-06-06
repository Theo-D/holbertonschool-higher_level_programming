#!/usr/bin/python3
"""
7-add_item.py - Module for writing args to file
"""
import sys
import os


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

if __name__ == "__main__":
    file = "add_item.json"
    if os.path.isfile(file):
        list = load_from_json_file(file)
    else:
        list = []
    args = sys.argv[1:]
    list.extend(args)
    save_to_json_file(list, file)
