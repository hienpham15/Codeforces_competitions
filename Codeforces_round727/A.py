#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 12:16:51 2021

@author: hienpham
"""
import os
import math
import sys


parse_input = lambda: sys.stdin.readline().rstrip("\r\n")

    

def func(n, x, t):
    
    start_time = []
    finish_time = []
    
    for i in range(n):
        start_time.append(x*i)
        finish_time.append(x*i + t)
    dis = 0    
    for i in range(len(start_time)):
         arr = [x for x in start_time[(i+1):] if x <= finish_time[i]]
         dis += len(arr)
        
    return dis

a = func(2000000000, 1, 2000000000)


def main():
    n_cases = int(parse_input())
    for i in range(n_cases):
        n, x, t = [int(i) for i in parse_input().split()]
        print(func(n, x, t))
        
if __name__ == "__main__":
    main()        