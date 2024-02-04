import numpy as np
import pandas as pd
from tqdm import tqdm
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

file_string = "/home/brent/Documents/github/my_spotify/data/processed/songs_artists.csv"
artists_genres_string = "/home/brent/Documents/github/my_spotify/data/processed/artists_genres.csv"

data = pd.read_csv(file_string)

# Login to api
# requires spotify credientials stored in SPOTIPY_CLIENT_ID and SPOTIPY_CLIENT_SECRET
# enviornment variables. In turn, those require a spotify developer account and app.
api = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

unique_artists = data["artist_uris"].drop_duplicates().reset_index(drop=True)
unique_artists = unique_artists.dropna()

dfs = []
for chunk in tqdm(np.array_split(unique_artists, (len(unique_artists)/50)+1)):
    result = api.artists(chunk)['artists']

    for artist in result:
        df = pd.DataFrame({"artist_uri":artist["uri"],
                           "artist_genres":artist["genres"]})
        dfs.append(df)

songs_artists = pd.concat(dfs, ignore_index=True)

songs_artists.to_csv(artists_genres_string)
