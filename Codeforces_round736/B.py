#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 21:56:48 2021

@author: hienpham
"""
import os
import math
import sys
 
parse_input = lambda: sys.stdin.readline().rstrip("\r\n")
 
 
def func(n, str1, strn):
    
    enemy = [int(i) for i in str1]
    gregor = [int(j) for j in strn]
    
    pawn = [0]*n
    
    k = 0
    count = 0
    while k < n:
        if k == 0:
            if gregor[0] == 1:
                if enemy[0] == 0:
                    count += 1
                    pawn[0] = 1
                elif enemy[1] == 1:
                    count += 1
                    pawn[1] = 1
        elif 0 < k < n-1:
            if gregor[k] == 1:
                if enemy[k] == 0:
                    count += 1
                    pawn[k] = 1
                else:
                    if enemy[k - 1] == 1 and pawn[k - 1] == 0:
                        count += 1
                        pawn[k - 1] = 1
 
                    elif enemy[k + 1] == 1 and pawn[k + 1] == 0:
                        count += 1
                        pawn[k + 1] = 1
        elif k == n-1:
            if gregor[n - 1] == 1:
                if enemy[n - 1] == 0:
                    count += 1
                    pawn[n - 1] = 1
                elif enemy[n - 2] == 1 and pawn[n - 2] == 0:
                    count += 1
                    pawn[n - 2] = 1
            
        k += 1
    
    return  count
 
#n = 4
#str1 = '1111'
#strn = '1111'
#ans = func(n, str1, strn)
 
def main():
    n_cases = int(parse_input())
    for i in range(n_cases):
        n = int(parse_input())
        str1 = parse_input()
        strn = parse_input()
        ans =  func(n, str1, strn)
        print(ans)
        
if __name__ == "__main__":
    main()