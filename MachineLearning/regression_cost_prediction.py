#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  1 14:27:03 2025

@author: kennyaskelson
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import tensorflow as tf

from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.layers import LeakyReLU


import tensorflow_docs as tfdocs
import tensorflow_docs.plots
import tensorflow_docs.modeling

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder


#wget https://cdn.freecodecamp.org/project-data/health-costs/insurance.csv
dataset = pd.read_csv('insurance.csv')
dataset.tail()

encoder = OneHotEncoder(drop='first', sparse_output=False)  # drop='first' avoids multicollinearity
categorical_cols = ['sex', 'smoker', 'region']

# Convert categorical columns
X_encoded = encoder.fit_transform(dataset[categorical_cols])

# Convert to DataFrame and merge with the original dataset
X_encoded_df = pd.DataFrame(X_encoded, columns=encoder.get_feature_names_out(categorical_cols))
X_encoded_df = pd.concat([X_encoded_df, dataset[['age', 'bmi', 'children']]], axis=1)

# Split features (X) and target (y)
y = dataset['expenses']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_encoded_df, y, test_size=0.2, random_state=42)

# Standardize the features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model = tf.keras.Sequential([                            
    tf.keras.layers.Dense(128, activation=LeakyReLU()),
    tf.keras.layers.Dense(64, activation=LeakyReLU()),
    tf.keras.layers.BatchNormalization(),
    tf.keras.layers.Dense(32, activation=LeakyReLU()),
    tf.keras.layers.Dense(1)      # Output layer with 1 classes
])


# Compile the model
model.compile(optimizer='adam',
              loss='mean_squared_error', metrics=['mae'])

# Train the model
history = model.fit(X_train, y_train, epochs=200, batch_size=64, validation_split=0.1)

model.evaluate(X_test, y_test)


#Plots

loss, mae = model.evaluate(X_test, y_test, verbose=2)

print("Testing set Mean Abs Error: {:5.2f} expenses".format(mae))

if mae < 3500:
  print("You passed the challenge. Great job!")
else:
  print("The Mean Abs Error must be less than 3500. Keep trying.")

# Plot predictions.
test_predictions = model.predict(X_test).flatten()

a = plt.axes(aspect='equal')
plt.scatter(y_test, test_predictions)
plt.xlabel('True values (expenses)')
plt.ylabel('Predictions (expenses)')
lims = [0, 50000]
plt.xlim(lims)
plt.ylim(lims)
_ = plt.plot(lims,lims)