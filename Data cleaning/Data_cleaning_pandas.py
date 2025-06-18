#### ML work on DataTalksClub ML ZoomCamp ####

import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

pd.__version__

df = pd.read_csv("laptops.csv")

len(df)

#2160

df.head()

len(df['Brand'].unique())

#27

for i in df.columns.tolist():
    print(f"{i}: {df[i].isna().any()}")


# 3 with NA's

df['Final Price'].max()

df_Dell = df.loc[df['Brand'] == 'Dell'] 

df_Dell['Final Price'].max()

#3936.0
 
df['Screen'].median()

df['Screen'].mode()

df['Screen'] = df['Screen'].fillna(15.6)

df['Screen'].median()

# Median is the same

df_keep = df.loc[df['Brand'] == 'Innjoo'] 


df_keep = df_keep[['RAM', 'Storage', 'Screen']]

df_keep_array = df_keep.to_numpy()

flipped = df_keep_array.T

XTX = df_keep_array.T @ df_keep_array

inverse_matrix = np.linalg.inv(XTX)

values = np.array([1100, 1300, 800, 900, 1000, 1100])

sum(inverse_matrix @ flipped @ values)

#91.29988062995753
