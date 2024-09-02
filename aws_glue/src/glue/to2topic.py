import time
from pyspark.sql.functions import col, avg  
from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DecimalType,DoubleType
from pyspark.sql.functions import concat, lit

spark = SparkSession.builder \
    .appName("Data") \
    .getOrCreate()

# Define the schema for the Kafka data
payload_after_schema = StructType([
    StructField("year_month", StringType(), True),
    StructField("Sales +", DoubleType(), True),
    StructField("Expenses +", DoubleType(), True),
    StructField("Operating profit", DoubleType(), True),
    StructField("OPM %", DoubleType(), True),
    StructField("Other Income +", DoubleType(), True),
    StructField("Interest", DoubleType(), True),
    StructField("Depreciation", DoubleType(), True),
    StructField("Profit before tax", DoubleType(), True),
    StructField("Tax %", DoubleType(), True),
    StructField("Net Profit +", DoubleType(), True),
    StructField("EPS in Rs", DoubleType(), True),
    StructField("Dividend payout %", DoubleType(), True),
])

payload_schema = StructType([
    StructField("after", payload_after_schema, True)
])


message_schema = StructType([
    StructField("payload", payload_schema, True)
])


df1 = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "kafka:9092") \
    .option("subscribe", "postgres.public.profit_loss_data_transposed") \
    .option("includeHeaders", "true") \
    .load()

print("Schema of raw Kafka data:")
df1.printSchema()


raw_df = df1.selectExpr("CAST(value AS STRING) as json_value")


print("Printing raw JSON values from Kafka:")
query1 = raw_df.writeStream \
    .format("console") \
    .option("truncate", "false") \
    .start()


parsed_df = raw_df.select(from_json(col("json_value"), message_schema).alias("data")) \
    .select("data.payload.after.*")


print("Printing parsed data after applying schema:")
query2 = parsed_df.writeStream \
    .format("console") \
    .option("truncate", "false") \
    .start()


transformed_df = parsed_df.withColumn("bouns", concat(lit('abc'), col('year_month')))

print("Printing transformed data to verify the transformation:")
query3 = transformed_df.writeStream \
    .format("console") \
    .option("truncate", "false") \
    .start()



query4 = transformed_df.selectExpr( "to_json(struct(*)) AS value") \
    .writeStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "kafka:9092") \
    .option("topic", "new_topic") \
    .option("checkpointLocation", "/tmp/checkpoints") \
    .start()

spark.streams.awaitAnyTermination()
