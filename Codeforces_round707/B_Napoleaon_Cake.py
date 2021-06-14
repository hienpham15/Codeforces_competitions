#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 11:31:53 2021

@author: hienpham
"""
import os 
import math
import sys

parse_input = lambda: sys.stdin.readline().rstrip("\r\n")


def func(n_layers, cream):
    drenched = []
    
    if max(cream) == 0:
        return [0 for i in range(n_layers)]
    
    for i in range(n_layers):
        drenched.append(0)
        if cream[i] != 0:
            if cream[i] >= len(drenched):
                drenched[:] = [1 for i in range(len(drenched))]
            else:
                drenched[-cream[i]:] = [1 for i in range(len(drenched[-cream[i]:]))]
                
    return drenched
                
 
#n = 10
#c = [0, 0, 0, 1, 0, 5, 0, 0, 0, 2]

#dren = func(n, c)

def main():
    n_cases = int(parse_input())
   
    for _ in range(n_cases):
        n_layers = int(parse_input())
        cream = [int(i) for i in parse_input().split()]
       
        result = func(n_layers, cream)
        for i in range(len(result)):
            print(result[i], end = " ")
       
if __name__ == "__main__":
    main()