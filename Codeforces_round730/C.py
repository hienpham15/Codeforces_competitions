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
        
    def draw(self, x, y, p, v, count=2, carry=1):
        ans = p/self.scale
    
        if x == 0 and y == 0:
            return ans
        if x > 0:

            if x-v > 0:
                self.d.append(x*(p+v/2)*count*carry)
                carry *= x
                prob = self.draw(x-v, y+v/2, p+v/2, v, count+1, carry)
                ans += x*(1 + prob)/self.scale
            else:
                self.d.append(x*(p+x/2)*count*carry)
                carry *= x
                prob = self.draw(0, y+x/2, p+x/2, v, count+1, carry)
                ans += x*(1 + prob)/self.scale
        else:
            if y-v > 0:
                self.d.append(y*(p+v)*count*carry)
                carry *= y 
                prob = self.draw(0, y-v, p+v, v, count+1, carry)
                ans += y*(1 + prob)/self.scale
            else:
                self.d.append(y*(p+y)*count*carry)
                carry *= y
                prob = self.draw(0, 0, p + y, v, count+1, carry)
                ans += y*(1 + prob)/self.scale
        return ans
    

    def func(self, c, m, p, v):
        p1 = self.draw(c, m, p, v)
        p2 = self.draw(m, c, p, v)
    
        return p/self.scale + p1 + p2
    
    
    def expected_Race(self, c, m, p, v):
        ans = p/self.scale
        if c > 0:
            if c > v:
                if m > 0:
                    prob = self.expected_Race(c-v, m+v/2, p+v/2, v)
                    ans += c*(1 + prob)/self.scale
                else:
                    prob = self.expected_Race(c-v, 0, p+v, v)
                    ans += c*(1 + prob)/self.scale
            else:
                if m > 0:
                    prob = self.expected_Race(0, m+c/2, p+c/2, v)
                    ans += c*(1 + prob)/self.scale
                else:
                    prob = self.expected_Race(0, 0, p+c, v)
                    ans += c*(1 + prob)/self.scale
        
        if m > 0:
            if m > v:
                if c > 0:
                    prob = self.expected_Race(c+v/2, m-v, p+v/2, v)
                    ans += m*(1 + prob)/self.scale
                else:
                    prob = self.expected_Race(0, m-v, p+v, v)
                    ans += m*(1 + prob)/self.scale
            else:
                if m > 0:
                    prob = self.expected_Race(c+m/2, 0, p+m/2, v)
                    ans += m*(1 + prob)/self.scale
                else:
                    prob = self.expected_Race(0, 0, p+m, v)
                    ans += m*(1 + prob)/self.scale
        return ans
        

c, m, p, v = 0.3125, 0.6561, 0.0314, 0.2048
scale = 10**6
c, m, p, v = round(c*scale), round(m*scale), round(p*scale), round(v*scale)
ans1 = dp().expected_Race(c, m, p, v)
ans2 = dp().func(c, m, p, v)

def main():
    n_cases = int(parse_input())
    for i in range(n_cases):
        c, m, p, v = [int(i) for i in parse_input().split()]
        print(dp().func(c, m, p, v))
        
if __name__ == "__main__":
    main()