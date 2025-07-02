import urllib.request
import json

# Create data to send
data = {
    "name": "Alice",
    "age": 30
}

# Serialize to JSON and encode
json_data = json.dumps(data).encode('utf-8')

# Setup the request
url = 'http://localhost:5000/api'
headers = {'Content-Type': 'application/json'}

req = urllib.request.Request(url, data=json_data, headers=headers)

# Send request and read response
with urllib.request.urlopen(req) as response:
    response_data = response.read().decode('utf-8')

# Deserialize and print
result = json.loads(response_data)
print("Server responded with:", result["message"])

for comment in result["comments"]:
    print("Name:", comment["name"])
    print("ID:", comment["id"])
    print("x:", comment["x"])
    print("-" * 30)
