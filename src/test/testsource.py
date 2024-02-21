import unittest
from src.components.source import APISource

appURL=f"https://www.reddit.com/r/pokemon/new.json?limit=50"

class TestSource(unittest.TestCase):
    def setUp(self):
        self.source=APISource()
        self.request=self.source.getRequest(appURL)
          
    #integration test
    def test_connection(self):
        self.assertEqual(self.request.status_code, 200)
        
    def test_count(self):
        count=self.request.json()['data']['children']
        self.assertEqual(len(count), 50)        

if __name__ == '__main__':
    unittest.main()
