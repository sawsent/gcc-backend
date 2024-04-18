import openai
import re
import os

class QuoteFetcher:
    def __init__(self) -> None:
        openai.api_key = os.getenv('OPENAI_API_KEY')


    def sendRequest(self, message):
        
        response = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=[
                {"role": "system", "content": "You are an assistent that helps me feel better through inspirational quotes. You give me quotes will make me feel better. If I'm sad, youll help me heal. You put the quotes between square brackets []. generate 1 quotes"},
                {"role": "user", "content": message},
            ],
            temperature=1.3
        )
        return response
    
    
    def find_content_in_brackets(self, text):
        print(text)
        matches = re.findall(r"\[(.*?)\]", text)
        if matches and matches[0].lower() != "unknown":
            return matches[0]
        else:
            return "The truly rich men are the ones who have health, loved ones and a work they love."

    
    
    def get(self, prompt):
        nelson_response = self.sendRequest(prompt)['choices'][0]['message']['content']
        
        quote = self.find_content_in_brackets(nelson_response)

        return {
            'quote': quote,
        }

