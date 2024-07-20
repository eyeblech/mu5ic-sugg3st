import requests
import random
import json

# Spotify API credentials
CLIENT_ID = 'your_client_id'
CLIENT_SECRET = 'your_client_secret'
ACCESS_TOKEN = 'your_access_token'

# Discord Webhook URL
WEBHOOK_URL = 'webhook_url'

# Function to get a Spotify access token
def get_access_token():
    auth_url = 'https://accounts.spotify.com/api/token'
    auth_data = {
        'grant_type': 'client_credentials'
    }
    auth_headers = {
        'Authorization': f'Basic {requests.auth._basic_auth_str(CLIENT_ID, CLIENT_SECRET)}'
    }
    response = requests.post(auth_url, data=auth_data, headers=auth_headers)
    return response.json()['access_token']

# Function to get a random metal song
def get_random_metal_song():
    headers = {
        'Authorization': f'Bearer {ACCESS_TOKEN}',
    }
    params = {
        'q': 'genre:"rap"',
        'type': 'track',
        'limit': 50
    }
    response = requests.get('https://api.spotify.com/v1/search', headers=headers, params=params)
    tracks = response.json()['tracks']['items']
    return random.choice(tracks)

# Function to send the song info to Discord
def notify_song():
    track = get_random_metal_song()
    track_name = track['name']
    artist_name = track['artists'][0]['name']
    track_id = track['id']
    message = f"🎶 Time to listen to: {track_name} by {artist_name} [Listen on Spotify](https://open.spotify.com/track/{track_id})"

    data = {
        'content': message
    }
    requests.post(WEBHOOK_URL, data=json.dumps(data), headers={'Content-Type': 'application/json'})

if __name__ == "__main__":
    notify_song()

