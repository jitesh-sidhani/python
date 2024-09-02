n=5

for row in range(0,n):
    for col in range(0,n):
        if row==0 or col==(n-1) or row==col:
            print("*",end="")
        else:
            print(end=" ")
    print()

    
# for i in range(n,0,-1):
#     for j in range(0,n-i):     # lower pyramid
#         print(end=" ")
#     for j in range(0,i):
#         print("*",end=" ")
#     print()


# for i in range(0,n):    # pyramid
#     for j in range(0,n-i-1):
#         print(end=" ")

#     for j in range(0,i+1):
#         print("*",end=" ")
#     print()


# for i in range(0,n):    #upper diamond
#     for j in range(0,n-i-1):
#         print(end=" ")

#     for j in range(0,i+1):
#         print("*",end=" ")
#     print()



# for i in range(n,0,-1):
#     for j in range(1,i+1):
#         print("*",end="")
#     print()



# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print("*",end="")
#     print()