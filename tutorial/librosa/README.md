# librosa

> librosa: is a python library for interacting and extracting music information.

    y, sr = librosa.load('/workspaces/deeJai/tutorial/librosa/gaga.mp3')

>`wave` : an array containg the actual wave signal data of the audio. In the example above y is the wave.

>`sr`: `sampling rate` - is the number of samples of the audio signal captured per second, measured in Hertz (Hz).

    tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)

>`tempo`: refer to the estimate speed or pace of the music measure in beat per minute(`BPM`) - an array
>`beat_frames`: numbers representing the actual point in the audio where the beats occur. - an array

    beat_times = librosa.frames_to_time(beat_frames, sr=sr)

>`beat_times`: the actual timestamp in seconds where the beat occurred in the audio.