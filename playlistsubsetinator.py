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
playlists = sp.current_user_playlists()

for i in playlists['items']:
    if i['name'] == "instrumental subset":
        PLAYLIST_ID = i['id']

INSTRUMENTAL_ID = "704usGUCin8p2D0emnMQQd"
print(PLAYLIST_ID)

def get_playlist_tracks(playlist_id):
    results = sp.playlist_tracks(playlist_id)
    tracks = results['items']
    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])
    return tracks

# with open("allinstrumentals.txt", "w") as f:
#     for track in get_playlist_tracks(INSTRUMENTAL_ID):
#         trackid  = track['track']['id']
#         if trackid is not None:
#             f.write(trackid)
#             f.write("\n")

with open("allinstrumentals.txt", "r") as f:
    instrumentals = f.readlines()

instrumentals = [x.rstrip() for x in instrumentals]
li_inst = range(0, len(instrumentals))
chosen = random.sample(li_inst, 200)
chosen_id = []

for i in chosen:
    chosen_id.append(instrumentals[i])
max = 100
div_lists = [chosen_id[i:i+max] for i in range(0, len(chosen_id), max)] #this splits up the list into increments of 100 
for i in div_lists:
    sp.playlist_add_items(playlist_id=PLAYLIST_ID, items=i)