import requests
import os
import openai
import re

class BookFetcher:

    def __init__(self) -> None:
        openai.api_key = os.getenv('OPENAI_API_KEY')
        self.google_api_key = os.getenv('GOOGLE_API_KEY')
   

    def sendRequest(self, message):
        
        response = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=[
                {"role": "system", "content": "You are an assistent that helps me feel better through books. You give me book query keywords that i can use with google books api. for instance If I'm sad, youll help me heal. You put the keywords between square brackets []. generate 3 keywords in english."},
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

    def fetchFromGAPI(self, query):
          # Replace with your actual API key
        url = f"https://www.googleapis.com/books/v1/volumes?q={query}&key={self.google_api_key}"
        response = requests.get(url)
        books = response.json()

        results = []
        for item in books['items']:
            info = item['volumeInfo']
            title = info.get('title', 'No title available')
            authors = info.get('authors', ['Unknown Author'])
            cover_image = info.get('imageLinks', {}).get('thumbnail', '/resources/booknotfound.jpg')
            
            results.append({"title": title, "author": ", ".join(authors), "cover": cover_image})

        return results
    
    def get(self, prompt):
        nelson_response = self.sendRequest(prompt)['choices'][0]['message']['content']
        
        
        quote = self.find_content_in_brackets(nelson_response)
        books = self.fetchFromGAPI(quote)
        return books

