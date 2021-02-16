import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id='27223774c22643fb937e2919a348cbf8',client_secret='ab8b84c8e4f44235b1fd21a6d61fa394', redirect_uri='http://localhost:8888/callback',scope='user-library-read' ))

results = sp.current_user_saved_tracks()
for idx, item in enumerate(results['items']):
    track = item['track']
    print(idx, track['artists'][0]['name'], '=', track['name']
    )