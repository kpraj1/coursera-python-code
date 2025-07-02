import urllib.request, urllib.parse, urllib.error
import json

total_sum=0
total_count=0

url = input("Enter location: ")
if len(url)<1:
    url = 'http://py4e-data.dr-chuck.net/comments_42.json'
print("Retrieving",url)
in_data = urllib.request.urlopen(url).read().decode('utf-8')
print("Retrieved",len(in_data),"characters")

decrypt_data= json.loads(in_data)

for item in decrypt_data["comments"]:
    if int(item["count"])>0:
        total_count+=1
        total_sum+=int(item["count"])
print(f"Count: {total_count}\nSum: {total_sum}")

# Pretty-print the JSON data with indentation
#print(json.dumps(decrypt_data, indent=4))