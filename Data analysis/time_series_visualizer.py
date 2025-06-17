#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 16:02:45 2024

@author: kennyaskelson
"""

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv")

# Clean data

df_clean = df.loc[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]

df = df_clean

def draw_line_plot():
    # Draw line plot
    x_data = df_clean['date']
    y_data = df_clean['value']

    # Plotting
    fig = plt.figure()
    plt.plot(x_data, y_data)  # Line plot with markers
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')




    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_clean[['year','month', 'day']] = df_clean['date'].str.split('-',expand=True)
    df_clean["month"] = pd.to_numeric(df_clean["month"])
    
    months = {
    1: 'January',
    2: 'February',
    3: 'March',
    4: 'April',
    5: 'May',
    6: 'June',
    7: 'July',
    8: 'August',
    9: 'September',
    10: 'October',
    11: 'November',
    12: 'December'
}
    
    df_clean['month'] = df_clean['month'].map(months) #use dictrionary to replace!
    
    month_order = list(months.values())  # Order of months
    
    df_clean['month'] = pd.Categorical(df_clean['month'], categories=month_order, ordered=True)
    
    df_reformat = df_clean.groupby(['year', 'month'])['value'].mean().unstack() #Gets the mean value for each month by year, then converts to long format
    
    # Plotting
    df_bar, ax = plt.subplots(figsize=(10, 6))
    df_reformat.plot(kind='bar', ax=ax)

    # Customize labels and titles
    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')
    ax.legend(title='Months')

    # Rotate x-axis labels for better readability
    plt.xticks(rotation=45)

    # Display the plot
    plt.tight_layout()
    plt.show()
                
    
    df_bar = df_bar

    # Draw bar plot
    fig = df_bar

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df_clean.copy()
    
    df_box[['year','month', 'day']] = df_box['date'].str.split('-',expand=True)
    df_box["month"] = pd.to_numeric(df_box["month"])
    
    months = {
    1: 'Jan',
    2: 'Feb',
    3: 'Mar',
    4: 'Apr',
    5: 'May',
    6: 'Jun',
    7: 'Jul',
    8: 'Aug',
    9: 'Sep',
    10: 'Oct',
    11: 'Nov',
    12: 'Dec'
}
    
    df_box['month'] = df_box['month'].map(months) #use dictrionary to replace!
    
    # Convert 'month' column to categorical with custom order
    month_order = list(months.values())  # Order of months
    
    df_box['month'] = pd.Categorical(df_box['month'], categories=month_order, ordered=True)

    # Draw box plots (using Seaborn)
    plt.figure(figsize=(12, 6))
    
    plt.subplot(1, 2, 1)  # Create the first subplot
    
    plot1 = sns.boxplot(data=df_box, x="year", y="value")
    
    plot1.set_xlabel("Year", fontsize=12)  # Change x-axis label
    plot1.set_ylabel("Page Views", fontsize=12)  # Change y-axis label
    plot1.set_title('Year-wise Box Plot (Trend)')
    
    plt.subplot(1, 2, 2)  # Create the second subplot
    
    plot2 = sns.boxplot(data=df_box, x="month", y="value")
    
    plot2.set_xlabel("Month", fontsize=12)  # Change x-axis label
    plot2.set_ylabel("Page Views", fontsize=12)  # Change y-axis label
    plot2.set_title('Month-wise Box Plot (Seasonality)')

    fig = plt.gcf()

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
