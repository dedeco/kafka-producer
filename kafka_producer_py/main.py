import sys
from kafka_producer_py.producer_purchases import ProducerPurchases
from kafka_producer_py.topic import Topic
from multiprocessing import Process


def run():
    """Checks for topic and creates the topic if it does not exist"""

    if len(sys.argv) != 3:
        raise Exception("Exactly 2 arguments are required: <BROKER_URL> <TOPIC_NAME>. eg: PLAINTEXT://127.0.0.1:9092 "
                        "com.google.sample.purchases")

    BROKER_URL = sys.argv[1]
    TOPIC_NAME = sys.argv[2]

    Topic(BROKER_URL, TOPIC_NAME).create_topic()

    qty_process = 5
    processes = []
    try:
        for i in range(qty_process):
            p = Process(target=ProducerPurchases(BROKER_URL, TOPIC_NAME).produce(i))
            p.start()
            processes.append(p)

        for t in processes:
            t.join()

    except KeyboardInterrupt as e:
        print("shutting down")


