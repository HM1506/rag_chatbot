from dotenv import load_dotenv
from anthropic import Anthropic
import os

# Load the API key from your .env file
load_dotenv()

# Create a client to talk to Claude
client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

# Send a simple test message
response = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=100,
    messages=[
        {"role": "user", "content": "Say hello in one short sentence."}
    ]
)

# Print Claude's reply
print(response.content[0].text)