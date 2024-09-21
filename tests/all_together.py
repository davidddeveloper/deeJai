from services.playlist import generate_compatible_playlist
from services.tracks import fetch_tracks_with_bpm
from services.search_song import search_song
from dj.crossfading import crossfade_tracks


playlist = generate_compatible_playlist(fetch_tracks_with_bpm('ariana'))
crossfade_tracks(playlist[0].get('uri'), playlist[1].get('uri'), playlist[0].get('id'))