import urllib.request, urllib.parse, urllib.error
import re

fhand = urllib.request.urlopen('http://www.dr-chuck.com/page1.htm')

print("main link: http://www.dr-chuck.com/page1.htm")
print("\n==Body==")
for line in fhand:
    decoded_line = line.decode().rstrip()
    print(decoded_line)
    nextlink = re.findall('href="(.+)"',line.decode().rstrip())
    if len(nextlink) >=1:
        print(f"\nnextlink:{nextlink}")
        nhand = urllib.request.urlopen(nextlink[0])
        print("\n==Body==")
        for nline in nhand:
            print(nline.decode().rstrip())