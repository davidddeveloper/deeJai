from auth.spotify_auth import sp

def search_song():
    results = sp.search(q='love', limit=10)
    return results