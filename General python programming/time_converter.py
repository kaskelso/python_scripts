#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 09:03:32 2023

@author: kennyaskelson
"""
#add_time("3:00 PM", "3:10")
# Returns: 6:10 PM


def add_time(start, duration, day = None):
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    x = start.split(" ")
    AM_PM = x[1]
    time = x[0].split(":")
    hours = int(time[0])
    minutes = int(time[1])
    y = duration.split(":")
    hours_add = int(y[0])
    minutes_add = int(y[1])
    if AM_PM == "PM":
        if hours in list(range(1, 12)):
            hours = hours + 12
        else:
            hours = hours
    if AM_PM == "AM":
        if hours == 12:
            hours = hours - 12
        else:
            hours = hours
    summed_hours = (hours + hours_add)
    summed_min = (minutes + minutes_add)
    if summed_min >= 60:
        summed_hours = summed_hours + 1
        print_min = summed_min - 60
    else:
        print_min = summed_min
    temp = (summed_hours / 24)
    first_digit = str(temp)[0]
    new_hours = summed_hours - (int(first_digit) * 24)
    if new_hours in list(range(13, 24)):
        print_hours = new_hours - 12
        print_AM_PM = "PM"
    elif new_hours in list(range(1, 12)):
        print_hours = new_hours
        print_AM_PM = "AM"
    elif new_hours == 12:
        print_hours = new_hours
        print_AM_PM = "PM"
    elif new_hours == 24:
        print_hours = new_hours - 12
    elif new_hours == 0:
            print_hours = new_hours + 12
            print_AM_PM = "AM"
    if int(first_digit) < 1:
        day_counter = ""
    elif int(first_digit) == 1:
        day_counter = "(next day)"
    elif int(first_digit) >= 2:
        day_counter = f'{"("}{int(first_digit)}{" days later)"}'
    if day == None:
        print_min = f"{print_min:02d}"
        print_hours = f"{print_hours:02d}"
        combine = ":".join([print_hours, print_min])
        new_time =  " ".join([combine, print_AM_PM, day_counter])
        new_time = new_time.rstrip()
        return new_time
    else:
        capitalized_day = day.capitalize()
        position = days_of_week.index(capitalized_day) + 1
        end_position = ((int(position) + int(first_digit)) % 7) - 1
        new_day = days_of_week[end_position]
        print_min = f"{print_min:02d}"
        print_hours = f"{print_hours:02d}"
        combine = ":".join([print_hours, print_min])
        combine1 =  " ".join([combine, print_AM_PM])
        combine2 = ", ".join([combine1, new_day])
        new_time = " ".join([combine2, day_counter])
        new_time = new_time.rstrip()
        return new_time