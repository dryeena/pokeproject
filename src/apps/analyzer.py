from src.components.rabbit import RabbitConnection
from src.components.db import DBConnection
import string, random, json, datetime

worker=f"Worker {random.choice(string.ascii_uppercase)}"
class Analyzer():
    def __init__(self, rabbit=None, db=None, testing=False):
        self.rabbit = rabbit or RabbitConnection()
        self.db = db or DBConnection()
        self.names = self.loadNames()
        self.testing = testing

    def collect(self, ch, method, _, body):
        collection=json.loads(body.decode())        
        print(f"[x] {worker} - Received job {collection['data']['name']}") if not self.testing else None
        self.analyze(collection['data'])
        print(f"[x] {worker} - Completed job") if not self.testing else None
        ch.basic_ack(delivery_tag=method.delivery_tag)

        return collection['data']
    def getDate(timestamp):
        return datetime.datetime.fromtimestamp(timestamp)
    def analyze(self, source):
        for name in self.names:
            if name.name in source['selftext']:
                self.addToDB(name.pokemon_id, name.name, source['created'])
    def loadNames(self):
        dbout = self.db.pullNames()
        return dbout
        
    def addToDB(self, id, name='', created=0):
        date=Analyzer.getDate(created)
        print(f"[*] {worker} - match found for {name}, id {id} at {date}") if not self.testing else None
        return self.db.insertOneAtDate(id, date.date())

if __name__ == '__main__':
    analyzer=Analyzer()
    print("[*] {worker} - Waiting for messages. To exit press CTRL+C")
    analyzer.rabbit.receive(analyzer.collect)

