# Input = [81, 52, 45, 10, 3, 2, 96] 
# N = 3
# # Output :  [9, 5]

# Input.sort(reverse=True)
# print(Input[0:N])

# phone="12-3-45-688"

# result=phone.count('-')
# print(result)


# list1=[1,2,3,4,5,6,7,8]
# #expected 

# if len(list1)<=1:
#     print(list1)
# first=list1[0]
# rotated=list1[1:] + [first]
# print(rotated)


# arr = [12, 10, 5, 6, 52, 36]
# n=len(arr)
# d = 2
# #Output: arr[] = [3, 4, 5, 6, 7, 1, 2] 
# new=[]
# if n<=1:
#     print(arr)
# for i in range(d,n):
#     new.append(arr[i])

# for j in range(0,d):
#     new.append(arr[j])
# print(new)




# Input : 6 5 4 4
# Output : true

# Input : 5 15 20 10
# Output : false

# def check(arr):
#     flag=False
#     for i in range(len(arr)-1):
#         if arr[i+1]<=arr[i] or arr[i+1]>=arr[i]:
#             flag=True
#         else:
#             flag=False
#     return flag

# arr=[6,5,4,4]
# result=check(arr)
# print(result)


# def check(arr):
    
#     for i in range(len(arr) - 2):
#         if arr[i] >= arr[i+1] and arr[i+1] <= arr[i+2]:
#             return False
#         if arr[i] <= arr[i+1] and arr[i+1] >= arr[i+2]:
#             return False
#         # if arr[i]==arr[i+1] and arr[i+1]> arr[i+2]:
#         #     return False
        
#     return True

# arr=[5, 15, 20 ,20,20,20,30]
# result=check(arr)
# print(result)

def isMonotonic(A):
    x, y = [], []
    x.extend(A)
    y.extend(A)
    x.sort()
    y.sort(reverse=True)
    if x == A or y == A:
        return True
    return False


# Driver program
A = [6, 5, 4, 4]

# Print required result
print(isMonotonic(A))