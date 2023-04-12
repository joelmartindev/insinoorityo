import openai
import os
from dotenv import load_dotenv

load_dotenv()

# Load your API key from an environment variable or secret management service
openai.api_key = os.getenv("OPENAI_API_KEY")
print(openai.api_key)

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": "You are a webshop assistant."},
        {"role": "user", "content": "Hello"}
    ]
)

print(response)
print('Pelkkä vastaus')
print(response['choices'][0]['message']['content'])