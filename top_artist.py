#import function

import pandas as pd
from top100spotify import top_100_songs

# Get Top 100 songs DataFrame
df_sorted = top_100_songs()

# Group by artist and sum their total Spotify streams within Top 100
top_artists = df_sorted.groupby('artist')['spotify_streams'].sum().reset_index()

# Sort and Rank
top_artists = top_artists.sort_values(by='spotify_streams', ascending=False).reset_index(drop=True)
top_artists.insert(0, 'ranking', top_artists.index + 1)

# Display Top 10 Artists
print("\nTop 10 Artists Based on Top 100 Spotify Songs (Total Streams):")
print(top_artists.head(10))