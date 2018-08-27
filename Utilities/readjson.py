#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
# /pythonjulia/files/AddTransactionRequestBody.json

def read_json(filename):
    with open(filename, 'r') as load_f:
        load_dict1 = json.load(load_f)
        load_dict2 = json.dumps(load_dict1)
        return load_dict2
