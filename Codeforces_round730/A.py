#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 16:35:10 2021

@author: hienpham
"""
import random
import math
import sys


parse_input = lambda: sys.stdin.readline().rstrip("\r\n")

def func(a, b):
    if a == b:
        return 0, 0
    
    if abs(a - b) == 1:
        return 1, 0
    
    if a > 0 and b > 0:
        e = abs(a - b)
        gcd = math.gcd(a, b)
        if e == gcd:
            return e, 0
        else:
            max_e = max(gcd, e)
        
        moves = min(min(a, b)%max_e, max_e - min(a, b)%max_e)
        return max_e, moves
    
    elif a==0 or b==0:
        return max(a, b), 0
    


def main():
    n_cases = int(parse_input())
    for i in range(n_cases):
        a, b = [int(i) for i in parse_input().split()]
        max_e, moves = func(a, b)
        print("{} {}".format(max_e, moves))
        
if __name__ == "__main__":
    main()