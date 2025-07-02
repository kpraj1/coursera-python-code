import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://www.dr-chuck.com/page1.htm')

# Print headers
print("=== HEADERS ===")
headers = fhand.getheaders()
for header in headers:
    print(f"{header[0]}: {header[1]}")
print("\n=== BODY ===")
for line in fhand:
    print(line.decode().rstrip())