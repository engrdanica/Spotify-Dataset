import pandas as pd

def top_100_songs():
    # Load CSV
    df = pd.read_csv(r'C:\Users\User\Desktop\Spotify\songs_2024.csv', encoding='ISO-8859-1')

    # Clean column names
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

    # Keep necessary columns
    df = df[[ 
        'track', 'album_name', 'artist', 'release_date', 'track_score',
        'spotify_streams', 'youtube_views', 'youtube_likes',
        'tiktok_posts', 'tiktok_likes', 'tiktok_views'
    ]]

    # Convert streams to numeric
    df['spotify_streams'] = pd.to_numeric(df['spotify_streams'].replace(',', '', regex=True), errors='coerce')

    # Clean data
    df = df.drop_duplicates()
    df = df.dropna(subset=['spotify_streams'])
    df = df[df['spotify_streams'] > 0]
    df['release_date'] = pd.to_datetime(df['release_date'], errors='coerce')

    # Deduplicate tracks
    df = df.sort_values(by='spotify_streams', ascending=False)
    df = df.drop_duplicates(subset=['track'], keep='first')

    # Select Top 100
    df_sorted = df.head(100).reset_index(drop=True)
    df_sorted.insert(0, 'ranking', df_sorted.index + 1)

    return df_sorted
