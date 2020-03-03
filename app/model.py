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

loaded_model = pickle.load(open('model\knnpickled', 'rb'))

class Predictor():
    def __init__(self, model=None):
        self.model = loaded_model

    def predict(self, user_input=None, size=10):
        pass