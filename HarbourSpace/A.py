#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 16:27:05 2021

@author: hienpham
"""
import os
import math
import sys



parse_input = lambda: sys.stdin.readline().rstrip("\r\n")



def func(n):
    
    return (n+1)//10


def main():
    n_cases = int(parse_input())
    for i in range(n_cases):
        n = int(parse_input())
        print(func(n))
        
if __name__ == "__main__":
    main()