import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pprint # Test purpose

date = input("Which year do you want to get into: Enter the date in YYYY-MM-DD format: ")
CLIENT_ID = ""
CLIENT_SECRET =""
REDIRECT_URL = "http://example.com"

auth = SpotifyOAuth(client_id=CLIENT_ID,client_secret=CLIENT_SECRET,username=USER, redirect_uri="https://example.com/", scope="playlist-modify-private")

sp = spotipy.Spotify(auth_manager=auth)
info_dict = sp.current_user()
user_id = info_dict["id"]
url = f"https://www.billboard.com/charts/hot-100/{date}/"


def get_uri(songname, year):
    result = sp.search(q=f"track:{songname} year:{year}",type="track")
    if result["tracks"]["items"]:
        return result["tracks"]["items"][0]["uri"]
    else:
        return None

head = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}
response = requests.get(url, headers=head)
print(response.status_code)

soup = BeautifulSoup(response.content,"html.parser")
song_names_spans = soup.select("li ul li h3")

song_names = [song.getText().strip() for song in song_names_spans]

song_uri = [get_uri(songname=song_names[i],year=date[0:4]) for i in range(len(song_names)) if get_uri(songname=song_names[i],year=date[0:4]) is not None]

playlist = sp.user_playlist_create(user=user_id,name=f"{date} 100 Bill-Board",public=False, description="description"))
try:
    sp.playlist_add_items(playlist_id=playlist["id"],items=song_uri,position=None)
    print("added succesfully")
except Exception as e:
    print("error is:",e)
