#n=int(input("Enter a num:"))

# define size n = even only
n = 8
 
# so this heart can be made n//2 part left,
# n//2 part right, and one middle line
# i.e; columns m = n + 1
m = n+1
 
# loops for upper part
for i in range(n//2-1):
    for j in range(m):
         
        # condition for printing stars to GFG upper line
        if i == n//2-2 and (j == 0 or j == m-1):
            print("*", end=" ")
             
        # condition for printing stars to left upper
        elif j <= m//2 and ((i+j == n//2-3 and j <= m//4) \
                            or (j-i == m//2-n//2+3 and j > m//4)):
            print("*", end=" ")
             
        # condition for printing stars to right upper
        elif j > m//2 and ((i+j == n//2-3+m//2 and j < 3*m//4) \
                           or (j-i == m//2-n//2+3+m//2 and j >= 3*m//4)):
            print("*", end=" ")
             
        # condition for printing spaces
        else:
            print(" ", end=" ")
    print()


# k=1
# for i in range(1,n+1):
#     for j in range(1,k+1):
#         print("*",end="")
#     k=k+2
#     print()


# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print("*",end="")
#     print()