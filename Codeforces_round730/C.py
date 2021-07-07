#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 17:36:22 2021

@author: hienpham
"""
import os
import math
import sys


parse_input = lambda: sys.stdin.readline().rstrip("\r\n")

class dp:
    def __init__(self):
        self.d = []
        self.scale = 10**6
        

    def func(self, c, m, p, v):
        
        return self.expected_Race(c, m, p, v)
    
    
    def expected_Race(self, c, m, p, v):
        ans = p/self.scale
        if c > 0:
            if c > v:
                if m > 0:
                    prob = self.expected_Race(c-v, m+v/2, p+v/2, v)
                    self.d.append(prob)
                    ans += c*(1 + prob)/self.scale
                else:
                    prob = self.expected_Race(c-v, 0, p+v, v)
                    self.d.append(prob)
                    ans += c*(1 + prob)/self.scale
            else:
                if m > 0:
                    prob = self.expected_Race(0, m+c/2, p+c/2, v)
                    self.d.append(prob)
                    ans += c*(1 + prob)/self.scale
                else:
                    prob = self.expected_Race(0, 0, p+c, v)
                    self.d.append(prob)
                    ans += c*(1 + prob)/self.scale
        
        if m > 0:
            if m > v:
                if c > 0:
                    prob = self.expected_Race(c+v/2, m-v, p+v/2, v)
                    self.d.append(prob)
                    ans += m*(1 + prob)/self.scale
                else:
                    prob = self.expected_Race(0, m-v, p+v, v)
                    self.d.append(prob)
                    ans += m*(1 + prob)/self.scale
            else:
                if c > 0:
                    prob = self.expected_Race(c+m/2, 0, p+m/2, v)
                    self.d.append(prob)
                    ans += m*(1 + prob)/self.scale
                else:
                    prob = self.expected_Race(0, 0, p+m, v)
                    self.d.append(prob)
                    ans += m*(1 + prob)/self.scale
        return ans
        

c, m, p, v = 0.4998, 0.4998, 0.0004, 0.1666
scale = 10**6
c, m, p, v = round(c*scale), round(m*scale), round(p*scale), round(v*scale)
ans = dp().expected_Race(c, m, p, v)

def main():
    n_cases = int(parse_input())
    for i in range(n_cases):
        c, m, p, v = [int(i) for i in parse_input().split()]
        print(dp().func(c, m, p, v))
        
if __name__ == "__main__":
    main()