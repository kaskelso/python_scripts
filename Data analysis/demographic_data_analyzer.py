#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 10:54:52 2024

@author: kennyaskelson
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

adults = pd.read_csv("adult.data.csv")

adults.head()

race = adults['race']

len(race)

#count by race

adults.groupby('race').size()

adults[adults['sex'] == 'Male']['age'].mean() #one line filter to men and take average age

(len(adults[adults['education'] == 'Bachelors'])/32561) * 100 #percent have bachelors

#filter for advanced degrees

test1 = adults[(adults['education'] == 'Bachelors') | (adults['education'] == 'Masters') | (adults['education'] == 'Doctorate')]

#percent that make more than 50k

(len(test1[test1['salary'] == '>50K'])/len(test1)) * 100

#percent without advanced degrees 

test2 = adults[((adults['education'] != 'Bachelors') & (adults['education'] != 'Masters') & (adults['education'] != 'Doctorate'))]

(len(test2[test2['salary'] == '>50K'])/len(test2)) * 100


#min hours

adults['hours-per-week'].min()

#min hours more than >50k

test3 = adults[adults['hours-per-week'] == 1]

(len(test3[test3['salary'] == '>50K'])/len(test3)) * 100


#country with highest percent of >50k and percentage

test4 = adults.groupby(['native-country', 'salary']).size().reset_index(name='count')

# Calculate the total number of people from each country
total_per_country = adults.groupby('native-country').size().reset_index(name='total')

# Merge the counts and total_per_country DataFrames on the 'country' column
merged = pd.merge(test4, total_per_country, on='native-country')

merged_50k = merged[merged['salary'] == '>50K']

merged_50k['perc_more50K'] = merged_50k['count'] / merged_50k['total']

mask = merged_50k['perc_more50K'] > 0.418

merged_50k[mask]

#Iran 41.9%

#most popular occupation for India with >50k 

adult_india_50k = adults[(adults['native-country'] == 'India') & (adults['salary'] == '>50K')]

adult_india_50k.groupby('occupation').size()

#Prof-specialty