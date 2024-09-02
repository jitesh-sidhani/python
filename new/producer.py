import random
import names
from kafka import KafkaProducer
import json
#import pymysql
import psycopg2
import pandas as pd

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda x: json.dumps(x).encode('utf-8')
)

postgres = {
    'dbname': 'postgres',
    'user': 'postgres',
    'password': 'mysecretpassword',
    'host': 'localhost',
    'port': 5432
}
 
def fetch_data_from_postgres(query):
    connection = psycopg2.connect(**postgres)
    try:
        df = pd.read_sql_query(query, connection)
        return df
    finally:
        print("Connection closed")
        # connection.close()

query = 'SELECT * FROM employees'
df = fetch_data_from_postgres(query)
 
data_records = df.to_dict(orient='records')
data_records

for value in data_records:
    producer.send('example_topic', value)
producer.flush()


# employee_data = {}

# for i in range(1, 51):
#     name = names.get_full_name()
#     salary = random.randint(30000, 150000)
#     department = random.randint(1, 10)
    
#     employee_data[i] = {
#         'Name': name,
#         'Salary': salary,
#         'Department': department
#     }

# data1 = []
# for i, row in employee_data.items():
#     data1.append(row)

# for value in data1:
#     producer.send("example_topic", value)
# producer.flush()