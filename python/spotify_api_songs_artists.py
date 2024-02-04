import numpy as np
import pandas as pd
from tqdm import tqdm
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

file_string = "/home/brent/Documents/github/my_spotify/data/processed/spotify.csv"
songs_artists_string = "/home/brent/Documents/github/my_spotify/data/processed/songs_artists.csv"

data = pd.read_csv(file_string)

# Login to api
# requires spotify credientials stored in SPOTIPY_CLIENT_ID and SPOTIPY_CLIENT_SECRET
# enviornment variables. In turn, those require a spotify developer account and app.
api = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

unique_songs = data["spotify_track_uri"].drop_duplicates().reset_index(drop=True)

print("THIS IS A TEST")
unique_songs = unique_songs[0:103]


dfs = []
for chunk in tqdm(np.array_split(unique_songs, (len(unique_songs)/50)+1)):
    result = api.tracks(chunk)['tracks']

    for song in result:
        df = pd.DataFrame({"song_uri":song["uri"], 
                           "artist_uris":pd.DataFrame(song["artists"])["uri"].to_list()})
        dfs.append(df)

songs_artists = pd.concat(dfs, ignore_index=True)

songs_artists.to_csv(songs_artists_string)