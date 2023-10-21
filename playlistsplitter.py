import os
import datetime
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import random
import pyinputplus as pyin

load_dotenv()
SCOPE= "user-read-private, playlist-modify-private, playlist-modify-public, playlist-read-private, user-library-read, user-read-currently-playing, user-follow-modify, user-follow-read, user-read-recently-played"
sp =  spotipy.Spotify(auth_manager = SpotifyOAuth(client_id=os.getenv('CLIENT_ID'), client_secret=os.getenv('CLIENT_SECRET'), redirect_uri="https://example.com", scope = SCOPE))
# for i in range(10):
    # print(playlists['items'][i]['owner'])
# playlist_dict= {}
# songs = playlists['items']
# for i in songs:
#     if i['owner']['display_name'] == "jada":
#         playlist_dict[i['name']] = i['id']
# print(playlist_dict)
# while playlists['next']:
    
#     print(sp.next(playlists))
# def get_playlists():
#     results = sp.current_user_playlists()
#     songs = results['items']
#     while results['next']:
#         songs = sp.next(results)
#         songs.extend(results['items'])
#     return songs
# print(get_playlists())

def get_playlist_tracks(playlist_id):
    results = sp.playlist_tracks(playlist_id)
    tracks = results['items']
    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])
    # print(results.keys())
    return tracks
playlist_id = input("enter the id of the playlist you want to split")
p_nickname = input("enter a short nickname for this playlist")
first = playlist_id.rfind("/")
end = playlist_id.rfind("?")
PLAYLIST_ID = playlist_id[first+1:end]
num_songs = int(input("enter the number of songs you want each sublist to have"))
output = get_playlist_tracks(PLAYLIST_ID)

id_list = []
for i in output:
    id_list.append([i['track']['id'], i["added_at"][:10]])
    # print(i['added_at'])
# for i in id_list:
#     print(i)
sublists = [id_list[i:i+num_songs] for i in range(0, len(id_list), num_songs)]
for count, sublist in enumerate(sublists):
    # print(i)
    only_ids = []
    playlist_name = f"{count+1}: {p_nickname} {sublist[0][-1]} to {sublist[-1][-1]}"
    # print(playlist_name)
    sp.user_playlist_create(user = "5kbehkqoyiok15qrj7uxo55d4", name=playlist_name)
    playlists = sp.current_user_playlists()

    playlist_dict= {}
    songs = playlists['items']
    for i in songs:
        if i['owner']['display_name'] == "jada":
            playlist_dict[i['name']] = i['id']
    # # sp.playlist_add_items()
    NEWPLAYLIST_ID = playlist_dict[playlist_name]
    print(NEWPLAYLIST_ID)

    #changes id-date tuple to a list with only ids
    for pair in sublist:
        only_ids.append(pair[0])
    
    split_ids = [only_ids[num:num+100] for num in range(0, len(only_ids), 100)]
    for id_list in split_ids:
        sp.playlist_add_items(playlist_id=NEWPLAYLIST_ID, items=id_list)


        
    # # print(only_ids)
    # print(i)