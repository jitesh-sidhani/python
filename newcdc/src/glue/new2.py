from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StructField, StringType, IntegerType
 
# Initialize Spark Session
spark = SparkSession.builder \
    .appName("Data") \
    .config('spark.jars', "debezium-connector-jdbc-2.7.0.Final.jar") \
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
 
# Define PostgreSQL JDBC properties
psql_jdbc_url = "jdbc:postgresql://postgres:5432/exampledb2"
psql_jdbc_properties = {
    "user": "docker",
    "password": "docker",
    "driver": "org.postgresql.Driver"
}
 
# Function to write to PostgreSQL
def write_to_psql(batch_df, batch_id):
    try:
        print(f"Batch ID: {batch_id}")
        batch_df.show()  # Print the batch DataFrame for debugging
        # Check if the table exists and create if not
        batch_df.write.jdbc(
            url=psql_jdbc_url,
            table="customer",  # Ensure this matches your PostgreSQL table name
            mode="upsert",  # Insert new rows and update existing ones
            keyColumns=["id"],  # Specify the key column(s)
            properties=psql_jdbc_properties
        )
        print(f"Batch {batch_id} written to PostgreSQL successfully.")
    except Exception as e:
        print(f"Error writing batch {batch_id} to PostgreSQL: {e}")
 
# Write the parsed data to PostgreSQL
query = parsed_df.writeStream \
    .foreachBatch(write_to_psql) \
    .outputMode("update").option("updateMode", "upsert").start()

 
# Await termination of all queries
query.awaitTermination()