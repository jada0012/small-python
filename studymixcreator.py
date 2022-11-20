import os
import datetime
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import random
import math
import pyinputplus as pyin
load_dotenv()
id = '3wIise6ZTbuO4L88mj6YRh'
SCOPE= "user-read-private, playlist-modify-private, playlist-modify-public, playlist-read-private, user-library-read, user-read-currently-playing, user-follow-modify, user-follow-read, user-read-recently-played"
sp =  spotipy.Spotify(auth_manager = SpotifyOAuth(client_id=os.getenv('CLIENT_ID'), client_secret=os.getenv('CLIENT_SECRET'), redirect_uri="https://example.com", scope = SCOPE))
print("welcome to the study mix creator!")
id = '704usGUCin8p2D0emnMQQd'
insid = "704usGUCin8p2D0emnMQQd"
jazzid = "4tPkN6WF7d4XLVBLlIrFRW"
wordsid = "3wIise6ZTbuO4L88mj6YRh"

instr_type = pyin.inputMenu(['jazz', 'everything'], numbered=True)

num_ins = int(input("how many instumental songs do you want? "))
num_word = int(input("how many non-instumental songs do you want? "))
len_playlist = int(input("how many hours do you want the playlist to be? "))

num_iter = math.ceil(15/ (num_ins + num_word)) * len_playlist
playlists = sp.current_user_playlists()

for i in playlists['items']:
    if i['name'] == "big brain time":
        PLAYLIST_ID = i['id']
# def get_playlist_tracks(playlist_id):
#     results = sp.playlist_tracks(playlist_id)
#     tracks = results['items']
#     while results['next']:
#         results = sp.next(results)
#         tracks.extend(results['items'])
#     return tracks

with open("tracksinwords.txt", "r") as g:
    words = g.readlines()
words = [x.rstrip() for x in words]
li_words = range(0, len(words))

# with open("smoothjazz.txt", "w") as f:
#     for track in get_playlist_tracks(jazzid):
#         trackid  = track['track']['id']
#         if trackid is not None:
#             f.write(trackid)
#             f.write("\n")

if instr_type == "jazz":
    print("here")
    with open("smoothjazz.txt", "r") as e:
        jazz = e.readlines()

    jazz = [x.rstrip() for x in jazz]
    li_jazz = range(0, len(jazz))
    sp.playlist_replace_items(playlist_id=PLAYLIST_ID, items=[])
    for i in range(num_iter):
        chosen_instrumentals = random.sample(li_jazz, num_ins)
        chosen_instrumentals_id = []
        chosen_words = random.sample(li_words, num_word)
        chosen_words_id = []

        for i in chosen_instrumentals:
            chosen_instrumentals_id.append(jazz[i])

        for j in chosen_words:
            chosen_words_id.append(words[j])

        allchosen = chosen_instrumentals_id + chosen_words_id

        sp.playlist_add_items(playlist_id=PLAYLIST_ID, items = allchosen)

elif instr_type == 2:
    with open("tracksininstrumental.txt", "r") as f:
        instrumentals  = f.readlines()
    instrumentals = [x.rstrip() for x in instrumentals]
    li_instrumentals = range(0, len(instrumentals))
    







# sp.playlist_replace_items(playlist_id=PLAYLIST_ID, items=[])

# for i in range(num_iter):
#     chosen_instrumentals = random.sample(li_instrumentals, num_ins)
#     chosen_instrumentals_id = []
#     chosen_words = random.sample(li_words, num_word)
#     chosen_words_id = []

#     for i in chosen_instrumentals:
#         chosen_instrumentals_id.append(instrumentals[i])

#     for j in chosen_words:
#         chosen_words_id.append(words[j])

#     allchosen = chosen_instrumentals_id + chosen_words_id

#     sp.playlist_add_items(playlist_id=PLAYLIST_ID, items = allchosen)

