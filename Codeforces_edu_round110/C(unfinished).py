#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 18:06:41 2021

@author: hienpham
"""
import os
import math
import sys


parse_input = lambda: sys.stdin.readline().rstrip("\r\n")


def func(string):
    if len(string) == 1:
        return 1
    
    if len(string) == 2:
        if string == '00' or string == '11':
            return 2
        else:
            return 3
    
    
            
    return count

#arr = [8, 7, 6, 9, 5, 3, 3, 4, 4, 2]
#c = func(arr)

def main():
    n_cases = int(parse_input())
    for i in range(n_cases):
        string = parse_input()
        print(func(string))
        
if __name__ == "__main__":
    main()