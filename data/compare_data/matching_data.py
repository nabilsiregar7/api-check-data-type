import requests
import json
from jsonschema import validate

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

# Validate the response against the schema
try:
    validate(data, expected_schema)
    print("API response matches the expected data type.")
except Exception as e:
    print("API response does not match the expected data type: {str(e)}")
