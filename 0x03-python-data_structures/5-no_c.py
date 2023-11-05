#!/usr/bin/python3
def no_c(my_string):
    newstr= ""
    for elm in my_string:
        if elm != "c" and elm != "C":
            newstr = newstr + elm
    print("{}".format(newstr))
