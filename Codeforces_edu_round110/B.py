#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 17:06:13 2021

@author: hienpham
"""

import os
import math
import sys


parse_input = lambda: sys.stdin.readline().rstrip("\r\n")

def split_even_odd(array):
    even = []
    odd = []
    
    for i in array:
        if (i%2 == 0):
            even.append(i)
        else:
            odd.append(i)
    
    even = sorted(even, reverse=True)
    odd = sorted(odd, reverse=True)
    return even+odd

def func(array):
    array_sorted = split_even_odd(array)
    
    if len(array) == 2:
        if math.gcd(array_sorted[0], 2*array_sorted[1]) > 1:
            return 1
        else:
            return 0
    
    count = 0
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if math.gcd(array_sorted[i], 2*array_sorted[j]) > 1:
                count += 1
            
    return count

#arr = [8, 7, 6, 9, 5, 3, 3, 4, 4, 2]
#c = func(arr)

def main():
    n_cases = int(parse_input())
    for i in range(n_cases):
        n_element = int(parse_input())
        array = [int(i) for i in parse_input().split()]
        print(func(array))
        
if __name__ == "__main__":
    main()