import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

htmlhand = urllib.request.urlopen('http://www.dr-chuck.com/page1.htm').read()
soup = BeautifulSoup(htmlhand,'html.parser')

#Retrieve all the anchor tags
tags = soup('a')
for tag in tags:
    newtag=tag.get('href',None)
    if newtag is not None:
        print(newtag)
        htmlnewhand = urllib.request.urlopen(newtag).read().decode().splitlines()
        for nline in htmlnewhand :
            print(nline.strip())
        break
        """ htmlnewhand = urllib.request.urlopen(newtag).read().decode().splitlines()
        
            urlopen(newtag) → opens the next page (like page2.htm)
            
            .read() → reads the full response as a byte string
            
            .decode() → converts byte string → regular text (UTF-8 by default)
            
            .splitlines() → splits text into a list of lines (removes \n)
            
            for nline in htmlnewhand → now you're looping over clean lines
        """
