#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 16:51:38 2021

@author: hienpham
"""
import os
import math
import sys



parse_input = lambda: sys.stdin.readline().rstrip("\r\n")


def func(n, k, string):
    first_ind = string.find('*')
    last_ind = string.rfind('*')
    
    count = 2
    
    if first_ind == last_ind:
        return 1
    else:
        i = first_ind
        while i < last_ind - k:
            j = k
            while j > 0:
                if i + j == last_ind:
                    return count
                else:
                    if string[i + j] == '*':
                        count += 1
                    
                        i += j
                        j = 0
                    else:
                        j -= 1
        return count

        
n = 7
k = 3
s = '.**.***'
func(n, k, s)

def main():
    n_cases = int(parse_input())
    for i in range(n_cases):
        n, k = [int(i) for i in parse_input().split()]
        string = parse_input()
        print(func(n, k, string))
        
if __name__ == "__main__":
    main()