import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

# counts = dict()
# for line in fhand:
#     words = line.decode().split()
#     for word in words:
#         counts[word]=counts.get(word,0)+1
#
# print(counts)
#
# max_word = max(counts, key=counts.get)
# print(f"The most frequent word is '{max_word}' with {counts[max_word]} occurrences.")

# for printing the content
for line in fhand:
    print(line.decode().rstrip())
