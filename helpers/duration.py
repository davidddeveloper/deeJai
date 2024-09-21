from auth.spotify_auth import sp


def get_track_duration(track_id):
    track = sp.track(track_id)
    duration_ms = track['duration_ms']
    return duration_ms / 1000  # Convert to seconds