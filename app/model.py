"""
This library interfaces with the pickled model.
"""

import os
import pickle
import pandas as pd
import numpy as np


###################
##BUILD PREDICTOR##
###################

class Predictor():
    def __init__(self, model=None):
        self.model = load_file('model')

    def predict(self, user_input=None, size=10):
        pass

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

params = {
    'model': 'knnpickled'
}