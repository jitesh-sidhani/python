from kafka.admin import NewTopic 
from kafka import KafkaAdminClient


admin_client = KafkaAdminClient(
    bootstrap_servers="localhost:9092", 
    client_id='test'
)

topic_list = []
# topic_list.append(NewTopic(name="example_topic", num_partitions=1, replication_factor=1))
# admin_client.create_topics(new_topics=topic_list, validate_only=False)

## topic is created - "example_topic"
print(admin_client.list_topics())
# print(example_topic)
