from spotifyApi import Spotify
import re

def extract_ids(text):
    url_pattern = r'https://open.spotify.com/playlist/[0-9a-zA-Z=?]+'
    urls = re.findall(url_pattern, text)

    ids = list(map(lambda url: url.split('/')[-1], urls))
    return ids

def get(gptResponse, client_id="24e3d58f0a374026a241f5b4647ecbe7", client_secret="59d089b30e32472e9bafe784da44fe15"):
    spotify = Spotify(client_id, client_secret)
    
    while True:

        res = gptResponse["choices"][0]["message"]["content"]
        ids = extract_ids(res)

        if len(ids) == 0:
            continue
        
        for id in ids:
            print(id)
            if spotify.playlist_exists(id):
                return {
                    'playlist_id': id,
                }