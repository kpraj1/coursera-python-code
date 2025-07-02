import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

#read once and keepit such that we can iterate and use whenever we want, if traditional you use fhand directly and iterate for next time it will be lost.
rdata = fhand.read().decode()

#use any time
print("first time:")
for line in rdata.splitlines():
    print(line)

#later use
print("\nlater use")
counts = dict()
for line in rdata.splitlines():
    for word in line.split():
        counts[word]=counts.get(word,0)+1
print(counts)