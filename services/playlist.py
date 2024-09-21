"""
    playlist: generate a playlist with similar bpm
"""
from services.tracks import fetch_tracks_with_bpm
from pprint import pprint

def generate_compatible_playlist(tracks, bpm_tolerance=5):
    """
        return a playlist with similar bpm with a tolerance of 5
    """
    if not tracks:
        return []
    
    sorted_tracks = sorted(tracks, key=lambda x: x['bpm'])
    playlist = [sorted_tracks[0]]
    
    for track in sorted_tracks[1:]:
        if abs(track['bpm'] - playlist[-1]['bpm']) <= bpm_tolerance:
            playlist.append(track)
    
    return playlist

# result = generate_compatible_playlist(fetch_tracks_with_bpm('ariana granda'))
# pprint(result)
