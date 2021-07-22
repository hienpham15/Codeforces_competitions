#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 16:44:03 2021

@author: hienpham
"""
import os
import math
import sys


parse_input = lambda: sys.stdin.readline().rstrip("\r\n")


def match(i, s, t):
    p_s = i
    p_t = 0
    
    while p_s < len(s)-1 and p_t < len(t) - 1:
        if s[p_s + 1] == t[p_t + 1]:
            p_s += 1
            p_t += 1
        else:
            break
    
    if p_t == len(t) - 1:
        return True
    
    while p_s > 0 and p_t < len(t) - 1:
        if s[p_s - 1] == t[p_t + 1]:
            p_s -= 1
            p_t += 1
        else:
            break
        
    if p_t == len(t) - 1:
        return True
    else:
        return False
        
    
def func(s, t):
    pos = []
    for i in range(len(s)):
        if s[i] == t[0]:
           pos.append(i)
           
    for i in range(len(pos)):
        ans = match(pos[i], s, t)
        if ans:
            return 'YES'
        
    return 'NO'
        
s = 'ba'
t = 'baa'
ans = func(s, t)


def main():
    n_cases = int(parse_input())
    for i in range(n_cases):
        s = parse_input()
        t = parse_input()
        print(func(s, t))
        
if __name__ == "__main__":
    main()