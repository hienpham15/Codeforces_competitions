#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 20 16:15:00 2021

@author: hienpham
"""

import os
import math
import sys


parse_input = lambda: sys.stdin.readline().rstrip("\r\n")



def func(n):
    i = n
    while i > 0:
        ans = i & (i - 1)
        if ans == 0:
            return (i - 1)
        else:
            i -= 1
    
    
def main():
    n_cases = int(parse_input())
    for i in range(n_cases):
        n = int(parse_input())
        print(func(n))
        
if __name__ == "__main__":
    main()