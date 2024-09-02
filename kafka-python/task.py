import psycopg2
from faker import Faker
 
db_params = {
    'dbname': 'postgres',
    'user': 'postgres',
    'password': 'mysecretpassword',
    'host': 'localhost',
    'port': 5432
}
 
# Connect to PostgreSQL database
try:
    conn = psycopg2.connect(**db_params)
    print("Connected to the database.")
except Exception as e:
    print(f"Unable to connect to the database: {e}")
 
# Create a cursor object
cur = conn.cursor()
 
# Create a table
create_table_query = '''
CREATE TABLE IF NOT EXISTS employees (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    department VARCHAR(50),
    salary INTEGER
)
'''
cur.execute(create_table_query)
conn.commit()
print("Table created successfully.")
 
 
# Fetch table schema
cur.execute("SELECT column_name, data_type, is_nullable FROM information_schema.columns WHERE table_name = 'employees';")
schema = cur.fetchall()

# Generate random data
fake = Faker()
data = []
for _ in range(100):
    row = []
    for col in schema[1:]:
        if col[1] == 'integer':
            row.append(fake.random_int())
        elif col[1] == 'character varying':
            row.append(fake.name())
    data.append(row)

# Insert data into the table
insert_query = '''
INSERT INTO employees ( salary, name, department)
VALUES (%s, %s, %s)
'''

cur.executemany(insert_query, data)
conn.commit()
print("Data inserted successfully.")
 
 
# Close the cursor and connection

cur.close()
conn.close()
print("Database connection closed.")
