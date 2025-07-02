"""
import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

# printing only body excluding headers
for line in fhand:
    print(line.decode().rstrip())
"""
import urllib.request, urllib.parse, urllib.error

url = 'http://data.pr4e.org/romeo.txt'
response = urllib.request.urlopen(url)
#printing both headers and body
# Print headers
print("=== HEADERS ===")
headers = response.getheaders()
for header in headers:
    print(f"{header[0]}: {header[1]}")

# Print body
print("\n=== BODY ===")
for line in response:
    print(line.decode().rstrip())