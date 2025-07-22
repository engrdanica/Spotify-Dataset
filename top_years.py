import pandas as pd
from top100spotify import get_top100_songs  # Import Top 100 songs

# Load Top 100 songs
df_sorted = top_100_songs()

# Extract release year
df_sorted['release_year'] = df_sorted['release_date'].dt.year

# Group by release_year and sum spotify_streams
top_years = df_sorted.groupby('release_year')['spotify_streams'].sum().reset_index()

# Sort and Rank
top_years = top_years.sort_values(by='spotify_streams', ascending=False).reset_index(drop=True)
top_years.insert(0, 'ranking', top_years.index + 1)

# Show Top 10 release years
print("\nTop 10 Release Years Based on Total Spotify Streams (Top 100 Songs):")
print(top_years.head(10))
