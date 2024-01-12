# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 14:36:14 2022

@author: vpunyap
"""

def repeat(string, a, b, c, d, alpha, beta, gamma, zeta):
    arr = string.split(" ")
    arr = [int(x) for x in arr ]
    arr = [alpha * [i * a for i in arr]] + [beta * [i * b for i in arr]] + [gamma * [i * c for i in arr] + [zeta * [i * d for i in arr]]]
    new_arr = []
    for i in arr:
        new_arr += i
    ans = " ".join([str(_) for _ in new_arr])
    return ans


if __name__ == "__main__":
    string = "1 1 0"
    a = 5
    b = -5
    c = -4
    d = 3
    alpha = 8
    beta = 8
    gamma = 1
    zeta = 7
    result = repeat(string, a, b, c, d, alpha, beta, gamma, zeta) + (" 96*0.6")
    print(result)

