import pandas as pd

#load CSV 
df = pd.read_csv(r'C:\Users\User\Desktop\Spotify\songs_2024.csv', encoding='ISO-8859-1')

#clean column names
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

#limiting the dataset by important columns
df = df[[
    'track',
    'album_name',
    'artist',
    'release_date',
    'track_score',
    'spotify_streams',
    'youtube_views',
    'youtube_likes',
    'tiktok_posts',
    'tiktok_likes',
    'tiktok_views'
]]

#conversion of release_date to datetime format
df['spotify_streams'] = pd.to_numeric(df['spotify_streams'].replace(',', '', regex=True), errors='coerce')

#function to clean Spotify data
def clean_spotify_data(df):
    df = df.drop_duplicates()
    df = df.dropna(subset=['spotify_streams'])
    df = df[df['spotify_streams'] > 0]
    df['release_date'] = pd.to_datetime(df['release_date'], errors='coerce')
    return df

#calling the cleaning function
df = clean_spotify_data(df)

# sort and select top 100
df_sorted = df.sort_values(by='spotify_streams', ascending=False).head(100)

# Create a ranking column (1 to 100)
df_sorted = df_sorted.reset_index(drop=True)
df_sorted.insert(0, 'ranking', df_sorted.index + 1)

print(df_sorted)