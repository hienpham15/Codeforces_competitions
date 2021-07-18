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
    
    my_points.sort()
    il_points.sort()
    
    my_points_prefix = [0]
    il_points_prefix = [0]
    for i in range(n_stages):
        my_points_prefix.append(my_points_prefix[i] + my_points[i])
        il_points_prefix.append(il_points_prefix[i] + il_points[i])
        
    my_points_prefix = my_points_prefix[1:]
    il_points_prefix = il_points_prefix[1:]
        
    if n_stages < 4:
        my_highpoint = my_points_prefix[n_stages - 1]
        il_highpoint = il_points_prefix[n_stages - 1]
    else:
        my_highpoint = my_points_prefix[n_stages -1] - my_points_prefix[n_stages//4 - 1]
        il_highpoint = il_points_prefix[n_stages -1] - il_points_prefix[n_stages//4 - 1]
    
    my_k = n_stages//4
    il_k = n_stages//4
    my_lowest = my_points[my_k]
    
    count = 0
    while my_highpoint < il_highpoint:
      
        n_stages += 1
        
        if n_stages%4 != 0:
            my_highpoint += 100
            
            if il_k - 1 >= 0:
                il_highpoint += il_points[il_k - 1]
                il_k -= 1
                
        else:
            my_highpoint += 100 - my_lowest 
            my_k += 1
            my_lowest = my_points[my_k]
            
        count +=1
        
    return count


n_stages = 4
my = [20, 30, 40, 50]
il = [100, 100, 100, 100]
ans = func(n_stages, my, il)

def main():
    n_cases = int(parse_input())
    for i in range(n_cases):
        n_stages = int(parse_input())
        my_points = [int(i) for i in parse_input().split()]
        il_points = [int(i) for i in parse_input().split()]
        print(func(n_stages, my_points, il_points))
        
if __name__ == "__main__":
    main()