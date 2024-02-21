import unittest
from src.components.db import DBConnection, Counts

testDB='pokedb_test'
date='2024-1-1'
class TestDB(unittest.TestCase):
    def setUp(self):
        self.db=DBConnection(testDB)
    #integration test
    def test_connection(self):
        self.assertEqual(self.db.getConn().is_active, True)
    #unit test
    def test_pullNames(self):
        count=self.db.pullNames()
        self.assertEqual(len(count), 3439)  

    def test_findName(self):
        name=self.db.findByName('bulbasaur')
        self.assertEqual(name.pokemon_id, 1)
        self.assertEqual(name.image, 'https://raw.githubusercontent.com/Purukitto/pokemon-data.json/master/images/pokedex/hires/001.png')

    def test_InsertOneAtDate(self):
        a=self.db.insertOneAtDate(1, date).hits
        b=self.db.insertOneAtDate(1, date).hits
        self.assertEqual(b,a+1) 

if __name__ == '__main__':
    unittest.main()
