import sqlite3
import json
import codecs

conn = sqlite3.connect('opengeo_prac.sqlite')
cur = conn.cursor()


fhand = codecs.open('where.js','w','utf-8')
fhand.write('myData = [\n')
count = 0

cur.execute('SELECT * FROM Locations')

for row in cur:
    data = str(row[1].decode())
    try:
        js = json.loads(str(data))
    except:
        continue

    if len(js['features']) == 0:
        continue

    try:
        lat = js['features'][0]['geometry']['coordinates'][1]
        lng = js['features'][0]['geometry']['coordinates'][0]
        place = js['features'][0]['properties']['display_name']
        place = place.replace("'","")
    except:
        print("unexpected format")
        print(js)

    try:
        print(place,lat,lng)
        count = count+1
        if count > 1:
            fhand.write(",\n")
        output  = "["+str(lat)+","+str(lng)+", '"+place+"']"
        fhand.write(output)
    except:
        continue

fhand.write("\n];\n")
cur.close()
fhand.close()
print(count,"records written to where.js")
print("open where.html to view data in a browser")
