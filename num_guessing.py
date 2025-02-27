#!/usr/bin/env python3
'''Random number guessing game'''
import random
import time

def is_valid(a):
    '''Checks if given string represents number from [1;100]'''
    return int(a) in range(1, 101)

n = random.randint(1, 100)

print('Добро пожаловать в числовую угадайку!')
time.sleep(1)
print('Попробуйте угадать число от 1 до 100, которое я загадал...')
time.sleep(1.5)
print('Начнем!')

while True:
    n1 = input()

    if is_valid(n1):
        n1 = int(n1)
    else:
        print('Разве это - число от 1 до 100?!')
        continue

    if n1 > n:
        time.sleep(random.randint(5, 20) / 10)
        print('Хмм...')
        time.sleep(random.randint(5, 20) / 5)
        print('Ваше число больше загаданного, попробуйте еще разок')
    elif n1 < n:
        time.sleep(random.randint(5, 20) / 10)
        print('Хмм...')
        time.sleep(random.randint(5, 20) / 5)
        print('Ваше число меньше загаданного, попробуйте еще разок')
    else:
        print('Хмм...')
        time.sleep(random.randint(5, 20) / 5)
        print('ХММ...')
        time.sleep(3)
        print('Вы угадали,', end=' ')
        time.sleep(1)
        print('поздравляем!!!')
        time.sleep(1)
        print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
        time.sleep(3)
        break
