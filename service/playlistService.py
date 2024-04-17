import openai;

def sendRequest(message):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an assistent that helps me feel better through music. You give me spotify playlists to help me feel better. Give me the link. The link is very important"},
            {"role": "user", "content": message},
        ],
    )
    return response

