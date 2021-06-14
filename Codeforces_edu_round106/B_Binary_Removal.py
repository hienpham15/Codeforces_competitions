#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 16:25:49 2021

@author: hienpham
"""
import os
import math
import sys


parse_input = lambda: sys.stdin.readline().rstrip("\r\n")




def func(bin_string):
    bin_array = [int(i) for i in list(bin_string)]
    
    if any(bin_array[i] == bin_array[i+1] for i in range(len(bin_array)-1)):
        if (all(element == 0 for element in bin_array)):
            return 'YES'
        elif (all(element == 1 for element in bin_array)):
            return 'YES'
        else:
            flag_1 = False;
            for i in range(len(bin_array) - 1):
                if (bin_array[i] == bin_array[i+1]) & (bin_array[i] == 1):
                    flag_1 = True
                elif (bin_array[i] == bin_array[i+1]) & (bin_array[i] == 0):
                    if flag_1:
                        return 'NO'
                    else:
                        return 'YES'
            if flag_1:
                return 'YES'
    else:
        return 'YES'

s = '10101011011'
func(s)

def main():
    n_cases = int(parse_input())
    for i in range(n_cases):
        bin_string = parse_input()
        print(func(bin_string))
        
if __name__ == "__main__":
    main()