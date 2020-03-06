"""
This library fetches playlist from the given spotify
playlist ID using spotify's own API and formats
it to be interfaced with model.py and get_pred.py
to get predictions/suggestions for users.
"""

#TO DO

import requests, time, os
import pandas as pd
from pandas.io.json import json_normalize
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from functools import reduce
import operator

client_credentials_manager = SpotifyClientCredentials()
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def spotify_playlist_tracks(playlist_id):
    """
    Takes a spotify playlist ID and returns a pandas dataframe 
    containing the artist name, album name, track name, and track id.
    
    """
    
    offset = 0
    track_listings = []
    
    touch = sp.playlist_tracks(playlist_id, 
                               fields="track(name%2C%20id%2C%20album(name))", 
                               limit = 1, offset = 0, market='ES')
    
    num_listings = touch['total']  # see how many total songs in the playlist

    for ii in range(0,num_listings, 100):
        tracks = sp.playlist_tracks(playlist_id, 
                                    fields="track(name%2C%20id%2C%20album(name))", 
                                    limit = 100, offset = ii, market='ES')
        while tracks:
            for i, track in enumerate(tracks['items']):
                track_listings.append([tracks['items'][i]['track']['artists'][0]['name'],
                                       tracks['items'][i]['track']['album']['name'], 
                                       tracks['items'][i]['track']['name'], 
                                       tracks['items'][i]['track']['id']])

            if tracks['next']:
                tracks = sp.next(tracks)
            else:
                tracks = None
                
        time.sleep(0.3) #To make sure we don't abuse spotify's API terms
        
    columns = ['artist', 'album', 'track', 'track_id']

    track_listings_df = pd.DataFrame(track_listings, columns = columns)
        
    return track_listings_df

def spotify_track_features(track_ids):
    """
    Takes a list of spotify track IDs and returns a pandas dataframe 
    containing various features of each track.
    
    """
    
    track_features = []
    
    for ii in range(0, len(track_ids), 100):
        if ii <= (len(track_ids)-100):
            track_features.append(sp.audio_features(track_ids[ii:ii+100]))
        else:
            track_features.append(sp.audio_features(track_ids[ii:]))
            
        time.sleep(0.2)
    
    track_features = reduce(operator.add, track_features)
    
    track_features = list(filter(None, track_features)) # Makes sure there are no NoneType in the list, 
                                                        # this happens when API returns nothing for given ID.
    track_features_df = json_normalize(track_features) # Turn JSON format to pandas dataframe
        
    return track_features_df

def pull_songs_and_feats(playlist_id):
    """
    Takes a playlist ID and automates calling and merging the 
    track identifiers with the track features.
    
    """
    
    track_df = spotify_playlist_tracks(playlist_id)
    
    track_ids = list(track_df['track_id'])
    
    track_features_df = spotify_track_features(track_ids)
    
    playlist_tracks = track_df.merge(track_features_df, how = 'right', 
                                     left_on = 'track_id', right_on = 'id')
    
    playlist_tracks = playlist_tracks.drop(columns = ['id', 'uri', 'track_href', 
                                                      'analysis_url', 'type'])
    playlist_tracks = playlist_tracks.drop_duplicates()

    playlist_tracks = playlist_tracks.sample(n=5)
    
    return playlist_tracks