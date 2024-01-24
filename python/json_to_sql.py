import glob
import pandas as pd
from sqlite3 import connect

file_string = "/home/brent/Documents/github/my_spotify/data/raw/Spotify Extended Streaming History/*Audio*"
output_string = "/home/brent/Documents/github/my_spotify/data/processed/spotify.db"

files = glob.glob(file_string)

dfs = []
for file in files:
    data = pd.read_json(file)
    dfs.append(data)

spotify = pd.concat(dfs, ignore_index=True)

conn = connect(output_string)

spotify.to_sql("spotify", conn)
