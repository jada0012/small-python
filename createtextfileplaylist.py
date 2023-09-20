import os
import datetime
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import random
import math
import pyinputplus as pyin
load_dotenv()
SCOPE= "user-read-private, playlist-modify-private, playlist-modify-public, playlist-read-private, user-library-read, user-read-currently-playing, user-follow-modify, user-follow-read, user-read-recently-played"
sp =  spotipy.Spotify(auth_manager = SpotifyOAuth(client_id=os.getenv('CLIENT_ID'), client_secret=os.getenv('CLIENT_SECRET'), redirect_uri="https://example.com", scope = SCOPE))
print("welcome to the player-sub-set-inator!!!")

PLAYLIST_ID = "704usGUCin8p2D0emnMQQd"
soca = "6B4bqDU5hinMJqP9AQQiGH"
postrock = "0uerlzoLgWept7L2kxEAxl"
spanish = "6OZnFZeYBAEzddPWznIUY4"
rockstone = "1hdHfEloXZG4VgbbUuxAVB"
eurobeat = "5PlkqpUUojNiRUW4B38ZgI"
grime = "6CHeeaWdvaeaUz7xTKhAAc"
filename=  "bruh"
def get_playlist_tracks(playlist_id):
    results = sp.playlist_tracks(playlist_id)
    tracks = results['items']
    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])
    return tracks

def writetofile(playlist_id, nameoffile):

    with open("%s.txt" %nameoffile, "w") as f:
        print("this works!")
        for track in get_playlist_tracks(playlist_id):
            trackid  = track['track']['id']
            if trackid is not None:
                f.write(trackid)
                f.write("\n")
    print(f"done creating {nameoffile} playlist!!")

list_id = input("enter the id for the playlist. ")
name_file = input("what do you want the text file to be named? ")
first = list_id.rfind("/")
end = list_id.rfind("?")
LIST_ID = list_id[first+1:end]
writetofile(LIST_ID, name_file)