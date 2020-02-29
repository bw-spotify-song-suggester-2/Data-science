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

def predict(self, user_input=None, size=5):

    
# TO DO