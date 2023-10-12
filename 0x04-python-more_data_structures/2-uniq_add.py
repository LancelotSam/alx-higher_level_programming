#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique = []
    result = 0
    for num in my_list:  # iterate through my_list
        if num not in unique:  # if no encountered in the current iteration
            unique.append(num)
            result += num
    return result
