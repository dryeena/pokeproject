import unittest
from mocks import Mocks
from src.apps.analyzer import Analyzer
import datetime
date=datetime.datetime(year=2024,month=1,day=1).timestamp()

class TestAnalyzer(unittest.TestCase):

    def setUp(self):
        self.mock=Mocks()
        
        self.Analyzer=Analyzer(rabbit=self.mock, db=self.mock, testing=True)
        
    def test_collect(self):
        test=self.Analyzer.collect(self.mock, self.mock, self.mock, self.mock)
        self.assertEqual(test['name'], 'bulbasaur')
    def test_hitDB(self):
        test=self.Analyzer.addToDB(id=1, created=date)
        self.assertEqual(test.hits, 1)

if __name__ == '__main__':
    unittest.main()
