#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 15:09:10 2024

@author: kennyaskelson
"""

from __future__ import absolute_import, division, print_function, unicode_literals

import tensorflow as tf

import pandas as pd

import numpy as np

CSV_COLUMN_NAMES = ['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth', 'Species']
SPECIES = ['Setosa', 'Versicolor', 'Virginica']
# Lets define some constants to help us later on

train_path = tf.keras.utils.get_file(
    "iris_training.csv", "https://storage.googleapis.com/download.tensorflow.org/data/iris_training.csv")
test_path = tf.keras.utils.get_file(
    "iris_test.csv", "https://storage.googleapis.com/download.tensorflow.org/data/iris_test.csv")

train = pd.read_csv(train_path, names=CSV_COLUMN_NAMES, header=0)
test = pd.read_csv(test_path, names=CSV_COLUMN_NAMES, header=0)

train_y = train.pop('Species') #train.pop selects column and drops it from dataframe
test_y = test.pop('Species')
train.head() # the species column is now gone

feature_columns = []
for col in train.columns:
    feature_columns.append(tf.feature_column.numeric_column(col))
 
model = tf.keras.Sequential([                           # Sequential just means info goes left to right through layers
    tf.keras.layers.Dense(30, activation='relu'),       # First hidden layer with 30 nodes
    tf.keras.layers.Dense(10, activation='relu'),       # Second hidden layer with 10 nodes
    tf.keras.layers.Dense(3, activation='softmax')      # Output layer with 3 classes
])

# Compile the model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Train the model
model.fit(train, train_y, epochs=500, shuffle=True)

model.evaluate(test, test_y)

indv = train.iloc[0].values

# Reshape indv to match the expected input shape of your model
indv = indv.reshape(1, -1)

# Make prediction
prediction = model.predict(indv)

# Convert the prediction to a human-readable label
predicted_label = SPECIES[np.argmax(prediction)]

print("Predicted class:", predicted_label)

#Says it is 99.9% to be Virginica! Amazing!
