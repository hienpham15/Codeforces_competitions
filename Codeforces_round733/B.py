#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 17 16:54:49 2021

@author: hienpham
"""
import os
import math
import sys


parse_input = lambda: sys.stdin.readline().rstrip("\r\n")


def isValid(i, j, h, w, board):
    
    if i == 0:
        if j == 0 or j%2 == 0:
            return True
        else:
            return False
    
    elif i%2 == 1:
        if i == h - 1:
            if j == 0 or j == w-1:
                return False
            else:
                if board[i - 1][j]==0 and board[i-1][j+1]==0 and board[i-1][j-1]==0 \
                    and board[i][j-1]==0 and board[i][j+1] == 0:
                        return True
                else:
                    return False
        else:
            return False
    
    elif i%2 == 0:
        if i == h - 1:
            if j%2 == 0:
                return True
            else:
                return False
        else:
            if j == 0 or j == w-1:
                return True
            else:
                return False
            

def func(h, w):
    board = [[0 for i in range(w)] for j in range(h)]
    
    for i in range(h):
        for j in range(w):
            if isValid(i, j, h, w, board):
                board[i][j] = 1
    return board

#ans = func(9, 6)

def main():
    n_cases = int(parse_input())
    for i in range(n_cases):
        h, w = [int(i) for i in parse_input().split()]
        board = func(h, w)
        
        for i in range(h):
            print(*board[i], sep='')
        print(' ')
        
        
if __name__ == "__main__":
    main()