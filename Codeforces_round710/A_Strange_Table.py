#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 16:25:28 2021

@author: hienpham
"""
import os
import math
import sys



parse_input = lambda: sys.stdin.readline().rstrip("\r\n")


def func(n, m, x):
    mod = x%n
    if mod != 0:
        return (mod-1)*m + (x//n + 1)
    else:
        return (n-1)*m + x//n


def main():
    n_cases = int(parse_input())
    for i in range(n_cases):
        n, m, x = [int(i) for i in parse_input().split()]
        print(func(n, m, x))
        
if __name__ == "__main__":
    main()
    
    