from sklearn.cluster import KMeans
from yellowbrick.cluster import KElbowVisualizer
import pandas as pd

# Import
df = pd.read_csv('track_master_df.csv')

# Specify X
feature_cols = df.select_dtypes(include='number').columns.tolist()
X = df[feature_cols].iloc[1:]

# Instantiate the clustering model and visualizer
model = KMeans()
visualizer = KElbowVisualizer(model, k=(4,21))

visualizer.fit(X) # Fit the data to the visualizer
visualizer.show() # Finalize and render the figure
