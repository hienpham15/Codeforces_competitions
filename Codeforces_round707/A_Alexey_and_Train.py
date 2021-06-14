#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 10:00:43 2021

@author: hienpham
"""
import os 
import math
import sys


parse_input = lambda: sys.stdin.readline().rstrip("\r\n")


def func(n_stations, a, b, extra_time):
    depart_time = []
    depart_time.append(0)
    for i in range(n_stations):
        
        if i == 0:
            arrival_time = a[i] + extra_time[i]
        else:
            travel_time = a[i] - b[i - 1] + extra_time[i]
            arrival_time =  travel_time + depart_time[i]
        
        stay_time = math.ceil((b[i] - a[i])/2)
        stay_check = arrival_time + stay_time
        
        if stay_check >= b[i]:
            depart_time.append(stay_check)
        else:
            depart_time.append(b[i])
        
    return arrival_time
    

#n = 5
#a = [1, 7, 9, 13, 19]
#b = [4, 8, 10, 15, 20]
#t = [1, 2, 3, 4, 5]

#func(n, a, b, t)
def main():
    n_cases = int(parse_input())
    
    for _ in range(n_cases):
        arrival = []
        depart = []
        n_stations = int(parse_input())
        for _ in range(n_stations):
            a, b = [int(i) for i in parse_input().split()]
            arrival.append(a)
            depart.append(b)
        extra_time = [int(i) for i in parse_input().split()]
        
        result = func(n_stations, arrival, depart, extra_time)
        
        print(result)
        
if __name__ == "__main__":
    main()