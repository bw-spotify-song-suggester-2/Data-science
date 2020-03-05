"""
This library interfaces with the pickled model.
"""

import os
import pickle
import pandas as pd
import numpy as np
import operator


###################
##BUILD PREDICTOR##
###################

class Predictor():
    def __init__(self, model=None, df=None):
        self.model = load_file('model')
        self.df = pd.read_csv('app/model/track_master_df.csv')

    def predict(self, user_input=None, size=10):
        
        """
        nearest neighbors model and feature matrix passed, returns recommendations data

        """

        distances, indices = self.model.kneighbors(user_input)

        recommend_indices = []
        for ii, dists in enumerate(distances):
            for jj, val in enumerate(dists):
                if (val > 0) & (val < 50):
                    recommend_indices.append((indices[ii][jj], int(round(val))))

        recommend_indices = sorted(recommend_indices, key = operator.itemgetter(1))

        ind, val = zip(*recommend_indices) 

        columns = ['artist', 'album', 'track', 'trackid']

        recommendations = self.df.iloc[list(ind[:size])][columns]

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
    'model': 'knn_model.pkl'
}