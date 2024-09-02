# s1 = "America"
# s2 = "Japan"
# #Expected Output: AJrpan

# m1=len(s1)//2
# m2=len(s2)//2

# ans=s1[0]
# ans=ans+s2[0]

# ans=ans+s1[m1]
# ans=ans+s2[m2]

# ans=ans+s1[-1]
# ans=ans+s2[-1]

# print(ans)



n1 = [1,2,3,0,0,0]
m = 3
n2 = [2,5,6]
n = 3 
new=[]
#Output: [1,2,3,5,6]
i=0
j=0

while i<m and j<n:
    if n1[i]<n2[j]:
        new.append(n1[i])
    elif n1[i]==n2[j]:
        new.append(n1[i])
    elif n1[i]>n2[j]:
        new.append(n2[j])
        
print(new)
        



















# def mutate_string(string, position, character):
#     for i in range(0,len(string)):
#         if i==position:
#             ans=string.replace(i,character )
#     return ans

# if __name__ == '__main__':
#     s = "abracadabra"
#     i, c = input().split()
#     s_new = mutate_string(s, int(i), c)
#     print(s_new)