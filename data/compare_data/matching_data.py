import requests
import json
from jsonschema import validate

# Define the expected schema
expected_schema = {
    "type": "object",
    "properties": {
        "userId": {"type": "integer"},
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

# Check if the API request was successful
if response.status_code == 200:
    api_response_data = response.json()
else:
    print(f"API request failed with status code {response.status_code}")
    api_response_data = None

# Validate the response against the schema
try:
    validate(data, expected_schema)
    print("API response matches the expected data type.")
except Exception as e:
    print(f"API response does not match the expected data type: {str(e)}")
