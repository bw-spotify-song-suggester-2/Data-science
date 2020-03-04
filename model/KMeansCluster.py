import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split

# Import
df = pd.read_csv('track_master_df.csv')

# Use only the numerical data
features = df.columns[4:]
df_num = df[features].copy()

# Fit model
kmeans = KMeans(n_clusters=10)
kmeans.fit(df_num)

# Create labels
labels = kmeans.labels_

# Append cluster labels to dataframe
new_series = pd.Series(labels)
df_num['clusters'] = new_series.values

# Calculate each cluster's centroid
# centroids = df_num.groupby('clusters').mean()
# print(centroids)

# Specify X, y
X = df_num.drop(columns='clusters')
y = df_num['clusters']

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, stratify=y, test_size=0.33, random_state=42)
