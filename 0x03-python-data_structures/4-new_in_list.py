#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if not ((idx < 0) or (idx > len(my_list) - 1)):
        new = my_list[:]
        new[idx] = element
        return new
    return my_list
