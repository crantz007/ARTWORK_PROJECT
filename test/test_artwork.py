import unittest
from unittest import TestCase
import sqlite3
from exceptions.artworkError import ArtworkError
from model.Model import Artwork
from model.Model import Artist
from database import Artwork_db


class test_artworkDB(TestCase):
    test_artworkDB = 'test_artwork.db'

    def setUp(self):
        Artwork_db.artist_db = self.test_artworkDB
        with sqlite3.connect(self.test_artworkDB) as con:
            con.execute('drop table if exists ARTWORK')
            con.execute('drop table if exists ARTIST')
        con.close()
        with sqlite3.connect(self.test_artworkDB) as con:
            con.execute('create table ARTIST(Artists text not null, email text unique not null)')
            con.execute(
                'create table ARTWORK(Artists text not null, name text unique , price float , available integer, foreign key(Artists) references ARTIST(Artists))')
        con.close()

        self.artist_db = Artwork_db.SQLArtworkDB()

    def test_add_artwork(self):

        ar = Artwork('Kobe', 'Bryant', 100, 1)
        self.artist_db.insert_artwork(ar)
        expected = {'Kobe': 'Bryant', 100: 1}
        self.compare_db_add_artwork(expected)

    def test_delete_artwork(self):
        a1 = Artwork('Max', 'Crantz', 100, 1)
        self.artist_db.insert_artwork(a1)
        self.artist_db.delete_artwork('Crantz')
        expected = {'Max', 'Crantz', 100, 1}
        self.delete_status(expected)

    def delete_status(self, expected):
        con = sqlite3.connect(self.test_artworkDB)
        query = con.execute('select * from ARTWORK').fetchall()
        for row in query:
            self.assertNotIn(row[0], expected.keys())

    def test_duplicate_artwork(self):
        ar = Artwork('Kobe', 'Molly', 100, 0)
        self.artist_db.insert_artwork(ar)
        ar2 = Artwork('Kobe', 'Molly', 100, 0)
        with self.assertRaises(ArtworkError):
            self.artist_db.insert_artwork(ar2)

    def test_change_status(self):
        ar = Artwork('Clark', 'Bill', 100, 0)
        self.artist_db.change_artwork_status('Bill', 1)
        self.artist_db.insert_artwork(ar)
        expected = {'Clark': 'Bill', 100: 1}
        self.compare_db_add_artwork(expected)

    def compare_db_add_artwork(self, expected):
        conn = sqlite3.connect(self.test_artworkDB)
        all_data = conn.execute('SELECT * FROM ARTWORK').fetchall()

        for row in all_data:
            self.assertIn(row[0], expected.keys())
            self.assertEqual(expected[row[0]], row[1])

    def test_add_artist(self):
        at = Artist('Jordan', 'jordan@gmail.com')
        self.artist_db.insert_artist(at)
        expected = {'Jordan': 'jordan@gmail.com'}
        self.compare_db_add_artist(expected)

    def test_add_duplicate_artist(self):
        dat1 = Artist('Karen', 'karen@gmail.com')
        self.artist_db.insert_artist(dat1)
        dat2 = Artist('Karen', 'karen@gmail.com')
        with self.assertRaises(ArtworkError):
            self.artist_db.insert_artist(dat2)

    def test_add_empty_artwork_in_store(self):
        at = Artwork('', '', 100, 1)
        self.assertRaises(ArtworkError)

    def test_add_empty_artist_in_store(self):
        ar = Artist('', '')
        self.assertRaises(ArtworkError)

    def compare_db_add_artist(self, expected):
        con = sqlite3.connect(self.test_artworkDB)
        query = con.execute('SELECT * FROM ARTIST').fetchall()
        con.close()
        for row in query:
            self.assertIn(row[0], expected.keys())
            self.assertEqual(expected[row[0]], row[1])
        con.close()


if __name__ == '__main__':
    unittest.main()
