#!/usr/bin/env python3
'''Задача на отработку метода двух указателей.
https://informatics.msk.ru/mod/statements/view.php?chapterid=2827#1'''
_ = input()
n = [int(i) for i in input().split()]
_ = input()
m = [int(i) for i in input().split()]

ansn = 0
ansm = 10**8
j = 0
for item in n:
    # Двигаем указатель на число из второго массива,
    # пока оно не станет больше текущего из первого
    while item > m[j] and j < len(m) - 1:
        j += 1
    # Проверяем оба ближайших к текущему в первом массиве числа
    # из второго массива: большее и меньшее
    if abs(m[j] - item) < abs(ansm - ansn):
        ansm = m[j]
        ansn = item
    if abs(m[j-1] - item) < abs(ansm - ansn):
        ansm = m[j-1]
        ansn = item

print(ansn, ansm)
