import requests

url = "http://localhost:8000/analyze"
data = {
    "entries": [
        "I had a great day today, everything went well",
        "I feel excited about my new project",
        "But I'm also a bit nervous about the upcoming deadline"
    ]
}

response = requests.post(url, json=data)
print(response.json())