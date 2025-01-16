# src/utils/url_extractor.py
import os
import json

def get_spotify_urls(directory):
    spotify_urls = []
    try:
        for filename in os.listdir(directory):
            if filename.endswith('.json'):
                filepath = os.path.join(directory, filename)
                with open(filepath, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    spotify_url = data.get('external_urls', {}).get('spotify')
                    if spotify_url:
                        spotify_urls.append(spotify_url)
        return spotify_urls
    except Exception as e:
        print(f"Error reading directory: {e}")
        return []

def get_urls_as_list():
    current_dir = os.getcwd()
    episode_dir = os.path.join(current_dir, 'data', 'episodes')
    return get_spotify_urls(episode_dir)
