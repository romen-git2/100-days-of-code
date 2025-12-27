import requests
import base64
import time
import os
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")

class SpotifyAuthManager:
    """Handles the work of getting and refreshing tokens"""
    
    TOKEN_URL = "https://accounts.spotify.com/api/token"

    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret
        self.access_token = None
        self.token_expires_at = 0

    def get_token(self):
        """Returns a valid access token. Refreshes if expired"""
        if not self.access_token or time.time() > self.token_expires_at:
            print("Token expired or missing. Fetching new one...")
            self._refresh_token()
        return self.access_token

    def _refresh_token(self):
        """Performs the POST request to exchange credentials for a token"""
        # spotify requires Client ID - secret to be Base64 encoded in the header
        auth_str = f"{self.client_id}:{self.client_secret}"
        auth_b64 = base64.b64encode(auth_str.encode()).decode()

        headers = {
            "Authorization": f"Basic {auth_b64}",
            "Content-Type": "application/x-www-form-urlencoded"
        }
        data = {"grant_type": "client_credentials"}

        response = requests.post(self.TOKEN_URL, headers=headers, data=data)
        
        if response.status_code == 200:
            json_data = response.json()
            self.access_token = json_data['access_token']
            expires_in = json_data['expires_in']
            self.token_expires_at = time.time() + expires_in - 60 # safety buffer of 60s
            print(f"Secured new token (Expires in {expires_in}s)")
        else:
            raise Exception(f"Auth Failed: {response.status_code} {response.text}")

class MusicAgent:
    """The Agent that uses the token to do actual work"""
    
    BASE_URL = "https://api.spotify.com/v1"

    def __init__(self, auth_manager):
        self.auth = auth_manager

    def search_artist(self, artist_name):
        print(f"Searching for '{artist_name}'...")
        
        # get the token (Auth Manager handles valid/expired logic)
        token = self.auth.get_token()
        
        # make the authenticated request
        headers = {"Authorization": f"Bearer {token}"}
        params = {
            "q": artist_name,
            "type": "artist",
            "limit": 1
        }
        
        try:
            response = requests.get(f"{self.BASE_URL}/search", headers=headers, params=params)
            
            # handle '401 Unauthorized' (token might have been revoked remotely)
            if response.status_code == 401:
                print("401 Error. Token rejected. Forcing refresh...")
                self.auth.access_token = None # force reset
                return self.search_artist(artist_name) # retry once
            
            response.raise_for_status() # raise error for other codes (404, 500)
            
            data = response.json()
            if data['artists']['items']:
                artist = data['artists']['items'][0]
                print(f"Found Artist: {artist['name']}")
                print(f"Popularity: {artist['popularity']}/100")
                print(f"Link: {artist['external_urls']['spotify']}")
            else:
                print("No artist found.")

        except Exception as e:
            print(f"Error fetching data: {e}")

if __name__ == "__main__":

    # initialize
    auth_manager = SpotifyAuthManager(CLIENT_ID, CLIENT_SECRET)
    agent = MusicAgent(auth_manager)

    # first fetch (will trigger login)
    agent.search_artist("Daft Punk")

    # second fetch (should re-use cached token instantly)
    agent.search_artist("The Weeknd")
    
    # simulate expiration
    print("Simulating token expiration...")
    auth_manager.token_expires_at = time.time() - 100 # set time to past
    agent.search_artist("Charitha Attalage")