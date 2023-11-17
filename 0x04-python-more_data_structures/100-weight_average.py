#!/usr/bin/python3
def weight_average(my_list=[]):
    result = 0
    sum = 0
    for i in range(len(my_list)):
        result += (my_list[i][0] * my_list[i][1])
        sum += my_list[i][1]
    if sum == 0:
        return 0
    else:
        return result / sum
