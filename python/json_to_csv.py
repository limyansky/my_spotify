import glob
import pandas as pd

file_string = "/home/brent/Documents/github/my_spotify/data/raw/Spotify Extended Streaming History/*Audio*"
output_string = "/home/brent/Documents/github/my_spotify/data/processed/spotify.csv"

files = glob.glob(file_string)

dfs = []
for file in files:
    data = pd.read_json(file)
    dfs.append(data)

spotify = pd.concat(dfs, ignore_index=True)

spotify.to_csv(output_string)
