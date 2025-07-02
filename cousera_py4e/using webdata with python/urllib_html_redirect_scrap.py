import urllib.request, urllib.parse, urllib.error
import re

fhand = urllib.request.urlopen('http://www.dr-chuck.com/page1.htm')

print("MAIN LINK : http://www.dr-chuck.com/page1.htm")
print("\n=== BODY ===")
for line in fhand:
    #print(line.decode().rstrip())
    nextlink = re.findall('href="(.+)"', line.decode().rstrip())
    if len(nextlink) >= 1:
        print(f"nextlink:{nextlink}")
        print("\n=== NEW LINK BODY ===")
        nhand = urllib.request.urlopen(nextlink[0])
        for nline in nhand:
            print(nline.decode().rstrip())
        break