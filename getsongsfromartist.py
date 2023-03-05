import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
load_dotenv()

SCOPE= "user-read-private, playlist-modify-private, playlist-modify-public, playlist-read-private, user-library-read, user-read-currently-playing, user-follow-modify, user-follow-read, user-read-recently-played"
sp =  spotipy.Spotify(auth_manager = SpotifyOAuth(client_id=os.getenv('CLIENT_ID'), client_secret=os.getenv('CLIENT_SECRET'), redirect_uri="https://example.com", scope = SCOPE))


urlentered = input("enter the artist id. ")
first = urlentered.rfind("/")
end = urlentered.rfind("?")
print(first)
print(end)
ARTIST_ID = urlentered[first+1:end]

print(ARTIST_ID)

NAME = sp.artist(ARTIST_ID)['name']
print(NAME)
options = ['album', 'single']
sp.user_playlist_create(
    user="5kbehkqoyiok15qrj7uxo55d4",
    name = f"{NAME}: the complete discography"
   
)


playlists = sp.current_user_playlists()
for i in playlists['items']:
    if i['name'] == f"{NAME}: the complete discography":
        PLAYLIST_ID =  i['id']
def get_artist_albums(id, album_type):
    results = sp.artist_albums(id, album_type=album_type)
    albums = results['items']
    while results['next']:
        results = sp.next(results)
        albums.extend(results['items'])
    return albums
tracklist = []
addedtoplaylist = []
for option in options:
    for i in get_artist_albums(ARTIST_ID, option):
        for j in sp.album_tracks(i['id'])['items']:
            if j is not None:
                tracklist.append(j['id'])
n = 100
x = [tracklist[i:i+n] for i in range(0, len(tracklist), n)]  
for i in x:
    sp.playlist_add_items(playlist_id=PLAYLIST_ID, items=i)



