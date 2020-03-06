"""
Data science API App that gives song/artist recommendations 
based on users' playlist of choice.
"""


from flask import Flask, request, render_template, jsonify, json
from flask_cors import CORS
from dotenv import load_dotenv
from .fetch_playlist import *
from .model import *

load_dotenv()
def create_app():
    app = Flask(__name__)
    CORS(app)

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
        tracks = pull_songs_and_feats(playlist_id=user_input)

        knnmodel = Predictor()
        recommendations = knnmodel.predict(user_input=tracks)
        return recommendations

    return app

        