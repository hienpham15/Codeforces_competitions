#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 16:35:58 2021

@author: hienpham
"""
import os
import math
import sys


parse_input = lambda: sys.stdin.readline().rstrip("\r\n")


def func(arr, n):
    mean = sum(arr)/n
    if mean == 1.0:
        return 0
    elif sum(arr) <= 0:
        return 1
    elif sum(arr) > n:
        return sum(arr) - n
    elif sum(arr) < n:
        return 1



def main():
    n_cases = int(parse_input())
    for i in range(n_cases):
        n = int(parse_input())
        arr = [int(i) for i in parse_input().split()]
        print(func(arr, n))
        
if __name__ == "__main__":
    main()