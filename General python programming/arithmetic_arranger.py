#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 13:32:23 2023

@author: kennyaskelson
"""

def arithmetic_arranger(problems, crunch=False):
    split_problems = []
    arranged_problems =[]
    top = []
    bottom = []
    lines = []
    for i in problems:
        if len(problems) > 5:
            return('Error: Too many problems.')
        elif len(problems) <= 5:
            x = i.split(" ")
            split_problems.append(x)
    first = []
    add_sub = []
    second = []
    for i in split_problems:
        first.append(i[0])
        add_sub.append(i[1])
        second.append(i[2])
    for x,y, in zip(first, second):
        if x.isnumeric() == False:
            return('Error: Numbers must only contain digits.')
        elif y.isnumeric() == False:
            return('Error: Numbers must only contain digits.')
    for x,y, in zip(first, second):
        if len(str(x)) > 4:
            return('Error: Numbers cannot be more than four digits.')
        elif len(str(y)) > 4:
            return('Error: Numbers cannot be more than four digits.')
    for i in add_sub:
        if i not in ('+', '-'):
            return("Error: Operator must be '+' or '-'.")
    for a, b, c in zip(first, add_sub, second):
        if len(a) < len(c):
            top.append(f'{" "*((len(str(c)) + 2) - len(str(a)))}{a}{" " * 4}') 
        elif len(a) >= len(c):
            top.append(f'  {a}{" " * 4}')
    for a, b, c in zip(first, add_sub, second):
        if len(c) >= len(a):
            bottom.append(f'{b} {c}{" " * 4}')
        elif (len(a) - len(c)) == 1 and len(c) == 2:
            bottom.append(f'{b}{" "*(len(str(a)) - 1)}{c}{" " * 4}')
        elif len(c) < len(a):
            bottom.append(f'{b}{" "*len(str(a))}{c}{" " * 4}')
    for x, z, in zip(first, second):
        if len(x) > len(z):
            lines.append(f'{"-"* (len(x) + 2)}{" " * 4}')
        elif len(x) < len(z):
            lines.append(f'{"-"* (len(z) + 2)}{" " * 4}')
        elif len(x) == len(z):
            lines.append(f'{"-"* (len(x) + 2)}{" " * 4}')
    top[-1] = top[-1].rstrip() + '\n'
    bottom[-1] = bottom[-1].rstrip() + '\n'
    lines[-1] = lines[-1].rstrip()
    top1 = "".join(top)
    bottom1 = "".join(bottom)
    lines1 = "".join(lines)
    tmp = [top1, bottom1, lines1]
    arranged_problems = ''.join(tmp)
    if bool(crunch) == True:
        result = []
        values = []
        lines[-1] = lines[-1] + "    "
        for x, y, z in zip(first, add_sub, second):
            if y == "+":
                result.append(int(x) + int(z))
            elif y == "-":
                result.append(int(x) - int(z))
        for a, b, in zip(result, lines):
            values.append(f'{" " * (((len(str(b)) - 4)) - len(str(a)))}{a}{" " * 4}')
        lines[-1] = lines[-1].rstrip() + '\n'
        lines1 = "".join(lines)
        values[-1] = values[-1].rstrip()
        values1 = "".join(values)
        tmp = [top1, bottom1, lines1, values1]
        arranged_problems = ''.join(tmp)
    print(arranged_problems)
    return(arranged_problems)


arithmetic_arranger(['32 - 698', '1 - 3801', '45 + 43', '123 + 49', '988 + 40'], True)