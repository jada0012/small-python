import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
load_dotenv()

SCOPE= "user-read-private, playlist-modify-private, playlist-modify-public, playlist-read-private, user-library-read, user-read-currently-playing, user-follow-modify, user-follow-read, user-read-recently-played"
sp =  spotipy.Spotify(auth_manager = SpotifyOAuth(client_id=os.getenv('CLIENT_ID'), client_secret=os.getenv('CLIENT_SECRET'), redirect_uri="https://example.com", scope = SCOPE))

NAME = sp.artist("7AC976RDJzL2asmZuz7qil")['name']
print(NAME)

sp.user_playlist_create(
    user="5kbehkqoyiok15qrj7uxo55d4",
    name = f"the complete discography of {NAME}"
   
)
playlists = sp.current_user_playlists()
for i in playlists['items']:
    if i['name'] == f"the complete discography of {NAME}":
        PLAYLIST_ID =  i['id']
def get_artist_albums(id):
    results = sp.artist_albums(id, album_type='album')
    albums = results['items']
    while results['next']:
        results = sp.next(results)
        albums.extend(results['items'])
    return albums
tracklist = []

for i in get_artist_albums("7AC976RDJzL2asmZuz7qil"):
    for j in sp.album_tracks(i['id'])['items']:

        if j is not None:
            tracklist.append(j['id'])
            # # sp.playlist_add_items(playlist_id=PLAYLIST_ID, items=tracklist)
            if len(tracklist) == 100:
                sp.playlist_add_items(playlist_id=PLAYLIST_ID, items=tracklist)
                tracklist = []
            
            
sp.playlist_add_items(playlist_id=PLAYLIST_ID, items=tracklist)


