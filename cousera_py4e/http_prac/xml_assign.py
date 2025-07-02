import urllib.request
import xml.etree.ElementTree as ET

url = input("Enter location: ")
fhand = urllib.request.urlopen(url).read()
print("Retrieving ",url)
print("Retrieved ",len(fhand)," characters")
sum = 0
content = ET.fromstring(fhand)
lst = content.findall('comments/comment')
print("Count: ",len(lst))
for i in lst:
    sum+=int(i.find('count').text)
print("Sum: ",sum)

