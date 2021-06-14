#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 16:48:02 2021

@author: hienpham
"""

import os
import math
import sys
from collections import Counter


parse_input = lambda: sys.stdin.readline().rstrip("\r\n")


def is_palindrome(string):
    return string == string[::-1]

def func(string):
    a = Counter(string)
    if a['a'] == len(string):
        return 'NO', ''
    
    i = 0
    while i < len(string):
        string_out = string[:i] + 'a' + string[i:]
                
        if not is_palindrome(string_out):
            ans = 'YES'
            return ans, string_out
        else:
            i += 1
            ans = 'NO'
            string_out = ''
        
    return ans, string_out


def main():
    n_cases = int(parse_input())
    for i in range(n_cases):
        string = parse_input()
        ans, string_out = func(string)
        if ans == 'YES':
            print("{}\n{}".format(ans, string_out))
        else:
            print(ans)
        
if __name__ == "__main__":
    main()