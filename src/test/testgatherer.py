import unittest
from src.apps.gatherer import Gatherer
from mocks import Mocks
class TestGatherer(unittest.TestCase):

    def setUp(self):
        self.mock=Mocks()        
        self.Gatherer=Gatherer(rabbit=self.mock, api=self.mock)
        
    def test_push(self):
        self.assertEqual(self.Gatherer.push('message'), None)

    def test_pull(self):
        b=self.Gatherer.pull('r/fake')
        self.assertEqual(len(b), 50)

if __name__ == '__main__':
    unittest.main()
