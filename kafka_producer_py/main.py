import sys

from kafka_producer_py.producer_purchases import ProducerPurchases
from kafka_producer_py.topic import Topic


def run():
    """Checks for topic and creates the topic if it does not exist"""

    if len(sys.argv) != 4:
        raise Exception("Exactly 2 arguments are required: <BROKER_URL> <TOPIC_NAME> <QUANTITY OF MESSAGES>. eg: "
                        "PLAINTEXT://127.0.0.1:9092 "
                        "com.google.sample.purchases "
                        "10 ")

    BROKER_URL = sys.argv[1]
    TOPIC_NAME = sys.argv[2]
    MESSAGES = int(sys.argv[3])

    Topic(BROKER_URL, TOPIC_NAME).create_topic()

    try:
        ProducerPurchases(BROKER_URL, TOPIC_NAME)\
            .produce(MESSAGES)
    except KeyboardInterrupt as e:
        print("shutting down")
