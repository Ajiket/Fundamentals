"""
api_get.py
Example of making a GET API call in Python using the requests library.
This script fetches a single post from the JSONPlaceholder test API.
"""

import requests  # Import the requests library for HTTP calls

# Define the API endpoint (this is a fake test API)
url = "https://jsonplaceholder.typicode.com/posts/1"

# Make the GET request
response = requests.get(url)

# Check if the request was successful (status code 200 = OK)
if response.status_code == 200:
    # Parse the response JSON into a Python dictionary
    data = response.json()
    
    # Print the results
    print("✅ GET request successful!")
    print("Post ID:", data["id"])
    print("Title:", data["title"])
    print("Body:", data["body"])
else:
    # Print error if request failed
    print("❌ Error:", response.status_code)
