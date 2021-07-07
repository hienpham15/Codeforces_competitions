#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 16:52:06 2021

@author: hienpham
"""
import os
import math
import sys


parse_input = lambda: sys.stdin.readline().rstrip("\r\n")


def func(n_track, arr):
    total_car = sum(arr)
    rem = total_car%n_track
    inconv = rem * (n_track - rem)
    
    return inconv


def main():
    n_cases = int(parse_input())
    for i in range(n_cases):
        n_track = int(parse_input())
        arr = [int(i) for i in parse_input().split()]
        print(func(n_track, arr))
        
if __name__ == "__main__":
    main()