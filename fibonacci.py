#!/usr/bin/env python3
'''Prints sum of the odd fibonacci numbers under 4 million'''

n1 = 1
n2 = 2
n3 = 0
total = 2

while n3 < 4_000_000:
    n3 = n1 + n2
    print('Fibonacci:', n3)

    n1 = n2
    n2 = n3
    if not n3 % 2:
        total += n3
        print(total)
