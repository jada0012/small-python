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
wordsid = "3wIise6ZTbuO4L88mj6YRh"
insid = "704usGUCin8p2D0emnMQQd"

def get_playlist_tracks(playlist_id):
    results = sp.playlist_tracks(playlist_id)
    tracks = results['items']
    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])
    print(results.keys())
    return tracks

# with open("tracksininstrumental.txt", "w") as f:
#     for track in get_playlist_tracks(insid):
#         trackid  = track['track']['id']
#         if trackid is not None:
#             f.write(trackid)
#             f.write("\n")

with open("tracksinwords.txt", "w") as f:
    for track in get_playlist_tracks(wordsid):
        trackid  = track['track']['id']
        if trackid is not None:
            f.write(trackid)
            f.write("\n")