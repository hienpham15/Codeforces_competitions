#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 17 18:42:25 2021

@author: hienpham
"""
import os
import math
import sys


parse_input = lambda: sys.stdin.readline().rstrip("\r\n")

def func(n, wishes):
    bag = {}
    
    naughty = {}
    
    for i, wish in enumerate(wishes):
        if wish in bag:
            bag[wish] += [i+1]
        else:
            bag[wish] = [i+1]
    
    d_wishes = len(bag)
    
    
    available = []
    
    assigned = [0 for i in range(n)]
    
    for wish in bag:
        gifts = bag[wish]
        if len(gifts) > 1:
            available += gifts[1:]
            bag[wish] = [gifts[0]]
            
    for i in range(n):
        if i+1 not in bag:
            bag[i+1] = [available.pop()]
    
    for key, values in bag.items():
        assigned[values[0] - 1] = key
            
        
    return d_wishes, assigned

n = 7
wishes = [6, 4, 6, 2, 4, 5, 6]
ans = func(n, wishes)


def main():
    n_cases = int(parse_input())
    for i in range(n_cases):
        n = int(parse_input().split())
        wishes = [int(i) for i in parse_input().split()]
        d_wishes, assigned = func(n, wishes)
        print(d_wishes)
        print(*assigned)
        
if __name__ == "__main__":
    main()