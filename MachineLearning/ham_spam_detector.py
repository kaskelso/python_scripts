# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import tensorflow as tf
import pandas as pd
from tensorflow import keras
import tensorflow_datasets as tfds
import numpy as np
import matplotlib.pyplot as plt
import re
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras import regularizers


train_file_path = "train-data.tsv"
test_file_path = "valid-data.tsv"

df_train = pd.read_table("train-data.tsv")
df_test = pd.read_table("valid-data.tsv")

df_train.columns = ['label','sms']
df_test.columns = ['label','sms']


# Function to clean text
def clean_text(text):
    text = re.sub(r'<.*?>', '', text)  # Remove HTML tags
    text = re.sub(r'[^a-zA-Z\s]', '', text)  # Remove non-alphabet characters
    return text.lower().strip()

# Clean the reviews
df_train['sms'] = df_train['sms'].apply(clean_text)

df_test['sms'] = df_test['sms'].apply(clean_text)



#### DONT REPEAT TOKENIZER ON TEST DATA IT CREATES MISMATCH AND LOW ACCURACY ####

# Tokenization and padding
tokenizer = Tokenizer(num_words=1000, oov_token='<OOV>')
tokenizer.fit_on_texts(df_train['sms'])
sequences = tokenizer.texts_to_sequences(df_train['sms'])
padded_sequences = pad_sequences(sequences, maxlen=100)

sequences_test = tokenizer.texts_to_sequences(df_test['sms'])
padded_sequences_test = pad_sequences(sequences_test, maxlen=100)

X_train = padded_sequences
X_test = padded_sequences_test 

# Convert labels to binary integers
label_map = {'ham': 0, 'spam': 1}
df_train['label'] = df_train['label'].map(label_map)
df_test['label'] = df_test['label'].map(label_map)

# Now extract again after conversion
y_train = df_train["label"].astype('float32')
y_test = df_test["label"].astype('float32')


model = tf.keras.Sequential([
    tf.keras.layers.Embedding(1000, 32),
    tf.keras.layers.LSTM(400),
    tf.keras.layers.Dense(256, activation='relu'),
    tf.keras.layers.Dropout(0.5),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

model.compile(
    loss='binary_crossentropy',
    optimizer='adam',
    metrics=['accuracy']
)

history = model.fit(X_train, y_train, epochs=5, validation_split=0.2)

model.evaluate(X_test, y_test)


def predict_message(pred_text):
    pred_text_num = tokenizer.texts_to_sequences([pred_text])

    pred_text_num_pad = pad_sequences(pred_text_num, maxlen=100)

    prediction = model.predict(pred_text_num_pad).flatten()

    if prediction > 0.5:
        outcome = "spam"
    else:
        outcome = "ham"

    output = []

    output.append(float(prediction[0]))

    output.append(outcome)


    return (output)

pred_text = "how are you doing today?"

prediction = predict_message(pred_text)
print(prediction)




