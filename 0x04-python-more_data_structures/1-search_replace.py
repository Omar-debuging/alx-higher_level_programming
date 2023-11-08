#!/usr/bin/python3
def search_replace(my_list, search, replace):
    newlist = []
    for i in range(len(my_list)):
        newlist.append(replace if my_list[i] == search else my_list[i])
    return newlist
