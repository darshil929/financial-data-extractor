import openai

openai.api_key = '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'

def poem_on_gym():
    prompt = 'write a poem on gym. only 4 lines please.'

    responce = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": "write a poem on gym. only 4 lines please."},    
        ]
    )

    print(responce.choices[0]['message']['content'])

if __name__ == '__main__':
    poem_on_gym()

