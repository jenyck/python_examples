#!/usr/bin/env python3
'''Counting frequency of all symbols in given file'''

with open('esenin.txt', encoding='utf-8').read().lower() as s:
    d = {x:s.count(x) for x in sorted(set(s)) if x.isalpha()}
    res = sum(d[i] for i in sorted(d, key=lambda x: d[x]))
    for i in sorted(d, key=lambda x: d[x]):
        print(f'{i}: {d[i]:5.0f} - {(d[i] / res * 100):7.4f}%')
    print('Total symbols:', res)
