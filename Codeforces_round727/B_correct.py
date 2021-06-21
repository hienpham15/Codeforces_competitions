#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 20:27:18 2021

@author: hienpham
"""
import sys
import string


parse_input = lambda: sys.stdin.readline().rstrip("\r\n")


def calc_prefix(song):
    prefix_sum = 0
    prefix = []
    
    for i in range(len(song)):
        prefix_sum += string.ascii_lowercase.index(song[i]) + 1
        prefix.append(prefix_sum)
    prefix.insert(0, 0)
    return prefix

def func(prefix, l, r):
    
    total = prefix[r] - prefix[l-1]
    return total

#s = 'abacaba'
#l, r = 1, 3 
#a = func(s, l, r)
def main():
    n, q = [int(i) for i in parse_input().split()]
    song = parse_input()
    prefix = calc_prefix(song)
    for j in range(q):
        l, r = [int(i) for i in parse_input().split()]
        print(func(prefix, l, r))
         
if __name__ == "__main__":
    main()