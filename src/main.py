# src/main.py
import os
import json
import pandas as pd
import re

# データ処理関数
def extract_guest_name(description):
    pattern = r'ゲスト・(.+?)さん'
    match = re.search(pattern, description)
    return match.group(1) if match else None

def extract_university(description):
    pattern = r'([\w\s]+大学[\w\s]+学部[\w\s]+学科|[\w\s]+大学[\w\s]+学部)'
    match = re.search(pattern, description)
    return match.group(1) if match else None

def extract_grad_school(description):
    pattern = r'([\w\s]+大学院[\w\s]+研究科)'
    match = re.search(pattern, description)
    return match.group(1) if match else None

def extract_employer(description):
    patterns = [
        r'現在は([\w\s]+)で',
        r'([\w\s]+)に就職',
        r'([\w\s]+)で勤務'
    ]
    for pattern in patterns:
        match = re.search(pattern, description)
        if match:
            return match.group(1)
    return None

class Episode:
    def __init__(self, json_data):
        self.name = json_data.get('name', '')
        self.description = json_data.get('description', '')
        self.image_url = next((img['url'] for img in json_data.get('images', []) 
                             if img['height'] == 640), '')
        self.spotify_url = json_data.get('external_urls', {}).get('spotify', '')
        self.release_date = json_data.get('release_date', '')

def process_episodes():
    episodes_dir = './data/episodes'
    data = []
    
    for filename in os.listdir(episodes_dir):
        if filename.endswith('.json'):
            filepath = os.path.join(episodes_dir, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                episode_data = json.load(f)
                episode = Episode(episode_data)
                
                data.append({
                    'name': extract_guest_name(episode.description),
                    'image': episode.image_url,
                    'description': episode.description,
                    'URL': episode.spotify_url,
                    'country': '',  # 手動で追加必要
                    'release_date': episode.release_date,
                    'Episode title': episode.name,
                    'University/college': extract_university(episode.description),
                    'Grad school': extract_grad_school(episode.description),
                    'Current Employer': extract_employer(episode.description)
                })

    df = pd.DataFrame(data)
    df = df.sort_values('release_date').groupby('name').first().reset_index()
    df.to_csv('./data/processed_episodes.csv', index=False)

if __name__ == "__main__":
    process_episodes()
