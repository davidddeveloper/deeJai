"""
    tempo: get the tempo using librosa module
"""
import librosa
from auth.spotify_auth import sp


def analyze_bpm(file_path):
    """ return the tempo (BPM)
    """
    y, sr = librosa.load(file_path)
    tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
    return tempo

def get_spotify_track_bpm(track_id):
    audio_features = sp.audio_features(tracks=[track_id])[0]

    # Extract the tempo (BPM)
    tempo = audio_features.get('tempo')
    return tempo