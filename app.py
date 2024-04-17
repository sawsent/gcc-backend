from flask import Flask
from service import playlistService
import jsonFormatter

app = Flask(__name__)

@app.route('/api/get/<message>')
def hello_world(message):
    message = message.replace('%20', ' ');
    
    response = playlistService.sendRequest(message)
    out = jsonFormatter.get(response)

    while out['status'] != 'success':
        response = playlistService.sendRequest(message)
        out = jsonFormatter.get(response)
    
    return jsonFormatter.get(response)


