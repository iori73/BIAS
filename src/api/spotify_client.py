import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os
from dotenv import load_dotenv
import yaml

class SpotifyClient:
    def __init__(self):
        load_dotenv()
        self.client = self._get_spotify_client()
    
    def _get_spotify_client(self):
        auth_manager = SpotifyClientCredentials(
            client_id=os.getenv('SPOTIFY_CLIENT_ID'),
            client_secret=os.getenv('SPOTIFY_CLIENT_SECRET')
        )
        return spotipy.Spotify(auth_manager=auth_manager)
    
    def get_show_episodes(self, show_id, limit=50):
        try:
            results = self.client.show_episodes(
                show_id,
                limit=limit,
                offset=0,
                market="JP"
            )
            return results['items']
        except Exception as e:
            print(f"Error fetching episodes: {e}")
            return None
