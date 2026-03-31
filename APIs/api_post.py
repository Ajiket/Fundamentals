"""
api_post.py
Example of making a POST API call in Python using the requests library.
This script sends new post data to the JSONPlaceholder test API.
"""

import requests  # Import the requests library for HTTP calls

# Define the API endpoint for creating a new post
url = "https://jsonplaceholder.typicode.com/posts"

# Data to send in the POST request (like submitting a form)
new_post = {
    "title": "My First API Post",
    "body": "This is a test post created via a POST API call.",
    "userId": 1
}

# Make the POST request with JSON data
response = requests.post(url, json=new_post)

# Check if the request was successful (status code 201 = Created)
if response.status_code == 201:
    # Parse the response JSON into a Python dictionary
    data = response.json()
    
    # Print the results
    print("✅ POST request successful!")
    print("New Post Created:", data)
else:
    # Print error if request failed
    print("❌ Error:", response.status_code)
