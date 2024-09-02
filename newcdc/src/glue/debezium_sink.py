from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

# Initialize Spark Session
spark = SparkSession.builder \
    .appName("Data") \
    .config('spark.jars', "./postgresql-42.6.1.jar") \
    .getOrCreate()

# Define the schema for the Kafka data
payload_after_schema = StructType([
   StructField("id", IntegerType(), True),
   StructField("city", StringType(), True),
   StructField("item", StringType(), True),
   StructField("amount", IntegerType(), True)
])

payload_schema = StructType([
    StructField("after", payload_after_schema, True)
])

message_schema = StructType([
    StructField("payload", payload_schema, True)
])

# Read data from Kafka
df1 = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "kafka:9092") \
    .option("subscribe", "postgres.public.customer") \
    .option("includeHeaders", "true") \
    .load()

# Extract the JSON value from the Kafka message
raw_df = df1.selectExpr("CAST(value AS STRING) as json_value")

# Parse the JSON data using the defined schema
parsed_df = raw_df.select(from_json(col("json_value"), message_schema).alias("data")) \
    .select("data.payload.after.*")

debezium_sink_properties = {
    "connector.class": "io.debezium.connector.postgresql.PostgresSinkConnector",
    "tasks.max": "1",
    "topics": "postgres.public.customer",
    "database.hostname": "postgres",
    "database.port": "5432",
    "database.username": "docker",
    "database.password": "docker",
    "database.dbname": "exampledb2",
    "schema.name": "public"
}

# Write the parsed data to PostgreSQL using Debezium Sink Connector
query = parsed_df.writeStream \
    .format("debezium-sink") \
    .options(**debezium_sink_properties) \
    .start()

query.awaitTermination()