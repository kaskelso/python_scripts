#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 09:15:55 2024

@author: kennyaskelson
"""
import numpy as np

def calculate(numbers):
    if len(numbers) != 9:
        raise ValueError("List must contain nine numbers.") #Raises issue or error
    output = {}
    table = np.array([
        numbers[:3], #0
        numbers[3:6], #1
        numbers[6:] #2
    ])
    flattened_table = table.flatten()
    output.update({'mean': [table.mean(axis=0).tolist(), table.mean(axis=1).tolist(), flattened_table.mean().tolist()]})
    output.update({'variance': [table.var(axis=0).tolist(), table.var(axis=1).tolist(), flattened_table.var().tolist()]})
    output.update({'standard deviation': [table.std(axis=0).tolist(), table.std(axis=1).tolist(), flattened_table.std().tolist()]})
    output.update({'max': [table.max(axis=0).tolist(), table.max(axis=1).tolist(), flattened_table.max().tolist()]})
    output.update({'min': [table.min(axis=0).tolist(), table.min(axis=1).tolist(), flattened_table.min().tolist()]})
    output.update({'sum': [table.sum(axis=0).tolist(), table.sum(axis=1).tolist(), flattened_table.sum().tolist()]})
    return output