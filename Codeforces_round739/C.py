#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 17:21:43 2021

@author: hienpham
"""
import os
import math
import sys


parse_input = lambda: sys.stdin.readline().rstrip("\r\n")

def is_in_table(prev_x, x):
    if x+1 <= prev_x:
        return True
    else:
        return False
    


def function(k, d):
    
    if k in d.keys():
        return d[k]
    else:
        ind = list(d.keys())[-1]
        tour = True
        left = False
        #down = False
        x, y = d[ind]
        prev_x = 1
        for i in range(ind+1, k+1):
            #x, y = d[i-1]
            
            if tour:
                y += 1
                tour = False
                y_next = y 
                d[i] = (x, y)
                continue
            
            
            if left:
                y -= 1
                d[i] = (x, y)
                if y == 1 and not tour:
                    left = False
                    prev_x = x
                    x = 1
                    y = y_next
                    tour = True
                continue
            
            if not is_in_table(prev_x, x) and y>1:
                x += 1
                d[i] = (x, y)
                left = True
                continue
            else:
                x += 1
                d[i] = (x, y)
                #down = True
                continue
            

        return d[k]
    

k = 14
d = {}
d[1] = (1, 1)
ans = function(k, d)

def main():
    n_cases = int(parse_input())
    d = {}
    d[1] = (1, 1)
    for i in range(n_cases):
        k = int(parse_input())
        print(function(k, d))
        
if __name__ == "__main__":
    main()