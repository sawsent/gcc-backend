from flask import Flask
from flask_cors import CORS
from playlistFetcher import PlaylistFetcher
from quoteFetcher import QuoteFetcher
from bookFetcher import BookFetcher
from videoFetcher import VideoFetcher
from gradientFetcher import GradientFetcher
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

@app.route('/api/get/playlist/<message>')
def playlist(message):
    message = message.replace('%20', ' ')
    fetcher = PlaylistFetcher(system_attributes)
    return fetcher.get(message)

@app.route('/api/get/quote/<message>')
def quote(message):
    message = message.replace('%20', ' ')
    fetcher = QuoteFetcher()
    return fetcher.get(message)

@app.route('/api/get/books/<message>')
def books(message):
    message = message.replace('%20', ' ')
    fetcher = BookFetcher()
    return fetcher.get(message)

@app.route('/api/get/videos/<message>')
def videos(message):
    message = message.replace('%20', ' ')
    fetcher = VideoFetcher()
    return fetcher.get(message)

@app.route('/api/get/gradient/<message>')
def gradient(message):
    message = message.replace('%20', ' ')
    fetcher = GradientFetcher()
    return fetcher.get(message)