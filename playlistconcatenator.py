import os

import sys
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
load_dotenv()
sys.path.insert(1, "D:\\python\\listen_to_this")
from listentothis import get_playlist_tracks

SCOPE= "user-read-private, playlist-modify-private, playlist-modify-public, playlist-read-private, user-library-read, user-read-currently-playing, user-follow-modify, user-follow-read, user-read-recently-played"
sp =  spotipy.Spotify(auth_manager = SpotifyOAuth(client_id=os.getenv('CLIENT_ID'), client_secret=os.getenv('CLIENT_SECRET'), redirect_uri="https://example.com", scope = SCOPE))

PLAYLIST_ID_WORDS = "3wIise6ZTbuO4L88mj6YRh"
PLAYLIST_ID_RANDOM = "5wBAJKSTtSAke2otg3DALr"
PLAYLIST_ID_METAL = "16ZMUy6y1JxjmLBkH2H1nF"


playlists = sp.user_playlists(user="f921itveupnl1921mxu9s8wr4")

# with open('wordsids.txt', 'w') as f:
#     for track in get_playlist_tracks(PLAYLIST_ID):
#         trackid = track['track']['id']
#         if isinstance(trackid, str):
#             f.write(trackid)
#             f.write("\n")
#i should read the first 50 or so tracks from random adn metalrock and if its not in the list of ids, then add it to words
with open('wordsids.txt') as f:
    inplaylist = [line.rstrip() for line in f]


def addtoplaylist(playlist_id):
    toadd = []
    for track in sp.playlist_tracks(playlist_id, limit=60):
        trackid = track['track']['id']
        if track not in inplaylist and isinstance(trackid, str):
            toadd.append(track['track'])
    with open('wordsids.txt', 'a') as g:
        for i in toadd:
            g.write(i)
            g.write('\n')
    sp.playlist_add_items(PLAYLIST_ID_WORDS, toadd)

addtoplaylist(PLAYLIST_ID_RANDOM)
addtoplaylist(PLAYLIST_ID_METAL)