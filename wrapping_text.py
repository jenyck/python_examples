#!/usr/bin/env python3
'''Wrapping in file from standard input'''
import textwrap
import fileinput

for fileinput_line in fileinput.input():
    print(textwrap.fill(fileinput_line, 78))
