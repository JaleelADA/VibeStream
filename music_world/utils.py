# music_world/utils.py

import time
import requests
import base64

# Spotify API credentials
client_id = '1391b9de2e9e4060815e9ff377c4238a'
client_secret = 'ee659d5be5364f8c985b4441789a1768'
refresh_token = 'AQBYVPgy3Utb9i-6K9xomHqfkiEmPPlesTvNckDeL4tw9G0M4XjAG7Ripv8tlMxh6r3tCiupn0SRT6siWxAuvwXrZbGqdxBy-K5PKFuAtyT3kPPgQ7nsLkjVHHpm5VkDhv0'

# Function to refresh the access token
def refresh_access_token():
    auth_str = f"{client_id}:{client_secret}"
    b64_auth_str = base64.b64encode(auth_str.encode()).decode()
    response = requests.post(
        'https://accounts.spotify.com/api/token',
        headers={
            'Authorization': f'Basic {b64_auth_str}',
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        data={
            'grant_type': 'refresh_token',
            'refresh_token': refresh_token
        }
    )
    if response.status_code == 200:
        return response.json()['access_token']
    else:
        raise Exception(f"Failed to refresh access token: {response.status_code}")

# Store the access token and its expiration time
access_token = refresh_access_token()
token_expiration_time = time.time() + 3600  # Tokens typically expire in 1 hour

# Function to get the current access token
def get_access_token():
    global access_token, token_expiration_time
    if time.time() > token_expiration_time:
        access_token = refresh_access_token()
        token_expiration_time = time.time() + 3600
    return access_token
