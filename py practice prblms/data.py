import random
import names

data = {}

# Generate random data for 50 rows
for i in range(1, 51):
    # Generate a random name
    name = names.get_full_name()
    
    # Generate a random salary between $30,000 and $150,000
    salary = random.randint(30000, 150000)
    
    # Generate a random department number between 1 and 10
    department = random.randint(1, 10)
    
    # Store the data in the dictionary
    data[i] = {
        'Name': name,
        'Salary': salary,
        'Department': department
    }

# Print the generated data
data1=[]
for i,row in data.items():
    
    data1.append(row)
    
print(data1)





