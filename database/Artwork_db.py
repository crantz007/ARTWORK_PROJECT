import sqlite3
from model.Model import Artwork
from exceptions.artworkError import ArtworkError

artist_db = 'artworkStore'


class SQLArtworkDB():
    # Creates tables if not exists
    def __init__(self):
        with sqlite3.connect(artist_db) as con:
            con.execute('CREATE TABLE IF NOT EXISTS ARTIST (Artists TEXT NOT NULL, email TEXT UNIQUE NOT NULL)')
        with sqlite3.connect(artist_db) as con:
            con.execute(
                'CREATE TABLE IF NOT EXISTS ARTWORK (Artists TEXT NOT NULL, name TEXT UNIQUE NOT NULL, price FLOAT, available INTEGER, FOREIGN KEY(Artists) REFERENCES ARTIST(Artists))')

    # inserting artist in to database from view view_model
    def insert_artist(self, artist):
        try:
            with sqlite3.connect(artist_db) as con:
                rows = con.execute('INSERT INTO ARTIST VALUES (?, ?)', (artist.name, artist.email))
            con.close()
            return rows
        except sqlite3.IntegrityError as e:
            raise ArtworkError(f'Cannot be added, {artist.email} already exists ')

    # inserting artwork in to database from view view_model
    def insert_artwork(self, artwork):
        try:
            with sqlite3.connect(artist_db) as con:
                rows = con.execute('INSERT INTO ARTWORK VALUES (?, ?, ?, ?)',
                                   (artwork.artist, artwork.name, artwork.price, artwork.available))
            con.close()
            return rows
        except sqlite3.IntegrityError:
            raise ArtworkError(f'Cannot be added, {artwork.name} already exists ')

    # Search all artwork
    def search_all_artwork(self, artist):
        con = sqlite3.connect(artist_db)
        artwork_cur = con.execute('SELECT * FROM ARTWORK where Artists = ?', (artist,))
        artworks = [Artwork(*row) for row in artwork_cur.fetchall()]
        con.close()
        return artworks

    # Search available artwork
    def search_available_artwork(self, artist):
        con = sqlite3.connect(artist_db)
        artwork_cur = con.execute('SELECT * FROM ARTWORK WHERE Artists like ? and available = 1', (artist,))
        artworks = [Artwork(*row) for row in artwork_cur.fetchall()]
        con.close()
        return artworks

    # Delete artwork by artwork name
    def delete_artwork(self, artwork):
        con = sqlite3.connect(artist_db)
        cursor = con.execute("delete from ARTWORK where name = ?", (artwork,))
        con.commit()
        con.close()
        if cursor.rowcount > 0:
            return True
        else:
            return False

    # Change artwork availability
    def change_artwork_status(self, artwork, available):
        con = sqlite3.connect(artist_db)
        cur = con.execute("UPDATE ARTWORK set available = ? where name = ?", (available, artwork))
        con.commit()
        con.close()
        if cur.rowcount > 0:
            return True
        else:
            return False
