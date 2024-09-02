# arr=[1,2,3,4]
# size=len(arr)  #4

# temp=arr[0]
# arr[0]=arr[size-1]
# arr[size-1]=temp    
# print(arr)

# Input: list = [4, 5, 6, 7, 8, 9]
# #Output: [9, 8, 7, 6, 5, 4] 

# print(Input[::-1])


# Original dictionary
# original_dict = {'gfg': [5, 6, 7, 8], 'is': [10, 11, 7, 5], 'best': [6, 12, 10, 8], 'for': [1, 2, 5]}

# unique=[]

# for value_list in original_dict.values():
#     for j in value_list:
#         if j not in unique:
#             unique.append(j)

# print(sorted(unique))

# Python code to demonstrate
# insertion of items in beginning of ordered dict
# from collections import OrderedDict

# # Initialising ordered_dict
# iniordered_dict = OrderedDict([('akshat', '1'), ('nikhil', '2')])

# # Inserting items in starting of dict
# iniordered_dict.update({'manjeet': '3'})
# iniordered_dict.move_to_end('manjeet', last=True)

# # Printing result
# print("Resultant Dictionary : "+str(iniordered_dict))


# list1 = [3, 2, 4]
# list1.pop(0)
# print(list1)
# #Output : 24 
# ans=1
# for i in range(len(list1)):
#     ans=ans*list1[i]
# print(ans)

names=["john","james","emmy"]
j=[]

for i in names:
    if 'j' in i:
        j.append(i)
print(j)