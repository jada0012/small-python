import os
import datetime
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import random
load_dotenv()
current_date = datetime.datetime.now().strftime("%d-%b-%Y, %H:%M:%S")
id = '3wIise6ZTbuO4L88mj6YRh'
SCOPE= "user-read-private, playlist-modify-private, playlist-modify-public, playlist-read-private, user-library-read, user-read-currently-playing, user-follow-modify, user-follow-read, user-read-recently-played"
sp =  spotipy.Spotify(auth_manager = SpotifyOAuth(client_id=os.getenv('CLIENT_ID'), client_secret=os.getenv('CLIENT_SECRET'), redirect_uri="https://example.com", scope = SCOPE))
name = "morning playlist"
def get_playlist_tracks(playlist_id):
    results = sp.playlist_tracks(playlist_id)
    tracks = results['items']
    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])
    return tracks

playlists = sp.current_user_playlists()
for i in playlists['items']:
    # if i['name'] == f"{current_date} || morning training motivation":
    if i['name'] == name:
        PLAYLIST_ID =  i['id']

inplaylist = []
for track in get_playlist_tracks(id):
    trackid  = track['track']['id']
    inplaylist.append(trackid)

li = range(0, len(inplaylist))
chosen = random.sample(li,10)
chosenid = []
for i in chosen:
    chosenid.append(inplaylist[i])
sp.playlist_replace_items(playlist_id=PLAYLIST_ID, items=chosenid)