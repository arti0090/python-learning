#!/usr/bin/env python3

""" module.py - przykładowy moduł w języku Python """

__counter = 0

def suml(list):
    global __counter
    __counter += 1
    sum = 0
    for element in list:
        sum += element
    
    return sum

def prodl(list):
    global __counter
    __counter += 1
    prod = 1
    for element in list:
        prod *= element

    return prod

if __name__ == '__main__':
    print("Wole byc modulem, ale moge zrobic dla Ciebie kilka testów.")
    my_list = [i + 1 for i in range(5)]
    print(suml(my_list) == 15)
    print(prodl(my_list) == 120)