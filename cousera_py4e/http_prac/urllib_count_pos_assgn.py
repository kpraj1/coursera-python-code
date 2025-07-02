# import urllib.request, urllib.parse, urllib.error
# import re
#
# #url="http://py4e-data.dr-chuck.net/known_by_Fikret.html"
# nurl=""
# iposition = 0
#
# position = int(input("enter position: "))
# count = int(input('enter count: '))
#
# url = input('Enter url: ')
# print("Retrieving: " + url)
# for i in range(count):
#     fhand = urllib.request.urlopen(url)
#     links = []
#     for line in fhand:
#         links += re.findall('href="(.+?)"',line.decode().rstrip())
#     if len(links)>=position:
#         url = links[position-1]
#         print("Retrieving: " + url)
#     else:
#         print("not enough links in the page for migration to next page for the given position")
#         break

#beautiful soup way of doing
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

#url="http://py4e-data.dr-chuck.net/known_by_Fikret.html"

position = int(input("enter position: "))
count = int(input('enter count: '))
url = input('Enter url: ')

print("Retrieving: " + url)
for i in range(count):
    fhand = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(fhand,"html.parser")

    tags = soup.find_all('a')

    if len(tags)>= position:
        url=tags[position-1].get('href',None)
        print("Retrieving: "+url)
    else:
        print("Not enough tags for the given position on this page")
        break
