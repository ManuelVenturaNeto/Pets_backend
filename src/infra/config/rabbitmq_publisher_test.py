import logging
import pytest
import pika
from .rabbitmq_publisher import RabbitMQClient

@pytest.mark.skip(reason="Sensive test")
def test_create_channel():
    """
    Testa se o canal RabbitMQ é criado corretamente.
    """
    client = RabbitMQClient()
    assert isinstance(
        client._RabbitMQClient__channel,
        pika.adapters.blocking_connection.BlockingChannel,
    )
    client.close()


@pytest.mark.skip(reason="Sensive test")
def test_set_queue():
    """
    Testa se a fila é declarada corretamente.
    """
    client = RabbitMQClient()
    client.set_queue("test_queue")
    assert client._RabbitMQClient__queue_name == "test_queue"
    client.close()


@pytest.mark.skip(reason="Sensive test")
def test_send_message():
    """
    Testa se a mensagem é enviada corretamente para a fila.
    """
    client = RabbitMQClient()
    client.set_queue("test_queue")

    message = {"key": "value"}
    assert client.send_message(message) is True

    client.close()


@pytest.mark.skip(reason="Sensive test")
def test_send_message_without_queue():
    """
    Testa se a tentativa de envio de mensagem sem definir uma fila gera um erro.
    """
    client = RabbitMQClient()

    with pytest.raises(ValueError, match="Queue not set. Use set_queue"):
        client.send_message({"key": "value"})

    client.close()


@pytest.mark.skip(reason="Sensive test")
def test_close_connection():
    """
    Testa se a conexão é fechada corretamente.
    """
    client = RabbitMQClient()
    client.close()

    with pytest.raises(pika.exceptions.ChannelWrongStateError):
        client._RabbitMQClient__channel.queue_declare(queue="should_fail")
