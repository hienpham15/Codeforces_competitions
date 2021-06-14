#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 17:35:50 2021

@author: hienpham
"""
import os
import math
import sys


parse_input = lambda: sys.stdin.readline().rstrip("\r\n")

def all_D(prefix):
    count = 0
    for char in prefix:
        if char == 'D':
            count += 1
    
    if count == len(prefix):
        return True
    else:
        return False


def all_K(prefix):
    count = 0
    for char in prefix:
        if char == 'D':
            count += 1
    
    if count == len(prefix):
        return True
    else:
        return False


def find_DK(prefix):
    n_DK = prefix.count('DK')
    return n_DK

def find_KD(prefix):
    n_KD = prefix.count('KD')
    return n_KD


def func(string, n):
    s = []
    prefix = ''
    for i in range(n):
        prefix += string[i]
        
        if all_D(prefix):
            s.append(len(prefix))
        elif all_K(prefix):
            s.append(prefix)
        else:
            n_DK = find_DK(prefix)
            n_KD = find_KD(prefix)
            
            if n_DK >= n_KD:
                s.append(n_DK)
            else:
                s.append(n_KD)
    return s

#string = 'DDK'
#s = func(string, len(string))

def main():
    n_cases = int(parse_input())
    for i in range(n_cases):
        n = int(parse_input())
        string = parse_input()
        s = func(string, n)
        print(*s)
        
if __name__ == "__main__":
    main()