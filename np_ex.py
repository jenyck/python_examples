#!/usr/bin/env python3

import numpy as np

a = np.array([[1,2], [3+5j, 0+1.42j]], dtype=complex)
print(a)

a = np.zeros((4, 11))
print(a)

a = np.eye(10)
print(a)

a = np.ones((5, 3, 3))
print(a)

def f1(i, j, k):
    return i**3 + j**2 + 50*k

a = np.fromfunction(f1, (6, 5, 7))
print(a)

a = np.arange(10.125, 12.875, 0.025)
print(a)

a = np.linspace(10.125, 12.875, 111)
print(a)
