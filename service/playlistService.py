import openai;

def sendRequest(message):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an assistent that helps me feel better through music. You give me spotify playlist links that matches my mood and helps me feel better. It makes me heal. Give me the 10 links. The links are very important"},
            {"role": "user", "content": message},
        ],
        temperature=1.2
    )

    
    return response