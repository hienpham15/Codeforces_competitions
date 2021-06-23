#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 07:38:54 2021

@author: hienpham
"""
import sys

sys.setrecursionlimit(10**6)

parse_input = lambda: sys.stdin.readline().rstrip("\r\n")


def check_k(k_arr, left, right, i):

    k = k_arr[i]
    a_l, b_l = left[i][0], left[i][1]
    a_r, b_r = right[i][0], right[i][1]
    
    if k >= a_l and k <= b_l:
        c = 0
    else:
        c = 3
    
    if k >= a_r and k <= b_r and c != 0:
        c = 1
    elif k >= a_r and k <= b_r and c == 0:
        c = 2  
    return c


def check_hand(left_hand, right_hand, left, right, i):
    a_l, b_l = left[i][0], left[i][1]
    a_r, b_r = right[i][0], right[i][1]
    
    if left_hand >= a_l and left_hand <= b_l:
        l = 0
    else:
        l = 1
    
    if right_hand >= a_r and right_hand <= b_r:
        r = 0
    else:
        r = 1  
    return l, r


def func(n_cases, m, k_arr, left, right, left_hand=0, right_hand=0):
    # note: only need to trace back 1 level
    left_false = False
    
    left_array = [0]
    right_array = [0]
    
    i = 0
    arr = [None]*n_cases
    while i < n_cases:
        
        if k_arr[i] > m:
            return 'No', None

        c = check_k(k_arr, left, right, i)
        l, r = check_hand(left_hand, right_hand, left, right, i)
        
        if c == 3:
            return 'No', None
        
        if c == 0:
            if r == 0:
                left_hand = k_arr[i]
                left_array.append(left_hand)
                arr[i] = 0
                i += 1
            elif r == 1 :
                if i > 0:
                    i -= 1
                    if len(left_array) > 2:
                        left_array.pop()
                        left_hand = left_array.pop()
                    else:
                        left_hand = left_array[0]
                    left_false = True
                else:
                    return 'No', None
                
        elif c == 1:
            if l == 0:
                right_hand = k_arr[i]
                right_array.append(right_hand)
                arr[i] = 1
                i +=1
            elif l == 1:
                if i > 0:
                    i -= 1
                    if len(right_array) > 2:
                        right_array.pop()
                        right_hand = right_array.pop()
                    else:
                        right_hand = right_array[0]
                    left_false = True
                else:
                    return 'No', None
        
        elif c == 2:
            if left_false:
                right_hand = k_arr[i]
                right_array.append(right_hand)
                arr[i] = 1
                i += 1
                
            else:
                if r == 0:
                    left_hand = k_arr[i]
                    left_array.append(left_hand)
                    arr[i] = 0
                    i += 1
                elif r == 1 and l == 0:
                    right_hand = k_arr[i]
                    right_array.append(right_hand)
                    arr[i] = 1
                    i +=1
                elif r == 1 and l == 1:
                    return 'No', None
                
            left_false = False
            
    
    if arr[n_cases - 1] != None:
        return 'Yes', arr


#n_cases, m = 2, 1000
#k_arr = [2, 3]
#left = [[0, 10], [3, 3]]
#right = [[1, 99], [3, 5]]
#ans, arr = func(n_cases, m, k_arr, left, right)


def main():
    n_cases, m = [int(i) for i in parse_input().split()]
    k_arr = []
    left = []
    right = []
    for i in range(n_cases):
        k = int(parse_input())
        a_l, b_l = [int(i) for i in parse_input().split()]
        a_r, b_r = [int(i) for i in parse_input().split()]
        
        k_arr.append(k)
        left.append([a_l, b_l])
        right.append([a_r, b_r])
        
 
    ans, arr = func(n_cases, m, k_arr, left, right)
    if ans == 'Yes':
        print(ans)
        print(*arr)
    else:
        print(ans)
    
if __name__ == "__main__":
    main()