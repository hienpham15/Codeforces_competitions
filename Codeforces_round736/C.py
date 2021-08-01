#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 21:57:20 2021

@author: hienpham
"""
import os
import math
import sys
import copy
 
 
parse_input = lambda: sys.stdin.readline().rstrip("\r\n")
 
 
def create_relationship(n, m, u, v):
    relationship = {}
    for i in range(n):
        relationship[str(i+1)] = []
    
    for j in range(m):
        relationship[str(u[j])].append(str(v[j]))
        relationship[str(v[j])].append(str(u[j]))
    return relationship
 
 
def add_friend(relationship, u, v):
    relationship[str(u)].append(str(v))
    relationship[str(v)].append(str(u))
    return relationship
 
 
def remove_friend(relationship, u, v):
    relationship[str(u)].remove(str(v))
    relationship[str(v)].remove(str(u))
    return relationship
 
 
def process(n, relationship):
    s2d = copy.deepcopy(relationship)
    
    i = 1
    while i <= n:
        if s2d[str(i)]:
            for val in relationship[str(i)]:
                if val not in s2d:
                    s2d[str(i)].remove(val)
            
            if s2d[str(i)]:
                del s2d[str(i)]
                
        i += 1
            
    n_survivors = len(s2d)
    return n_survivors
 
"""
n, m = 4, 3
u = [2, 1, 3]
v = [1, 3, 4]
relationship = create_relationship(n, m, u, v)
relationship = add_friend(relationship, 2, 3)
relationship = remove_friend(relationship, 3, 1)
ans = process(n, relationship)
"""
 
def main():
    n, m = [int(i) for i in parse_input().split()]
    u, v = [], []
    for i in range(m):
        u_i, v_i = [int(i) for i in parse_input().split()]
        u.append(u_i)
        v.append(v_i)
        
    relationship = create_relationship(n, m, u, v)
    s2d = copy.deepcopy(relationship)
    q = int(parse_input())
    for j in range(q):
        t = [int(i) for i in parse_input().split()]
        if t[0] == 3:
            ans = process(n, s2d)
            print(ans)
        elif t[0] == 1:
            s2d = add_friend(s2d, t[1], t[2])
        elif t[0] == 2:
            s2d = remove_friend(s2d, t[1], t[2])
            
if __name__ == "__main__":
    main()