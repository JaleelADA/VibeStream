# music_world/views.py

from django.shortcuts import render
import requests
from .utils import get_access_token

def home(request):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {get_access_token()}'
    }
    data = requests.get("https://api.spotify.com/v1/browse/featured-playlists?limit=3", headers=headers)
    data1 = requests.get("https://api.spotify.com/v1/browse/new-releases?limit=3", headers=headers)
    status_code = data.status_code
    data = data.json()
    data1 = data1.json()
    if status_code == 200:
        data = data['playlists']['items']
        data1 = data1['albums']['items']
        return render(request, 'music_world/home.html', {
            "data": data, "data1": data1
        })
    else:
        return render(request, 'music_world/error.html', {
            "data": data, "message": data['error']['message']
        })

def playlist(request, id):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {get_access_token()}'
    }
    data = requests.get(f'https://api.spotify.com/v1/playlists/{id}', headers=headers)
    status_code = data.status_code
    data = data.json()
    if status_code == 200:
        return render(request, 'music_world/playlist.html', {"data": data})
    else:
        return render(request, 'music_world/error.html', {
            "data": data, "message": data['error']['message']
        })

def search(request):
    query = request.GET.get('query', '')
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {get_access_token()}'
    }
    data = requests.get(f'https://api.spotify.com/v1/search?q={query}&type=artist,album,playlist', headers=headers)
    status_code = data.status_code
    data = data.json()
    if status_code == 200:
        return render(request, 'music_world/search_results.html', {"data": data})
    else:
        return render(request, 'music_world/error.html', {
            "data": data, "message": data['error']['message']
        })

def album(request, id):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {get_access_token()}'
    }
    data = requests.get(f'https://api.spotify.com/v1/albums/{id}', headers=headers)
    status_code = data.status_code
    data = data.json()
    if status_code == 200:
        return render(request, 'music_world/album.html', {"data": data})
    else:
        return render(request, 'music_world/error.html', {
            "data": data, "message": data['error']['message']
        })

def sartist(request):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {get_access_token()}'
    }
    query = request.GET.get('query', '')
    data = requests.get(f'https://api.spotify.com/v1/search?q={query}&type=artist', headers=headers)
    status_code = data.status_code
    data = data.json()
    if status_code == 200:
        return render(request, 'music_world/sartist.html', {"data": data['artists']['items']})
    else:
        return render(request, 'music_world/error.html', {
            "data": data, "message": data['error']['message']
        })

def artist(request, id):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {get_access_token()}'
    }
    data = requests.get(f'https://api.spotify.com/v1/artists/{id}', headers=headers)
    status_code = data.status_code
    data = data.json()
    if status_code == 200:
        return render(request, 'music_world/artist.html', {"data": data})
    else:
        return render(request, 'music_world/error.html', {
            "data": data, "message": data['error']['message']
        })

def audio(request, id):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {get_access_token()}'
    }
    data = requests.get(f'https://api.spotify.com/v1/audio-features/{id}', headers=headers)
    status_code = data.status_code
    data = data.json()
    if status_code == 200:
        context = {
            "danceability": data['danceability'],
            "energy": data['energy'],
            "loudness": data['loudness'],
            "speechiness": data['speechiness'],
            "acousticness": data['acousticness'],
            "instrumentalness": data['instrumentalness'],
            "liveness": data['liveness'],
            "valence": data['valence'],
            "tempo": data['tempo']
        }
        return render(request, 'music_world/audio.html', context)
    else:
        return render(request, 'music_world/error.html', {
            "data": data, "message": data['error']['message']
        })
