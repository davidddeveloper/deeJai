import librosa

filename = librosa.example('nutcracker')

y, sr = librosa.load('/workspaces/deeJai/tutorial/librosa/gaga.mp3')


tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)

time_stamps = librosa.frames_to_time(beat_frames, sr=sr)

print(time_stamps)