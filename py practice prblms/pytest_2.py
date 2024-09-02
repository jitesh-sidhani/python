s="()))"   # output= 2
#s=")))()()()))())) )((("  # output = 5
count=0

for i in s:
    if i==")":
        count=count+1
    elif i=="(":
        count=count-1

print(count)




# l=0
# r=0
# for i in s:
#     if i=="(":
#         l=l+1
#     elif i==")":
#         r=r+1         

# if l==r:
#     print(0)
# else:
#     print(r-l)


