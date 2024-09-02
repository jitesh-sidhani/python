from pyspark.sql import SparkSession

# Initialize Spark session
spark = SparkSession.builder.appName("LocalGlueJob").getOrCreate()

 # Read data from a local CSV file
# df = spark.read.option("header", "true").csv("/home/glue_user/workspace/data/input.csv")

# Perform transformations
# df_transformed = df.filter(df["column"] > 10)
# df_transformed.show()

# Write the result to a local file
df_transformed.write.csv("/home/glue_user/workspace/data/output", header=True)

# Stop the Spark session
spark.stop()
