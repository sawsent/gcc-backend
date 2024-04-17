from flask import Flask
from service import playlistService
from format import get

app = Flask(__name__)

@app.route('/api/get/<message>')
def hello_world(message):
    message = message.replace('%20', ' ');
    
    response = playlistService.sendRequest(message)

    return get(response.json())


