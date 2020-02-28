"""code to retrieve data from the database"""

import sqlite3


def song_info():
    """takes in the list of two arrays returned from the model
    and returns all the information about the songs in a list that
    can then be jsonified"""

    #connectiong to the database
    sl_conn = sqlite3.connect('database.sqlite3')
    sl_curs = sl_conn.cursor()


    #initalizing the list to be returned
    return_list = []
    
    #TO DO

    
    sl_curs.close()
    return return_list