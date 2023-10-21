import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
load_dotenv()


SCOPE= "user-read-private, playlist-modify-private, playlist-modify-public, playlist-read-private, user-library-read, user-read-currently-playing, user-follow-modify, user-follow-read, user-read-recently-played"

sp =  spotipy.Spotify(auth_manager = SpotifyOAuth(client_id=os.getenv('CLIENT_ID'), client_secret=os.getenv('CLIENT_SECRET'), redirect_uri="https://example.com", scope = SCOPE))


PLAY_ID = "6teIxagDTKhx7qjkrZNHjj"
SECOND_ID = "5KLpzXadbD3poek1wkjTKd"
def get_playlist_tracks(playlist_id):
    results = sp.playlist_tracks(playlist_id)
    tracks = results['items']
    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])
    print(results.keys())
    return tracks
n = 600
max = 100
my_list = []
for j in get_playlist_tracks(PLAY_ID):
    if j is not None:
        my_list.append(j['track']['id'])
print("done making big list")
final = [my_list[i * n:(i + 1) * n] for i in range((len(my_list) + n - 1) // n )] 
print (final[0])
print("done splitting list")
bruh = final[-1]
div_lists = [bruh[i:i+max] for i in range(0, len(bruh), max)] #this splits up the list into increments of 100 
print("done dividing list")

for i in div_lists:
    sp.playlist_add_items(playlist_id=PLAY_ID, items=i)