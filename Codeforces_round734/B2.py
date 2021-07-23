#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 17:14:55 2021

@author: hienpham
"""
import os
import math
import sys
from collections import Counter

parse_input = lambda: sys.stdin.readline().rstrip("\r\n")



def func(n, k, arr):
    stats = Counter(arr)
    d = {}
    for i in range(k+1):
        d[i] = []
    
    j = 1
    for key, val in stats.items():
        if val >= k:
            for i in range(k):
                d[i+1] += [key]
            
            m = 0
            while m < val - k:
                d[0] += [key]
                m += 1
        else:
            while val > 0:
                if j > k:
                    j = 1
                d[j] += [key]
                val -= 1
                j += 1
    
    min_l = math.inf
    for i in range(1, len(d)):
        array = d[i]
        l = len(array)
        if l < min_l:
            min_l = l
    
    for i in range(1, len(d)):
        array = d[i]
        for i in range(abs(len(array) - min_l)):
            if array:
                d[0] += [array.pop()]
    
    ans = []
    
    for val in arr:
        j = 0
        while True:
            if val in d[j]:
                ans.append(j)
                d[j].remove(val)
                break
            else:
                j += 1
    return ans

arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9]
n, k = 13, 3
ans = func(n, k, arr)

def main():
    n_cases = int(parse_input())
    for i in range(n_cases):
        n, k = [int(i) for i in parse_input().split()]
        arr = [int(i) for i in parse_input().split()]
        ans =  func(n, k, arr)
        print(' '.join(map(str, ans)))
        
if __name__ == "__main__":
    main()