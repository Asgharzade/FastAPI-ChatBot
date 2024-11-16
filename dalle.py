from openai import OpenAI
with open('misc/api_key.txt', 'r') as f:
    APIKEY = f.read()
client = OpenAI(api_key= APIKEY)
response = client.images.generate(
  model="dall-e-3",
  prompt="an ugly dirty donkey reading an old tick book",
  size="1024x1024",
  quality="standard",
  n=1,
)

image_url = response.data[0].url
print(image_url)