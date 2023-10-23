import requests

# Define the expected schema
expected_schema = {
    "type": "object",
    "properties": {
        "userId": {"type": "string"},
        "id": {"type": "integer"},
        "title": {"type": "string"},
        "body": {"type": "string"}
    },
    "required": ["userId", "id", "title", "body"]
}

# Make the API request
url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)
data = response.json()
