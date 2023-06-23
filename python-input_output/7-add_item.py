#!/usr/bin/python3
"""task 7"""
import json
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

file = "add_item.json"
try:
    liz = load_from_json_file(file)
except FileNotFoundError:
    liz = []
liz += sys.argv[1:]
save_to_json_file(liz, file)
