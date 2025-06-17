#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 31 16:47:44 2025

@author: kennyaskelson
"""

import numpy as np
import pandas as pd
from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors
import matplotlib.pyplot as plt

# get data files
#!wget https://cdn.freecodecamp.org/project-data/books/book-crossings.zip

#!unzip book-crossings.zip

books_filename = 'BX-Books.csv'
ratings_filename = 'BX-Book-Ratings.csv'

df_books = pd.read_csv(
    books_filename,
    encoding = "ISO-8859-1",
    sep=";",
    header=0,
    names=['isbn', 'title', 'author'],
    usecols=['isbn', 'title', 'author'],
    dtype={'isbn': 'str', 'title': 'str', 'author': 'str'})

df_ratings = pd.read_csv(
    ratings_filename,
    encoding = "ISO-8859-1",
    sep=";",
    header=0,
    names=['user', 'isbn', 'rating'],
    usecols=['user', 'isbn', 'rating'],
    dtype={'user': 'int32', 'isbn': 'str', 'rating': 'float32'})

# Merge on 'isbn'
#df_merged = pd.merge(df_ratings, df_books, on="isbn", how="inner")

# Display merged data
#print(df_merged.head())

# Get value counts of each ISBN
isbn_counts = df_ratings['isbn'].value_counts()

# Filter out ISBNs with fewer than 100 ratings
filtered_isbns = isbn_counts[isbn_counts >= 100].index

# Keep only rows with those ISBNs
df_ratings_filtered = df_ratings[df_ratings['isbn'].isin(filtered_isbns)]

# Get value counts of each User
user_counts = df_ratings['user'].value_counts()

# Filter out Users with fewer than 200 ratings
filtered_user = user_counts[user_counts >= 200].index

# Keep only rows with those ISBNs
df_ratings_filtered = df_ratings_filtered[df_ratings_filtered['user'].isin(filtered_user)]

# Reshape the dataframe, each column is isbn each row is user, the fill is ratings (missing is 0) then we flip the data frame
# so that rows are books and columns are users
ratings_matrix = df_ratings_filtered.pivot(index='user', columns='isbn', values='rating').fillna(0).T

df_merged = df_books[['isbn', 'title']].merge(
    ratings_matrix, on='isbn', how='right'
)

# Move 'BookTitle' to the first column
df_merged = df_merged.set_index('title')

df_merged = df_merged.drop(labels = 'isbn', axis = 1)

# Fit NearestNeighbors model .values just gives the data no columns or row names

nbrs = NearestNeighbors(n_neighbors=5, algorithm='auto', metric="cosine").fit(df_merged.values)

#grabs values for "Angels"
df_merged.loc["The Queen of the Damned (Vampire Chronicles (Paperback))"].values 

def get_recommends(book = ""):
    distances, indices = nbrs.kneighbors([df_merged.loc[book].values], n_neighbors=6)

#turns it into 1D array because can't slice 2D array
    distances = distances.flatten()

    indices = indices.flatten()

#drop first value because it is always the input book
    distances = distances[1:]

    indices = indices[1:]

#finds values in the df and puts them into list
    recommended_books_com = df_merged.iloc[indices].index.values.tolist()
    recommended_books_dist_com = distances.tolist()
    
    #reverses the order 
    recommended_books_com = recommended_books_com[::-1]
    recommended_books_dist_com = recommended_books_dist_com[::-1]
    
    recommended_books = recommended_books_com
    
    recommended_books_dist = recommended_books_dist_com
    
    recommendations = []

    for book, distance in zip(recommended_books_com, recommended_books_dist_com):
        recommendations.append([book, distance])
                
    return recommendations

books = get_recommends("Where the Heart Is (Oprah's Book Club (Paperback))")
print(books)