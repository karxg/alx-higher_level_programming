#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    divisible_check = []
    for n in my_list:
        divisible_check.append(n % 2 == 0)
    return divisible_check
