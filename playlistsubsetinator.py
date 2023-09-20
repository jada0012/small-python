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

def get_user_playlists():

    results = sp.current_user_playlists()
    playlists = results['items']
    while results['next']:
        results = sp.next(results)
        playlists.extend(results['items'])
    return playlists


# x = get_user_playlists()
# create_playlist_name = input("enter the name of the playlist you'd like to create!")
# playlist_name = input("enter the playlsit you'd like to find")

# playlist_found = False
# for playlist in x:
#     # print(playlist.keys())
#     if playlist['name'] == playlist_name:
#         playlist_found = True
#         PLAYLIST_ID = playlist['id']

# if playlist_found == True:
#     print(f"found! the id is {PLAYLIST_ID}")
# else:
#     print("not found, check spelling!")
playlists = sp.current_user_playlists()

playlist_choice = pyin.inputYesNo("create new playlist? ")
if playlist_choice == "yes":
    new_pname = input("enter the name of playlist. ")
    sp.user_playlist_create(user="5kbehkqoyiok15qrj7uxo55d4", name=new_pname )
    for i in playlists['items']:
        if i['name'] == new_pname:
            PLAYLIST_ID =  i['id']
else:
    searchornot =pyin.inputYesNo("do you have a direct link to the playlist in question?")
    if searchornot=="yes":
        list_id = input("enter the id for the playlist. ")
        first = list_id.rfind("/")
        end = list_id.rfind("?")
        PLAYLIST_ID = list_id[first+1:end]
    else: 
        playlist_tosearch = input("enter the name of the playlist. ")
        found= False
        for i in playlists['items']:
            print(i['name'])
            if i['name'] == playlist_tosearch:
                found = True
                PLAYLIST_ID = i['id']
        if found is False:
            print("playlist not found. start over. ")


INSTRUMENTAL_ID = "704usGUCin8p2D0emnMQQd"
# print(PLAYLIST_ID)
num_songchoice = pyin.inputYesNo("do you want to change the number of songs to add per playlist? ")
if num_songchoice == "yes":
    num_songs = pyin.inputInt("enter the number of songs you want")
else:
    num_songs=9
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
clear = input("start again from scratch?")
if clear == "yes":
    sp.playlist_replace_items(playlist_id=PLAYLIST_ID, items=[])
    
songs = input("enter a list of the genres you want from the following list: bubblegrunge, jazz, words, postrock, rockstone, soca, spanish, eurobeat, grime, lofipop, feels80, stoner, gothicsymphonic, reggae")
songlist = songs.split(" ")
print(songlist)
for i in songlist:
    if i != "":
        with open("%s.txt" %i, "r") as f:
            instrumentals = f.readlines()

        instrumentals = [x.rstrip() for x in instrumentals]
        li_inst = range(0, len(instrumentals))
        chosen = random.sample(li_inst, num_songs)
        chosen_id = []

        for i in chosen:
            chosen_id.append(instrumentals[i])
        max = 100
        div_lists = [chosen_id[i:i+max] for i in range(0, len(chosen_id), max)] #this splits up the list into increments of 100 
        for i in div_lists:
            sp.playlist_add_items(playlist_id=PLAYLIST_ID, items=i)