from flask import Flask
from flask_cors import CORS
from fetcher import Fetcher
import os

system_attributes = {
    "api_integration": {
        "spotify": {
            "client_id": os.getenv('CLIENT_ID'),
            "client_secret": os.getenv('CLIENT_SECRET'),
            "access_token": None,  # Initially null, obtain through OAuth
            "refresh_token": None,
            "token_type": "Bearer",
            "expires_in": 3600,  # Lifetime of the access token in seconds
            "token_expiry": None  # Datetime when the token will expire (to be set programmatically)
        }
    },
    "model": {
        "type": "gpt-3.5-turbo",  # Model type for GPT (or other operations)
        "temperature": 1.1,  # Creativity temperature for text generation
        "max_tokens": 150  # Maximum number of tokens to generate
    }
}

app = Flask(__name__)
CORS(app)

@app.route('/api/get/<message>')
def hello_world(message):
    message = message.replace('%20', ' ');
    
    message = message.replace('%20', ' ');
    
    fetcher = Fetcher(system=system_attributes)

    return fetcher.get(message)