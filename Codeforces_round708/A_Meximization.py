#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 15:27:14 2021

@author: hienpham
"""
import os
import math
import sys
from collections import Counter

parse_input = lambda: sys.stdin.readline().rstrip("\r\n")


def func(array):
    sorted_array = sorted(array)
    
    new_array = []
    sup_array = []
    for item, count in Counter(sorted_array).items():
        new_array.append(item)
        if count > 1:
            sup_array.append(item)
        
    final_array = new_array + sup_array
    return final_array


#s = [0, 3, 3, 2, 1, 1, 1, 7, 4, 7, 5]
#arr = func(s)

def main():
    n_cases = int(parse_input())
    for i in range(n_cases):
        n = int(parse_input())
                
        array = parse_input()
        
        result = func(array)
        for i in range(len(result)):
            print(result[i], end = " ")
        #print(func(array))
        
if __name__ == "__main__":
    main()