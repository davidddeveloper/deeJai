import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id='93da8bd3ffc245c1b8465d5f158bdd18',
    client_secret='90c75fbca08544c2a959962de692dd73'))