from confluent_kafka.admin import AdminClient, NewTopic


class Topic:

    def __init__(self, brokers_url: str, topic: str):
        self.client = AdminClient({"bootstrap.servers": brokers_url})
        self.topic = topic

    def create_topic(self):
        """Creates the topic with the given topic name"""
        futures = self.client.create_topics(
            [NewTopic(topic=self.topic, num_partitions=5, replication_factor=1)]
        )
        for _, future in futures.items():
            try:
                future.result()
            except Exception as e:
                print("exiting production loop")
