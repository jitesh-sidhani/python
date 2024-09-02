from pyspark.sql import SparkSession
import pandas as pd
from pyspark.sql.functions import split, explode

spark =  SparkSession.builder.appName("new1").getOrCreate()
print(spark)

df = spark.createDataFrame(
    [
        ("sue", 32),
        ("li", 3),
        ("bob", 75),
        ("heo", 13),
    ],
    ["first_name", "age"],
)
print("hello world")
print(spark)
print(df.show())
# df.writeStream.format("console").start()
# Read from Kafka
df1 = spark \
    .readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "172.17.0.2:9092") \
    .option("subscribe", "postgres.public.student") \
    .option("includeHeaders", "true") \
    .load()

# .option("kafka.bootstrap.servers", "kafka-server")"kafka:9092" "localhost:9092" \
print("df1: ",df1)
print("going to print type of data")
print(type(df1))
print("going to print data")

parsed_df = df1.selectExpr("CAST(key AS STRING)", "CAST(value AS STRING)")
 
query = parsed_df.writeStream \
    .outputMode("append") \
    .format("console") \
    .start()