import sqlite3



conn = sqlite3.connect('track_assgn_db.sqlite')
cur = conn.cursor()

cur.executescript(
    '''
    DROP TABLE IF EXISTS Artist;
    DROP TABLE IF EXISTS Album;
    DROP TABLE IF EXISTS Genre;
    DROP TABLE IF EXISTS Track;
    
    CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
    );
    
    CREATE TABLE Genre (
        id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name TEXT UNIQUE
    );
    
    CREATE TABLE Album (
        id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        artist_id  INTEGER,
        title TEXT UNIQUE,
        FOREIGN KEY (artist_id) REFERENCES Artist(id)
    );
    
    CREATE TABLE Track (
        id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        title TEXT  UNIQUE,
        album_id  INTEGER,
        genre_id  INTEGER,
        len INTEGER, rating INTEGER, count INTEGER,
        FOREIGN KEY (album_id) REFERENCES Album(id)
        FOREIGN KEY (genre_id) REFERENCES Genre(id)
    );
    ''')
handle = open('tracks.csv')
# Another One Bites The Dust,Queen,Greatest Hits,55,100,217103,Rock
# 0,                         1,     2,           3,  4,  5,    6

for line in handle:
    line = line.strip()
    parts = line.split(',')

    if len(parts) < 7: continue

    name = parts[0]
    artist = parts[1]
    album = parts[2]
    count = parts[3]
    rating = parts[4]
    length = parts[5]
    genre = parts[6]

    #print("----"*5)
    #print(name,album,artist,count,rating,length,genre)

    cur.execute('''INSERT OR IGNORE INTO  Artist(name) VALUES(?)''',(artist,))
    cur.execute('''SELECT id FROM Artist WHERE name = ?''',(artist,))
    artist_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO  Album(title,artist_id) VALUES(?,?)''', (album,artist_id))
    cur.execute('''SELECT id FROM Album WHERE title = ?''', (album,))
    album_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO  Genre(name) VALUES(?)''', (genre,))
    cur.execute('''SELECT id FROM Genre WHERE name = ?''', (genre,))
    genre_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO  Track(title,album_id,genre_id,len,rating,count)
     VALUES(?,?,?,?,?,?)''', (name, album_id,genre_id,length,rating,count))

    conn.commit()


sqlstr = '''SELECT Track.title, Artist.name, Album.title, Genre.name 
    FROM Track JOIN Genre JOIN Album JOIN Artist 
    ON Track.genre_id = Genre.ID and Track.album_id = Album.id 
        AND Album.artist_id = Artist.id
    ORDER BY Artist.name LIMIT 3'''
# Print each row with nicely formatted output
for row in cur.execute(sqlstr):
    print("DEBUG: row =", row)  # This shows exactly what each row looks like - DEBUG: row = ('cwen@iupui.edu', 5)
cur.close()