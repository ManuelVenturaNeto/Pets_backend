from typing import Dict
import json
import pika


class RabbitMQClient:
    """
    Class to manage rabbitMQ connections.
    """

    def __init__(self) -> None:
        self.__host = "localhost"
        self.__port = 5672
        self.__username = "guest"
        self.__password = "guest"
        self.__channel = self.__create_channel()
        self.__queue_name = None

    def __create_channel(self) -> pika.adapters.blocking_connection.BlockingChannel:
        """
        Creates and returns a RabbitMQ channel.
        """
        credentials = pika.PlainCredentials(self.__username, self.__password)
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(
                host=self.__host, port=self.__port, credentials=credentials
            )
        )
        return connection.channel()

    def set_queue(self, queue_name: str, durable: bool = True) -> None:
        """
        Sets the queue to be used by this client.

        :param queue_name: The name of the RabbitMQ queue.
        :param durable: If True, the queue will be durable (persistent).
        """
        self.__queue_name = queue_name
        self.__channel.queue_declare(queue=self.__queue_name, durable=durable)

    def send_message(self, body: Dict) -> bool:
        """
        Sends a message to the currently selected queue.

        :param body: The message to be sent.
        :return: True if the message is sent successfully, otherwise raises an exception.
        :raises ValueError: If the queue is not set before sending a message.
        """
        if not self.__queue_name:
            raise ValueError(
                "Queue not set. Use set_queue(queue_name) before sending messages."
            )

        self.__channel.basic_publish(
            exchange="",
            routing_key=self.__queue_name,
            body=json.dumps(body),
            properties=pika.BasicProperties(delivery_mode=2),  # Persistent messages
        )
        return True

    def close(self) -> None:
        """
        Closes the RabbitMQ connection.
        """
        self.__channel.close()
