"""
This library interfaces with the pickled model.
"""

import os
import pickle
import pandas as pd
import numpy as np
import operator
from sklearn.neighbors import NearestNeighbors
import category_encoders as ce
from .KMeansCluster import df_num as cluster_df
from .KMeansCluster import df as master_df
from .KMeansCluster import clean_dataframe


###################
##BUILD PREDICTOR##
###################

class Predictor():
    def __init__(self, model=None):
        self.model = load_file('model')
        
    def predict(self, user_input=None):
        """
        input: target playlist
        
        output: recommendations using a hybrid of random forest and nearest neighbors 
                models; json format.
        
        """
        X_test = clean_dataframe(df=user_input)
        
        predictions = self.model.predict(X_test)
        
        clusters = list(set(predictions))

        columns = ['artist', 'album', 'track', 'track_id']

        recommendations = pd.DataFrame(columns = columns)

        for cluster in clusters:
            
            count = list(predictions).count(cluster)
            
            X = cluster_df[cluster_df['clusters'] == cluster].drop(columns = 'clusters')

            knn = NearestNeighbors(n_neighbors=5, algorithm='brute').fit(X)

            distances, indices = knn.kneighbors(X_test)

            recommend_indices = []

            for ii, dists in enumerate(distances):
                for jj, val in enumerate(dists):
                    if (val > 0) & (val < 40):
                        recommend_indices.append((indices[ii][jj], int(round(val))))

            recommend_indices = sorted(recommend_indices, key = operator.itemgetter(1))

            ind, val = zip(*recommend_indices)

            recommendations = pd.concat([recommendations, master_df.iloc[list(ind[:count*2])][columns]])

            recommendations = recommendations.drop_duplicates()
            
            rec_json = recommendations.to_json(orient = 'table', index = False, force_ascii = False)
    
        return rec_json

######################
###Helper Functions###
######################

def get_abs_path(filename, **kwargs):
    if os.path.isfile(os.path.abspath(filename)):
        return os.path.abspath(filename)
    else:
        return os.path.join(
            os.getcwd(), 'app/model/'+filename,
        )
        
def load_file(file_key):
    with open(get_abs_path(params[file_key]), 'rb') as f:
        opened = pickle.load(f)
    return opened

##################
##SET PARAMETERS##
##################

params = {
    'model': 'randomforest.pkl'
}