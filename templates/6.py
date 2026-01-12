"""Матеха (гцд/лцм + проверка простоты)"""

import math

a, b = map(int, input().split())
g = math.gcd(a,b)
l = a//g*b

def prime(x):
    if x < 2: return False
    i = 2
    while i*i <= x:
        if x % i == 0:
            return False
        i += 1
    return True
