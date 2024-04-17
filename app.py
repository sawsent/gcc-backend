from flask import Flask
from service import playlistService
app = Flask(__name__)

@app.route('/api/get/<message>')
def hello_world(message):
    response = playlistService.sendRequest(message)
    return response


