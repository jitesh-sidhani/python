str1 = "PYnative29@#8496"
# Expected Outcome: Sum is: 38 Average is  6.333333333333333
new=""
for i in str1:
    if i.isnumeric():
        new=new+i
print(new)
ans=0
for i in new:
    ans=ans+int(i)

average = ans / len(new)
print(ans)
print(average)















# s1 = "Yn"
# s2 = "PYnative"

# def string_balance_test(s1, s2):
#     flag = True
#     for char in s1:
#         if char in s2:
#             continue
#         else:
#             flag = False
#     return flag

# ans=string_balance_test(s1,s2)
# print(ans)



# str1 = 'PyNaTive'
# # output - yaivePNT
# new=""
# str1.islower()
# for i in str1:
#     if i.islower():
#         new=new+i
# print(new)
# for i in str1:       
#     if i.isupper():
#         new=new+i
# print(new)


# s1 = "America"
# s2 = "Japan"

# # output:-  AJrpan
# x=""
# m1=len(s1)//2
# m2=len(s2)//2

# x=s1[0]+s2[0]
# x=x+s1[m1]+s2[m2]
# x=x+s1[-1]+s2[-1]

# print(x)


# s1 = "Ault"
# s2 = "Kelly"
# # Output:AuKellylt

# m=len(s1)//2

# x=s1[:m]
# x=x+s2+s1[m:]

# print(x)



# str1 = "JhonDipPeta"
# # Output- Dip

# str2 = "Jasons"
# # Output- Son

# new=""
# m=len(str2)//2

# new=str2[m-1:m+2]
# print(new)



# str="James"
# # out:- Jms
# new=""
# m=len(str)//2

# new=str[0]
# new=new+str[m]
# new=new+str[-1]

# print(new)