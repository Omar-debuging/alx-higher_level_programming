#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        l = list(a_dictionary.items())
        maximum = l[0][1]
        for i in range(len(l)):
            if l[i][1] >= maximum:
                maximum = l[i][1]
        return (list(a_dictionary.keys())[list(a_dictionary.values()).index(maximum)])
    else:
        return None
