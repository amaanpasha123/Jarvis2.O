from openai import OpenAI
from config import apikey

client = OpenAI(api_key=apikey)

response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {
      "role": "user",
      "content": "write an email to my boss rohit for my termination letter"
    }
  ],
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)