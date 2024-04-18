import openai
import requests
import re
import os

class VideoFetcher:
    def __init__(self) -> None:
        openai.api_key = os.getenv('OPENAI_API_KEY')
        self.google_api_key = os.getenv('GOOGLE_API_KEY')
   

    def sendRequest(self, message):
        
        response = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=[
                {"role": "system", "content": "You are an assistent that helps me feel better through videos. You give me youtube query keywords that i can use with google youtube data api. for instance If I'm sad, youll help me heal. You put the keywords between square brackets []. generate 3 keywords in english."},
                {"role": "user", "content": message},
            ],
            temperature=1.3
        )
        return response
    
    
    def find_content_in_brackets(self, text):
        print(text)
        matches = re.findall(r"\[(.*?)\]", text)
        if matches and matches[0].lower() != "unknown":
            return ",".join(matches)
        else:
            return "The truly rich men are the ones who have health, loved ones and a work they love."

    def fetchFromGAPI(self, query):  # Replace with your actual API key
        url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&q={query}&key={self.google_api_key}&type=video"
        response = requests.get(url)
        videos = response.json()
        
        results = []
        for item in videos['items']:
            video_data = {
                "title": item['snippet']['title'],
                "url": f"https://www.youtube.com/watch?v={item['id']['videoId']}"
            }
            results.append(video_data)
    
        return results
    
    def get(self, prompt):
        nelson_response = self.sendRequest(prompt)['choices'][0]['message']['content']
        
        
        curated = self.find_content_in_brackets(nelson_response)
        videos = self.fetchFromGAPI(curated)
        return videos