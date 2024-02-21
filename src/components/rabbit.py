import pika
import os

connectionName=os.environ.get('RABBITHOST','localhost')
queueName=os.environ.get('RABBITQUEUE','pokegatherer1')
exchangeName=os.environ.get('RABBITEXCHANGE','pokeGatherer')
exchangeType='direct'
routingKey='42'
class RabbitConnection:
    def __init__(self, exchangeType=exchangeType, queue=queueName):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(connectionName))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=queue, durable=True)
        self.channel.exchange_declare(exchangeName, durable=True, exchange_type=exchangeType)
        self.channel.queue_bind(exchange=exchangeName, queue=queueName, routing_key=routingKey)        
    def close(self):
        self.connection.close()

    def send(self, message):
        self.channel.basic_publish(exchange=exchangeName, routing_key=routingKey, body=message)

    def receive(self, method):
        self.channel.basic_qos(prefetch_count=10)
        self.channel.basic_consume(queue=queueName, on_message_callback=method)
        self.channel.start_consuming()

        

