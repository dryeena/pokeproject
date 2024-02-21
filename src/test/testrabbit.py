import unittest
from src.components.rabbit import RabbitConnection
class TestRabbit(unittest.TestCase):
    def setUp(self):
        self.rabbit=RabbitConnection(queue="test_queue")  

    #integration test
        
    
    def test_connection(self):
        self.assertTrue(self.rabbit.connection.is_open)
        self.rabbit.send('test message')
        self.assertTrue(self.rabbit.connection.basic_nack)
        self.rabbit.close()

    def test_close_connection(self):
        self.rabbit.close()
        self.assertTrue(self.rabbit.connection.is_closed)
        

if __name__ == '__main__':
    unittest.main()
