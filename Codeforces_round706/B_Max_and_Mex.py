# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os
import math
import sys




parse_input = lambda: sys.stdin.readline().rstrip("\r\n")

def find_mex(multiset):
    if not multiset:
        return 1
    i = 0
    while i <= max(multiset):
        if i not in multiset:
            return i
        i += 1
    return i


def operation(max_val, mex_val):
    return math.ceil((mex_val + max_val)/2)
    

def func(multiset, k):
    for i in range(k):
        mex_val = find_mex(multiset)
        max_val = max(multiset)
        new_val = operation(max_val, mex_val)
        multiset.append(new_val)
    return len(set(multiset))


def main():
    n_cases = int(parse_input())
    for _ in range(n_cases):
        n, k = [int(i) for i in parse_input().split()]
        multiset = [int(i) for i in parse_input().split()]
        result = func(multiset, k)
        print(result)

#def main():
#    n_cases = int(input().strip())
#    for _ in range(n_cases):
#        nk = input().strip().split(' ')
#        n = int(nk[0])
#        k = int(nk[1])
       
#        multiset = list(map(int, input().strip().split(' ')))
#        result = func(multiset, k)
#        print(result)
        
if __name__ == "__main__":
    main()