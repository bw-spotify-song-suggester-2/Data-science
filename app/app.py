"""
Data science API App that gives song/artist recommendations 
based on users' playlist of choice.
"""


from flask import Flask, request, render_template, jsonify
from dotenv import load_dotenv
# from .fetch_playlist import *
# from .model import Predictor
# from models import NNeighClassifier
# from flask_sqlalchemy import SQLAlchemy
# from decouple import config

load_dotenv()
def create_app():
    app = Flask(__name__)
    # app.config['SQLALCHEMY_DATABASE_URI'] = config('SQLALCHEMY_URI')
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

    #Initialise Database
    # db = SQLAlchemy(app)

    @app.route("/")
    def home():
        """Root page, you shoud not land here.
        
        Returns:
            string -- Provides link to project home.
        """
        return render_template('home.html')

    @app.route("/request/", methods=['GET', 'POST'])
    def search(user_input=None):
        """Takes in user input and predicts top recommended songs
        
        Keyword Arguments:
            playlist ID
        
        Returns:
            A list of recommended songs
        """
        user_input = str(request.args['search'])
        #TO DO
        #1 fetch playlist and format
        #2 get predictions
        #3 get info from database
        # tracks = pull_songs_and_feats(playlist_id=user_input)

        # knnmodel = Predictor()
        # pred_distances, pred_indices = knnmodel.predict(user_input=tracks)
        if user_input is not None:
            rec_file = open('model/recommendations.json', 'r')
        return rec_file
    
    return app

        