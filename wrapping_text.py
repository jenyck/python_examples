#!/usr/bin/env python3
"""Wrapping in file from standard input

Wraps all the lines in given file to be 78 symbols long
"""
import textwrap
import fileinput

for fileinput_line in fileinput.input():
    print(textwrap.fill(fileinput_line, 78))
