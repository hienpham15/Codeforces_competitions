#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 17 18:11:24 2021

@author: hienpham
"""
import os
import math
import sys


parse_input = lambda: sys.stdin.readline().rstrip("\r\n")

def func(n_stages, my_points, il_points):
    selected = n_stages - n_stages//4
    
    my_points.sort(reverse=True)
    il_points.sort(reverse=True)
    
    my_highpoint = sum(my_points[:selected])
    il_highpoint = sum(il_points[:selected])
    
    count = 0
    while my_highpoint < il_highpoint:
        my_points.insert(0, 100)
        il_points.append(0)
        n_stages += 1
        
        selected = n_stages - n_stages//4
        my_highpoint = sum(my_points[:selected])
        il_highpoint = sum(il_points[:selected])
        
        count +=1
        
    return count


#n_stages = 7
#my = [7, 59, 62, 52, 27, 31, 55]
#il = [33, 35, 50, 98, 83, 80, 64]
#ans = func(n_stages, my, il)

def main():
    n_cases = int(parse_input())
    for i in range(n_cases):
        n_stages = int(parse_input())
        my_points = [int(i) for i in parse_input().split()]
        il_points = [int(i) for i in parse_input().split()]
        print(func(n_stages, my_points, il_points))
        
if __name__ == "__main__":
    main()