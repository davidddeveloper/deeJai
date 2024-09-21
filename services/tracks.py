"""
    tracks.py: fetch tracks for a query
"""
from auth.spotify_auth import sp
from helpers.tempo import get_spotify_track_bpm


def fetch_tracks_with_bpm(query):
    """
        return array of tracks for a search query
    """
    results = sp.search(q=query, type='track', limit=50)
    tracks = []
    for item in results['tracks']['items']:
        track_id = item['id']
        bpm = get_spotify_track_bpm(track_id)
        tracks.append({
            'id': track_id,
            'name': item['name'],
            'artist': item['artists'][0]['name'],
            'bpm': bpm,
            'uri': item['uri']
        })
    return tracks
