import pandas as pd
import numpy as np
from sklearn.cluster import KMeans

# Import
df = pd.read_csv('track_master_df.csv')

# Use only the numerical data
features = df.columns[4:]
df_cont = df[features]

# Fit model
kmeans = KMeans(n_clusters=10)
kmeans.fit(df_cont)

# Create labels
labels = kmeans.labels_

# Append cluster labels to dataframe
new_series = pd.Series(labels)
df_cont['clusters'] = new_series.values
print(df_cont.head())

# Calculate each cluster's centroid
centroids = df_cont.groupby('clusters').mean()
print(centroids)
