import time
from auth.spotify_auth import sp
from helpers.duration import get_track_duration

def crossfade_tracks(current_track_uri, next_track_uri, track_id, crossfade_duration=5):
    # This is a simplified example. Actual implementation would require controlling playback.
    sp.start_playback(uris=[current_track_uri])
    time.sleep(get_track_duration(track_id) - crossfade_duration)
    sp.start_playback(uris=[next_track_uri], position_ms=0)
    # Implement volume control via Spotify API if possible


