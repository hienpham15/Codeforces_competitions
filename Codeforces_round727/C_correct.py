#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 20:55:54 2021

@author: hienpham
"""
import sys


parse_input = lambda: sys.stdin.readline().rstrip("\r\n")

def func(arr, n , k, x):
    count = 1
    gaps = []
    
    arr = sorted(arr)
    for i in range(0, n - 1):
        if arr[i+1] - arr[i] > x:
            if ((arr[i+1] - arr[i])%x==0):
                add = (arr[i+1] - arr[i])//x - 1
            else:
                add = (arr[i+1] - arr[i])//x 
            gaps.append(add)
    
    gaps.sort()
    for gap in gaps:
        if k > 0:
            if gap <= k:
                k -= gap
            else:
                count += 1
        else:
            count += 1  
    return count

#arr = [1, 1, 5, 8, 12, 13, 20, 22]
#n, k, x = 8, 2, 3
#a= func(arr, n , k, x)


def main():
    n, k, x = [int(i) for i in parse_input().split()]
    arr = [int(i) for i in parse_input().split()]
    print(func(arr, n , k, x))
        
if __name__ == "__main__":
    main()