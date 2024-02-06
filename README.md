# my_spotify: Dashboarding my Lifetime Spotify Listening
I built a [Tableau Dashboard](https://public.tableau.com/views/MySpotifyData_17066362308130/Dashboard12?:language=en-US&:display_count=n&:origin=viz_share_link) to analyze my lifetime Spotify streaming history. This repository contains some helper scripts I used for data processing/accessing the Spotify API, as well as a copy of the Tableau Desktop ".twb" file I used for the analysis.

![My Spotify Dashboard](./docs/images/Dashboard.png)

# Directory and Files

## Directory Structure
```
.
├── docs                    # Documentation files
│   └──images               # Images used in README
├── notebooks               # Tableau/Mathematica files used in exploration
├── python                  # Scripts for data processing/API access
└── README.md               # This file
```
## Python Scripts
`json_to_csv.py`: Merges Spotify .json files, and converts them to a single .csv file.  
`json_to_sql.py`: Merges Spotify .json files, and converts them to a sqlite database.  
`spotify_api_artists_genres.py`: Takes a .csv file of Spotify artist URI's and uses the Spotify API to look up their genre.  
`spotify_api_songs_artists.py`: Takes a .csv file of Spotify song URI's and uses the Spotify API to look up their artist.  

## Notebooks
`Exploring_Spotify.nb`: A Mathematica notebook using SQL to pull some quick statistics from a `json_to_sql.py` output.  
`Tableau_Plots.twb`: A Tableau Desktop version of the above-linked Tableau Public dashboard.  

# Data
## Spotify Extended Streaming Data
This project was made possible by downloading my [extended streaming history](https://support.spotify.com/us/article/data-rights-and-privacy-settings/) from Spotify.
Once a request is made, Spotify will fulfill it within 30 days.
It took a little two weeks to recieve a download link after my request was made.
The resulting .json files I downloaded were combined and converted to .csv with the `json_to_csv.py` script. 

## Spotify API
The Spotify extended streaming history does not include genre information. Using the [Spotipy](https://spotipy.readthedocs.io/en/2.22.1/) package and a free [Spotify Developer](https://developer.spotify.com/) account with API access, I was able to determine the genre for each song.
This process involved running a few scripts:  
`json_to_csv.py` -> `spotify_api_songs_artists.py` -> `spotify_api_artists_genres.py`  

# Further Improvements
For ease of use, I would like to combine the three relevant .py files into a single script.
