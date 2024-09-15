import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="0e6ced6cd3a24f5c9be763a90a054bf4",
                                                           client_secret="90b246aaf2554ff489833c95360dc155"))

results = sp.search(q='weezer', limit=20)
for idx, track in enumerate(results['tracks']['items']):
    print(idx, track['name'])