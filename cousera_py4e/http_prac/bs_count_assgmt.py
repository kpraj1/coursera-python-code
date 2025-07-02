from bs4 import BeautifulSoup
import urllib.request

sample_url = "https://py4e-data.dr-chuck.net/comments_42.html"
actual_url = "https://py4e-data.dr-chuck.net/comments_2178607.html"

html = urllib.request.urlopen(actual_url)
soup = BeautifulSoup(html,"html.parser")

#finding all spans and by using kwargs class = comment we will extract number values
spans = soup.find_all("span", class_="comments")

total = 0
count = 0
#with the help of this for loop we will convert comment numbers to int then update the count and total
for span in spans:
    count=count+1
    total += int(span.text)

print(f"Count {count}\nSum {total}")