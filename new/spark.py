from pyspark.sql import SparkSession

# Initialize Spark session
spark = SparkSession.builder.appName("Spark Streaming").getOrCreate()

# Define Kafka parameters
kafka_bootstrap_servers = "localhost:9092"
topic_name = "example_topic"

# Read data from Kafka topic using Spark Streaming
kafka_stream = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", kafka_bootstrap_servers) \
    .option("subscribe", topic_name) \
    .load()

# Select the value column from the Kafka stream
data_stream = kafka_stream.selectExpr("CAST(value AS STRING)")

# Write the result to console
data_stream.writeStream \
    .outputMode("append") \
    .format("console") \
    .start() \
    .awaitTermination()

# Stop the Spark session
spark.stop()