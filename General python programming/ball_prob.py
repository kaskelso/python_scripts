#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 16:40:30 2024

@author: kennyaskelson
"""

import copy
import random

class Hat:
    def __init__(self, **kwargs):
        self.contents = self._generate_contents(kwargs)

    def _generate_contents(self, colors):
        contents = []
        for color, quantity in colors.items(): #.items() views python dictionary
            contents.extend([color] * quantity) #extend appends lists
        return contents
    def draw(self, times):
        if times > len(self.contents):
            sub_sample = random.sample(self.contents, len(self.contents))
        else:
            sub_sample = random.sample(self.contents, times)
        for color in sub_sample:
            self.contents.remove(color)
        return sub_sample

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    n_positive_tests = 0
    for i in range(num_experiments):
        if num_balls_drawn > len(hat.contents):
            num_balls_drawn = len(hat.contents)
        test = random.sample(hat.contents, num_balls_drawn)
        all_colors_found = True
        for ball in expected_balls:
            if test.count(ball) < expected_balls.get(ball, 0):
                all_colors_found = False
                break

        if all_colors_found:
            n_positive_tests += 1
    return n_positive_tests / num_experiments
        
       