#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 16:31:37 2021

@author: hienpham
"""
import os
import math
import sys


parse_input = lambda: sys.stdin.readline().rstrip("\r\n")

def is_in_q1(val, skill):
    ind = skill.index(val)
    if ind == 0 or ind == 1:
        return True
    else:
        return False
    

def is_in_q2(val, skill):
    ind = skill.index(val)
    if ind == 2 or ind == 3:
        return True
    else:
        return False


def func(skill):
    max_val_1 = max(skill)
    skill_copy = skill[:]
    skill_copy.remove(max_val_1)
    max_val_2 = max(skill_copy)
    
    if is_in_q1(max_val_1, skill) and is_in_q1(max_val_2, skill):
        return "NO"
    elif is_in_q2(max_val_1, skill) and is_in_q2(max_val_2, skill):
        return "NO"
    else:
        return "YES"

a = [3, 7, 9, 5]

ans = func(a)

def main():
    n_cases = int(parse_input())
    for i in range(n_cases):
        skill = [int(i) for i in parse_input().split()]
        print(func(skill))
        
if __name__ == "__main__":
    main()