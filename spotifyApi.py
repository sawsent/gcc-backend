import requests

class Spotify:
    def __init__(self, client_id, client_secret) -> None:
        self.client_id = client_id
        self.client_secret = client_secret
        self.__token = self.__get_token(client_id, client_secret)

    def playlist_exists(self, id):
    
        headers = {
            'Authorization': 'Bearer {token}'.format(token=self.__token)
        }
      
        url = f'https://api.spotify.com/v1/playlists/{id}'

        response = requests.get(url, headers=headers)

        return response.status_code == 200
        

    def __get_token(self, CLIENT_ID, CLIENT_SECRET):
        AUTH_URL = 'https://accounts.spotify.com/api/token'

        # POST
        auth_response = requests.post(AUTH_URL, {
            'grant_type': 'client_credentials',
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
        })

        auth_response_data = auth_response.json()
        print(auth_response_data)
        return auth_response_data['access_token']