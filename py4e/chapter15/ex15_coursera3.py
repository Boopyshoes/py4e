# PY4E/Using Databases with Python course
# Coursera exercise 3 (week 3)
import xml.etree.ElementTree as ET
import sqlite3

db_connection = sqlite3.connect('tracks.sqlite')
db_cursor = db_connection.cursor()

# Make some fresh tables using executescript()
db_cursor.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;

CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY 
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);
''')


fname = input('Enter iTunes export file name: ')
if ( len(fname) < 1 ) : fname = 'Library.xml'

commit_frequency = input('How many entries per db commit?: ')
try:
    commit_frequency = int(commit_frequency)
except:
    commit_frequency = 1

# <key>Track ID</key><integer>369</integer>
# <key>Name</key><string>Another One Bites The Dust</string>
# <key>Artist</key><string>Queen</string>
def lookup(d, key):
    found = False
    for child in d:
        if found : return child.text
        if child.tag == 'key' and child.text == key :
            found = True
    return None

parsed_XML = ET.parse(fname)
tracks = parsed_XML.findall('dict/dict/dict')
# print(tracks)
print('Dict count:', len(tracks))
print(len(tracks))
if commit_frequency < 1:
    commit_frequency = 1

commit_counter = commit_frequency
print(commit_counter)

for track in tracks:
    #print(track)
    if(lookup(track, 'Track ID') is None): continue
    track_name = lookup(track, 'Name')
    track_artist = lookup(track, 'Artist')
    track_album = lookup(track, 'Album')
    track_genre = lookup(track, 'Genre')
    track_count = lookup(track, 'Play Count')
    track_rating = lookup(track, 'Rating')
    track_length = lookup(track, 'Total Time')

    if track_name is None or track_artist is None or track_album is None or track_genre is None:
        continue
    print(track_name, track_artist, track_album, track_genre, track_count, track_rating, track_length)

    # Set the Artist table, no foreign keys
    db_cursor.execute('''
       INSERT OR IGNORE INTO Artist (name)
        VALUES(?)''', (track_artist,))
    db_cursor.execute('SELECT id FROM Artist WHERE name = ?', (track_artist,) )
    artist_id = db_cursor.fetchone()[0]

    # Set the Genre talbe, no foreign keys
    db_cursor.execute('''
        INSERT OR IGNORE INTO Genre (name)
        VALUES(?)''', (track_genre,))
    db_cursor.execute('SELECT id FROM Genre WHERE name = ?', (track_genre,))
    genre_id = db_cursor.fetchone()[0]

    db_cursor.execute('''
        INSERT OR IGNORE INTO Album (title, artist_id)
        VALUES(?, ?)''', (track_album, artist_id))
    db_cursor.execute('SELECT id FROM Album WHERE title = ?', (track_album,))
    album_id = db_cursor.fetchone()[0]

    db_cursor.execute('''
        INSERT OR IGNORE INTO Track (title, album_id, genre_id, len, rating, count)
        VALUES (?, ?, ?, ?, ?, ?)''', (track_name, album_id, genre_id, track_length, track_rating, track_count))

    commit_counter -= 1
    print(commit_counter, commit_counter == 0)
    if commit_counter == 0:
        db_connection.commit()
        commit_counter = commit_frequency
        print('commit executed')

if commit_counter != 0:
    db_connection.commit()
    print('final commit executed')

