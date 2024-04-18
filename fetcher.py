import requests
import datetime
import openai
import re

class Fetcher:
    def __init__(self, system):
        self.system = system
        self.spotify_auth_details = system['api_integration']['spotify']
        self.base_spotify_url = "https://api.spotify.com/v1"

        self.authenticate_spotify(force=True)

    
    def authenticate_spotify(self, force=True):
        """ Refreshes the Spotify token using the refresh token if necessary. """
        now = datetime.datetime.now()
        if force or now >= self.spotify_auth_details.get('token_expiry', now):
            
        
            response = requests.post(
                'https://accounts.spotify.com/api/token',
                data={
                'grant_type': 'client_credentials',
                'client_id': self.system['api_integration']['spotify']['client_id'],
                'client_secret': self.system['api_integration']['spotify']['client_secret'],
                }
            )
            token_info = response.json()
            self.spotify_auth_details['access_token'] = token_info['access_token']
            self.spotify_auth_details['expires_in'] = token_info['expires_in']
            self.spotify_auth_details['token_expiry'] = now + datetime.timedelta(seconds=token_info['expires_in'])


    def sendRequest(self, message):
        
        response = openai.ChatCompletion.create(
            model=self.system['model']['type'],
            messages=[
                {"role": "system", "content": "You are an assistent that helps me feel better through music. You give me a query so i can better search for spotify playlists, based on what music will make me feel better. If I'm sad, youll help me heal. You put the query between square brackets []. generate 1 query idea with at least 5 words"},
                {"role": "user", "content": message},
            ],
            temperature=self.system['model']['temperature']
        )
        return response
    
    
    def find_content_in_brackets(self, text):
        print(text)
        matches = re.findall(r"\[(.*?)\]", text)
        if matches:
            return matches[0]
        else:
            return "happy upbeat chill incredible"

    def extract_id(self, text):
        print(text)
        url_pattern = r'https://open.spotify.com/playlist/[0-9a-zA-Z=?]+'
        urls = re.findall(url_pattern, text)

        ids = list(map(lambda url: url.split('/')[-1], urls))
        return ids[0]

    def generate_playlist_link(self, mood):
        """ Generates Spotify playlist links based on the user's mood """
        self.authenticate_spotify()  # Ensure the token is valid


        query = f"{mood} feeling mood"  # Customize your query
        response = requests.get(
            f"{self.base_spotify_url}/search",
            headers={"Authorization": f"Bearer {self.spotify_auth_details['access_token']}"},
            params={"q": query, "type": "playlist", "limit": 1}
        )
        playlists = response.json()['playlists']['items']
        playlist_links = [playlist['external_urls']['spotify'] for playlist in playlists]
        return playlist_links[0]
    
    def get(self, prompt):
        nelson_response = self.sendRequest(prompt)['choices'][0]['message']['content']
        spotify_prompt = self.find_content_in_brackets(nelson_response)
        url = self.generate_playlist_link(spotify_prompt)
        id = self.extract_id(url)

        return {
            'status': 'success',
            'playlist_id': id,
        }

