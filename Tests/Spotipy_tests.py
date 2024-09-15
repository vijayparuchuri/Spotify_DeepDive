import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os

try:
    from dotenv import load_dotenv
    load_dotenv('../.env')
except ImportError:
    print("python-dotenv not installed, using system environment variables")

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=os.environ.get('SPOTIFY_CLIENT_ID'),
                                                           client_secret=os.environ.get('SPOTIFY_CLIENT_SECRET')))

results = sp.search(q='weezer', limit=20)
for idx, track in enumerate(results['tracks']['items']):
    print(idx, track['name'])