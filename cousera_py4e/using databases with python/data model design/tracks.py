import sqlite3



conn = sqlite3.connect('track_prac_db.sqlite')
cur = conn.cursor()

cur.executescript(
    '''
    DROP TABLE IF EXISTS Artist;
    DROP TABLE IF EXISTS Album;
    DROP TABLE IF EXISTS Genre;
    DROP TABLE IF EXISTS Track;
    
    CREATE TABLE Artist(
        id INTEGER PRIMARY KEY,
        artist_name TEXT UNIQUE
    );
    CREATE TABLE Genre(
        id INTEGER PRIMARY KEY,
        genre TEXT UNIQUE
    );
    CREATE TABLE Album(
        id INTEGER PRIMARY KEY,
        album_name TEXT UNIQUE,
        artist_id INTEGER,
        FOREIGN KEY (artist_id) REFERENCES Artist(id)
    );
    CREATE TABLE Track(
        id INTEGER PRIMARY KEY,
        title Text UNIQUE,
        album_id INTEGER,
        genre_id INTEGER,
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
    album = parts[1]
    artist = parts[2]
    count = parts[3]
    rating = parts[4]
    length = parts[5]
    genre = parts[6]

    print("----"*5)
    print(name,album,artist,count,rating,length,genre)

    cur.execute('''INSERT OR IGNORE INTO  Artist(artist_name) VALUES(?)''',(artist,))
    cur.execute('''SELECT id FROM Artist WHERE artist_name = ?''',(artist,))
    artist_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO  Album(album_name,artist_id) VALUES(?,?)''', (album,artist_id))
    cur.execute('''SELECT id FROM Album WHERE album_name = ?''', (album,))
    album_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO  Genre(genre) VALUES(?)''', (genre,))
    cur.execute('''SELECT id FROM Genre WHERE genre = ?''', (genre,))
    genre_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO  Track(title,album_id,genre_id,len,rating,count)
     VALUES(?,?,?,?,?,?)''', (name, album_id,genre_id,length,rating,count))

    conn.commit()
cur.close()