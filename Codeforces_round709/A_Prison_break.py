#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 14:25:17 2021

@author: hienpham
"""
import os
import math
import sys



parse_input = lambda: sys.stdin.readline().rstrip("\r\n")


def func(a, b):
    
    return a*b


def main():
    n_cases = int(parse_input())
    for i in range(n_cases):
        a, b = [int(i) for i in parse_input().split()]
        print(func(a, b))
        
if __name__ == "__main__":
    main()