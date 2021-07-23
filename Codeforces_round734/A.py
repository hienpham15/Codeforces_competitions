#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 16:34:45 2021

@author: hienpham
"""
import os
import math
import sys


parse_input = lambda: sys.stdin.readline().rstrip("\r\n")


def func(burle):
    rem = burle%3
    
    if rem == 0:
        c1 = c2 = burle//3
    elif rem == 1:
        c1 = burle//3 + 1
        c2 = burle//3
    else:
        c1 = burle//3
        c2 = burle//3 + 1
        
    return (c1, c2)

#ans = func(1000)

def main():
    n_cases = int(parse_input())
    for i in range(n_cases):
        burle = int(parse_input())
        print(*func(burle))
        
if __name__ == "__main__":
    main()