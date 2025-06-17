#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 14:34:48 2024

@author: kennyaskelson
"""

import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.figure(figsize=(14, 6))

    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')

    # Create first line of best fit
    slope, intercept, r, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    
    df_2000 = df.loc[df['Year'] >= 2000]

    slope_2000, intercept_2000, r_2000, p_value_2000, std_err_2000 = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])

    # Calculate the sea level rise for each year in the future
    years_future = range(1880, 2051)
    
    sea_level_future = slope * years_future + intercept
    
    years_future_2 = range(2000, 2051)
    
    sea_level_future_2 = slope_2000 * years_future_2 + intercept_2000
    
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='Sea Level')

    plt.plot(years_future, sea_level_future, color='red', label='Line of Best Fit (full)')
    
    plt.plot(years_future_2, sea_level_future_2, color='green', label='Line of Best Fit (2000)')
    
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()