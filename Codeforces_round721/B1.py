#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 20 16:47:17 2021

@author: hienpham
"""

import os
import math
import sys


parse_input = lambda: sys.stdin.readline().rstrip("\r\n")


def is_palindrome(string):
    if string == string[::-1]:
        return True
    else:
        return False


def func(string, n):
   A_score = 0
   B_score = 0
   

   ind = round(n/2)
   
   while string.count('0') > 0:
       if (string.count('0') % 2 != 0) and is_palindrome(string):
           string = string[:ind] + '1' + string[ind + 1:]
           A_score += 1
           
           string = string.replace('0', '1', 1)
           B_score += 1 
           
           flag = 0
           
       elif (string.count('0') % 2 == 0) and is_palindrome(string): 
           string = string.replace('0', '1', 1)
           A_score += 1
           
           string = string[::-1]
           flag = 1
           
       elif not is_palindrome(string) and flag != 1:
           string = string[::-1]
           
           string = string.replace('0', '1', 1)
           B_score += 1
           flag = 0
           
       elif not is_palindrome(string) and flag == 1:
           string = string.replace('0', '1', 1)
           A_score += 1
           flag = 0
           
           if is_palindrome(string):
               string = string.replace('0', '1', 1)
               B_score += 1
               
           else:
               string = string[::-1]
               flag = 1
   
   if n == 1:
       return 'BOB'
    
   
   if A_score > B_score:
       return 'BOB'
   elif A_score < B_score:
       return 'ALICE'
   else:
       return 'DRAW'
   
string = '11000011'
ans = func(string, 8)

def main():
    n_cases = int(parse_input())
    for i in range(n_cases):
        n = int(parse_input())
        string = parse_input()
        print(func(string, n))
        
if __name__ == "__main__":
    main()