#!/usr/bin/python3
def uniq_add(my_list=[]):
    s = 0
    newlist = []
    for elm in my_list:
        if elm not in newlist:
            newlist.append(elm)
    for i in newlist:
        s += i
    return s
