from unittest.mock import Mock, MagicMock
from src.components.db import Counts

class Mocks():
    def __init__(self):
        self.basic_ack=Mock()
        self.basic_ack.return_value=True
        self.delivery_tag=Mock()
        self.delivery_tag.return_value=None
        self.send=Mock()
        self.send.return_value=None
        self.getFromSubreddit=Mock()
        self.getFromSubreddit.return_value=[1 for _ in range(50)]
        self.decode=Mock()
        self.decode.return_value='{"data": {"name": "bulbasaur", "selftext": 3} }'
        self.pullNames=Mock()
        self.pullNames.return_value=[]
        self.insertOneAtDate=Mock()
        self.insertOneAtDate.return_value=Counts(hits=1, pokemon_id=1, id=343)