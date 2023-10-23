import requests

# Send a request to the API and receive a response
api_url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(api_url)

# Check if the API request was successful
if response.status_code == 200:
    api_response_data = response.json()
else:
    print(f"API request failed with status code {response.status_code}")
    api_response_data = None

# Inputted payload data
input_payload = {
    "title": "recommendation",
    "body": "motorcycle",
    "userId": 12
}

# Compare the API response to the inputted payload
if api_response_data:
    if api_response_data == input_payload:
        print("API response matches the input payload.")
    else:
        print("API response does not match the input payload.")
else:
    print("API request failed, cannot compare the response.")
