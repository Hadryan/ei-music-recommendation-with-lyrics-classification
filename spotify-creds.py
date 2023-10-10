import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials

cid = ""  # Client ID
secret = ""  # Client Secret
username = ""  # Your Spotify username

scope = "user-library-read playlist-modify-public playlist-read-private"

redirect_uri = "http://localhost:8888/callback"

client_credentials_manager = SpotifyClientCredentials(
    client_id=cid, client_secret=secret
)

sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

token = util.prompt_for_user_token(
    username,
    scope,
    client_id=cid,
    client_secret=secret,
    redirect_uri="http://localhost:8888/callback",
)

if token:
    sp = spotipy.Spotify(auth=token)
else:
    print("Can't get token for", username)
