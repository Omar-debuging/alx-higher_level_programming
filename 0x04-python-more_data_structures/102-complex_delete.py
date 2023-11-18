#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    dict = {}
    if value not in a_dictionary.values():
        return a_dictionary
    else:
        for key, val in a_dictionary.items():
            if val != value:
                dict[key] = val
        return  dict
