#!/usr/bin/python3
""" module contains program to add arguments to json file """

import sys
import os

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

with open(filename, 'a', encoding="utf-8") as f:
    pass

if len(sys.argv) == 1 and os.path.getsize(filename) == 0:
    save_to_json_file([], filename)

else:
    arg_list = sys.argv[1:]

    if os.path.getsize(filename) == 0:
        my_object = arg_list
        save_to_json_file(my_object, filename)
    else:
        my_object = load_from_json_file(filename)
        my_object.extend(arg_list)
        save_to_json_file(my_object, filename)
