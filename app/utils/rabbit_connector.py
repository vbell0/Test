import json
import pika

from app.settings import BROKER_URL, BROKER_LOGIN, BROKER_PASSWORD


class RabbitMQConnector:
    def __init__(self):
        self.url = f'amqps://{BROKER_LOGIN}:{BROKER_PASSWORD}@{BROKER_URL}'
        self.conn_parameters = None
        self.connection = None
        self.channel = None
        self.connect()

    def connect(self):
        self.conn_parameters = pika.URLParameters(self.url)
        self.connection = pika.BlockingConnection(self.conn_parameters)
        self.channel = self.connection.channel()

    def publish_message(self, exchange, body):
        try:
            body = {'event': exchange, 'object': body}
            body = json.dumps(body)
            self.channel.basic_publish(exchange=exchange, routing_key='', body=body)
        except Exception as error:
            self.connect()
            self.channel.basic_publish(exchange=exchange, routing_key='', body=body)

    def declare_exchange(self, exchange):
        self.channel.exchange_declare(exchange=exchange, exchange_type='fanout', durable=True)
