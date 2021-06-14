#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 16:34:52 2021

@author: hienpham
"""

import os
import math
import sys



parse_input = lambda: sys.stdin.readline().rstrip("\r\n")


def all_even(arr):
    count = 0
    for elem in arr:
        if elem == 0 or elem%2 == 0:
            count += 1
    
    if count == len(arr):
        return True
    else:
        return False
            
def add_even_element(arr, max_val, min_val):
    if min_val == 0:
        x = 0
    else:
        x = 2
        
    for i in range(x, max_val, 2):
        if i not in arr:
            arr.append(i)
    return arr

def add_element(arr, max_val, min_val):
    if min_val == 0:
        x = 0
    else:
        x = 1
    for i in range(x, max_val):
        if i not in arr:
            arr.append(i)
    return arr
    

def func(arr, len_a):
    
    max_val = max(arr)
    min_val = min(arr)
    
    if max_val - min_val > max_val:
        return "NO", 0, 0
    
    if all_even(arr):
        even_arr = add_even_element(arr, max_val, min_val)
        return "YES", len(even_arr), even_arr
        
    else:
        new_arr = add_element(arr, max_val, min_val)
        return "YES", len(new_arr), new_arr

#arr = [3, 0, 9]
#ans, new_len, new_arr = func(arr, len(arr))

def main():
    n_cases = int(parse_input())
    for i in range(n_cases):
        len_a = int(parse_input())
        arr = [int(i) for i in parse_input().split()]
        ans, new_len, new_arr = func(arr, len_a)
        if ans == "NO":
            print(ans)
        else:
            print(ans)
            print(new_len)
            print(*new_arr)
        
if __name__ == "__main__":
    main()