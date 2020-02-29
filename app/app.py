"""
Data science API App that gives song/artist recommendations 
based on users' playlist of choice.
"""


from flask import Flask, request, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from decouple import config
from flask_sqlalchemy import SQLAlchemy
from pickle import load


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = config('SQLALCHEMY_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

    #Initialise Database
    db = SQLAlchemy(app)

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
        
        return jsonify(song_list)


        