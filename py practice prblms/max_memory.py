

n = 5  # Number of elements in task_memory
task_memory = [7, 2, 23,2, 9] #mem
task_type = [1, 2, 1,1, 3] #type
max_memory = 23
ways = 0
myDict = {}

for i in range(n):
    if task_type[i] in myDict:
        myDict[task_type[i]] += task_memory[i]
    else:
        myDict[task_type[i]] = task_memory[i]
       
print(myDict)

for k, v in myDict.items():
    while v > max_memory:
        v =v- max_memory
        ways += 1
    if v > 0:
        ways += 1


print(ways)
