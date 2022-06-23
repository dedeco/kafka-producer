from confluent_kafka import Producer

from kafka_producer_py.purchase import Purchase


class ProducerPurchases:

    def __init__(self, brokers_url: str, topic: str):
        self.brokers_url = brokers_url
        self.topic = topic

    def produce(self, process: int):
        """Produces data into the Kafka Topic"""
        p = Producer({"bootstrap.servers": self.brokers_url})
        num_produced = 0
        while num_produced < 1000:
            p.produce(self.topic, Purchase().serialize())
            p.flush()
            num_produced += 1
            if num_produced % 100 == 0:
                print(f"produced {num_produced} messages in process {process}")

