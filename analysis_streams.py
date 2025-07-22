import pandas as pd
import matplotlib.pyplot as plt
from top100spotify import top_100_songs

df_sorted = top_100_songs()

# Convert columns to numeric (remove commas)
for col in ['spotify_streams', 'youtube_views', 'youtube_likes', 'tiktok_posts', 'tiktok_likes', 'tiktok_views']:
    df_sorted[col] = pd.to_numeric(df_sorted[col].replace(',', '', regex=True), errors='coerce')

# Check how Spotify streams relate to other stuff
corr = df_sorted[['spotify_streams', 'tiktok_posts', 'tiktok_likes', 'tiktok_views', 'youtube_views', 'youtube_likes']].corr()
print("Correlation with Spotify Streams:")
print(corr['spotify_streams'])

print("\nCorrelation between Spotify Streams and External Factors:")
print(corr['spotify_streams'])

# TikTok Views vs. Spotify Streams
plt.scatter(df_sorted['tiktok_views'], df_sorted['spotify_streams'])
plt.xlabel('TikTok Views')
plt.ylabel('Spotify Streams')
plt.title('TikTok Views vs. Spotify Streams')
plt.show()

# YouTube Views vs. Spotify Streams
plt.scatter(df_sorted['youtube_views'], df_sorted['spotify_streams'])
plt.xlabel('YouTube Views')
plt.ylabel('Spotify Streams')
plt.title('YouTube Views vs. Spotify Streams')
plt.show()

# Find average streams for songs with and without TikTok activity
avg_with_tiktok = df_sorted[df_sorted['tiktok_views'] > 0]['spotify_streams'].mean()
avg_without_tiktok = df_sorted[df_sorted['tiktok_views'] == 0]['spotify_streams'].mean()
print("Average Spotify Streams (with TikTok):", avg_with_tiktok)
print("Average Spotify Streams (no TikTok):", avg_without_tiktok)

# Find average streams for songs with and without YouTube activity
avg_with_youtube = df_sorted[df_sorted['youtube_views'] > 0]['spotify_streams'].mean()
avg_without_youtube = df_sorted[df_sorted['youtube_views'] == 0]['spotify_streams'].mean()
print("Average Spotify Streams (with YouTube):", avg_with_youtube)
print("Average Spotify Streams (no YouTube):", avg_without_youtube)