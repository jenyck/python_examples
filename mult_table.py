#!/usr/bin/env python3
'''Multiplication table of the entered number'''

n = int(input("Введите число: "))
for i in range(1, 11):
    print(n, "x", i, "=", n * i)
