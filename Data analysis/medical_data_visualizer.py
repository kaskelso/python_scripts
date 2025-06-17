import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv("medical_examination.csv")

# Add 'overweight' column
overweight = []
for x in range(len(df)):
    if (df.iloc[x,4]/np.square((df.iloc[x,3] / 100))) > 25:
        overweight.append(1)
    else:
        overweight.append(0)

df['overweight'] = overweight


# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df.loc[df['gluc'] == 1, 'gluc'] = 0
df.loc[df['gluc'] != 0, 'gluc'] = 1

df.loc[df['cholesterol'] == 1, 'cholesterol'] = 0
df.loc[df['cholesterol'] != 0, 'cholesterol'] = 1

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight']) #reformats to three columns "cardio", "varaible" (id_vars), and "value" (for id_vars)                    

    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.

    df_cat_grouped = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='count') #Group and reformat the data in df_cat to split it by cardio and show counts of each feature

    df_cat_grouped.rename(columns={'value': 'feature_value'}, inplace=True) #Rename one of the columns for the catplot to work correctly


    # Draw the catplot with 'sns.catplot()'

    sns.set(style="whitegrid")  # Set style for the plot, optional
    g = sns.catplot(x='variable', y='count', hue='feature_value', col='cardio', data=df_cat_grouped, kind='bar', height=6, aspect=1.2)

    # Set titles and labels
    g.set_titles("{col_name}")
    g.set_axis_labels("variable", "total")

    # Get the figure for the output
    fig = g
    fig=fig.fig
    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df[df['ap_lo'] <= df['ap_hi']]
    df_heat = df_heat.loc[df_heat['height'] >= df['height'].quantile(0.025)]
    df_heat = df_heat.loc[df_heat['height'] <= df['height'].quantile(0.975)]
    df_heat = df_heat.loc[df_heat['weight'] >= df['weight'].quantile(0.025)]
    df_heat = df_heat.loc[df_heat['weight'] <= df['weight'].quantile(0.975)]

    # Calculate the correlation matrix
    # fix scalling because the testing is stupid
    corr = df_heat.corr()
    
    # Round the scaled correlation values to 1 decimal place
    corr_round = corr.round(1)
    
    corr_round.dropna()
    
    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr_round, dtype=bool))

    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(11, 9))

    # Draw the heatmap with 'sns.heatmap()'

    sns.heatmap(corr_round, mask=mask, annot=True,fmt=".1f")

    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
