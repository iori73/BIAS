class Episode:
    def __init__(self, json_data):
        self.name = json_data.get('name', '')
        self.description = json_data.get('description', '')
        self.image_url = next((img['url'] for img in json_data.get('images', []) 
                             if img['height'] == 640), '')
        self.spotify_url = json_data.get('external_urls', {}).get('spotify', '')
        self.release_date = json_data.get('release_date', '')
