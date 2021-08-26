#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 16:58:07 2021

@author: hienpham
"""

import os
import math
import sys


parse_input = lambda: sys.stdin.readline().rstrip("\r\n")


def isPrime(num): 
    prime_flag = 0
    
    if(num > 1):
        for i in range(2, int(math.sqrt(num)) + 1):
            if (num % i == 0):
                prime_flag = 1
                break
        if (prime_flag == 0):
            return True
        else:
            return False
    else:
        return False


def notPrime(num):
    if num == 1:
        return True
    
    if not isPrime(num):
        return True
    else:
        return False


def dp(num, d):
    
    if len(num) == 1:
        if notPrime(int(num)):
            if 1 not in d:
                d.update({1:int(num)})
        return 
    else:
        for i in range(len(num)):
            new_num = num[:i] + num[i+1:]
            if notPrime(int(new_num)):
                if len(new_num) not in d:
                    d.update({len(new_num):int(new_num)})
                    dp(new_num, d)
                else:
                    return


def bottomUp(num, prev_num, d):
    for i in range(len(num)):
        check_num = prev_num + num[i]
        #new_num = num[:i] + num[i+1:]
       
        if notPrime(int(check_num)):
            d.update({len(check_num):int(check_num)})
            return 
        #else:
        #    bottomUp(new_num, prev_num, d)
         
    for i in range(len(num)):
        prev_num += num[i]
        new_num = num[:i] + num[i+1:]
        bottomUp(new_num, prev_num, d)
        
        if d:
            return
            

         
def func(k, n):
    n_str = str(n)
    d = {}
    
    #if notPrime(n):
    #    d[k] = n
    #dp(n_str, d)
    #key = list(d.keys())[-1]
    
    bottomUp(n_str, '', d)
    key = list(d.keys())[0]
    return key, d[key]

#k = 30
#n = 626221626221626221626221626221
#ans = func(k, n)


def main():
    n_cases = int(parse_input())
    for i in range(n_cases):
        k = int(parse_input())
        n = int(parse_input())
        n_left, digit = func(k, n)
        print(n_left)
        print(digit)
        
if __name__ == "__main__":
    main()