from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StructField, StringType, IntegerType
 
spark = SparkSession.builder.appName("Customer Data")\
    .config('spark.jars', "./postgresql-42.7.3.jar") \
    .getOrCreate()

# Read data from Kafka
df1 = spark.readStream \
   .format("kafka") \
   .option("kafka.bootstrap.servers", "kafka:9092") \
   .option("subscribe", "postgres.public.customer") \
   .option("includeHeaders", "true") \
   .load()
 
# Print raw Kafka data schema 
print("Schema of raw Kafka data:")
df1.printSchema()
 
# convert the binary value to json
raw_df = df1.selectExpr("CAST(value AS STRING) as json_value")
 
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

# Parse the JSON data using the defined schema
parsed_df = raw_df.select(from_json(col("json_value"), message_schema).alias("data")) \
   .select("data.payload.after.*")
 
transformed_df = parsed_df.withColumn("total_amount", col("amount") + 50)
  
# Define PostgreSQL JDBC properties
psql_jdbc_url = "jdbc:postgresql://postgres:5432/exampledb"
psql_jdbc_properties = {
    "user": "docker",
    "password": "docker",
    "driver": "org.postgresql.Driver"
}

# Function to write to PostgreSQL
def write_to_psql(batch_df, batch_id):
    try:
        print(f"Batch ID: {batch_id}")
        batch_df.show()
        batch_df.write.jdbc(
            url=psql_jdbc_url,
            table="sink_customer",
            mode="append",
            properties=psql_jdbc_properties
        )
        print(f"Batch {batch_id} written to PostgreSQL successfully.")
    except Exception as e:
        print(f"Error writing batch {batch_id} to PostgreSQL: {e}")

# Write the transformed data to PostgreSQL
query = transformed_df.writeStream \
   .foreachBatch(write_to_psql) \
   .outputMode("append") \
   .start()

query.awaitTermination()
