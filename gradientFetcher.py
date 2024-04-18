import openai
import re
import os

class GradientFetcher:
    def __init__(self) -> None:
        openai.api_key = os.getenv("OPENAI_API_KEY")


    def sendRequest(self, message):
        
        response = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=[
                {"role": "system", "content": "You are an assistent that gives me a beautiful css gradient background with 4 edges. It needs to mirror my mood in a way that will make me feel better. You give it in this format: [background: linear-gradient(45deg, #83A8A6, #497A78, #C0CDC4, #83A8A6)] even if you dont understand what im telling you, generate a css gradient background."},
                {"role": "user", "content": "Im feeling " + message},
            ],
            temperature=1.3
        )
        return response
    
    
    def find_content_in_brackets(self, text):
        matches = re.findall(r"\[(.*?)\]", text)
        if matches:
            return matches[0]
        else:
            return "background: linear-gradient(45deg, #83A8A6, #497A78, #C0CDC4, #83A8A6)"

    
    
    def get(self, prompt):
        nelson_response = self.sendRequest(prompt)['choices'][0]['message']['content']
        
        gradient = self.find_content_in_brackets(nelson_response)

        return {
            'gradient': gradient + ';',
        }

