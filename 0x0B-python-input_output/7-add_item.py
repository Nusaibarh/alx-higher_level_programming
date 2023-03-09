#!/usr/bin/python3
"""
Use all our modules bayii...
"""

import sys
json = __import__("json")
load_file = __import__('6-load_from_json_file').load_from_json_file
save_file = __import__('5-save_to_json_file').save_to_json_file


n = len(sys.argv)
try:
    obj = load_file("add_item.json")
except Exception:
    save_file([], "add_item.json")
    obj = load_file("add_item.json")
finally:
    for i in range(1, n):
        obj.append(sys.argv[i])
    save_file(obj, "add_item.json")
