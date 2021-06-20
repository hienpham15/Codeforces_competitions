#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 13:06:30 2021

@author: hienpham
"""
import os
import math
import sys




parse_input = lambda: sys.stdin.readline().rstrip("\r\n")

def func(arr, n , k, x):
    count = 1
    
    arr = sorted(arr)
    for i in range(0, n - 1):
        if arr[i+1] - arr[i] > x:
            if k > 0:
                add = (arr[i+1] - arr[i])//x
                if add <= k:
                    k = k - add
                else:
                    count += 1
            else:
                count += 1  
    return count

#arr = [20, 20, 80, 70, 70, 70, 420, 5, 1, 5, 1, 60, 90]
#n, k, x = 13, 0, 37
#a= func(arr, n , k, x)


def main():
    n, k, x = [int(i) for i in parse_input().split()]
    arr = [int(i) for i in parse_input().split()]
    print(func(arr, n , k, x))
        
if __name__ == "__main__":
    main()