#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 10:47:41 2021

@author: hienpham
"""
import os
import math
import sys


parse_input = lambda: sys.stdin.readline().rstrip("\r\n")



def func(n_cases, shop_list, total_items):
    total_pay = 0
    n_items = 0
    shop_list = sorted(shop_list)
    i = 0
    j = n_cases - 1
    
    while n_items < total_items:
        p1 = list(shop_list[i])
        p2 = list(shop_list[j])
        
        n_buy = p2[1]
        req_disc = p1[0]

        buy_more = req_disc - n_items
        
        if n_items >= req_disc:
            total_pay += 1*p1[1]
            n_items += p1[1]
            i += 1
        else:
            if buy_more > 0 and buy_more < n_buy:
                total_pay += 2*buy_more
                n_items += buy_more
                
                shop_list[j][1] -= buy_more 
                """
                n_item_disc = n_buy - buy_more
                
                total_pay += 1*n_item_disc
                n_items += n_item_disc
                
                j -= 1
                """
            else:
                total_pay += 2*n_buy
                n_items += n_buy
                j -= 1
    return total_pay

#n_cases = 2
#shop_list = [[7, 7], [4, 1]]
#total_items = 8
#ans = func(n_cases, shop_list, total_items)


def main():
    n_cases = int(parse_input())
    shop_list = []
    total_items = 0
    for i in range(n_cases):
        a, b = [int(i) for i in parse_input().split()]
        shop_list.append([b, a])
        total_items += a
    print(func(n_cases, shop_list, total_items))
        
if __name__ == "__main__":
    main()