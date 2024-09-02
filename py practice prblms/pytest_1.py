ans1=[]
ans2=[]
s1="axx#bb#c"  #axbc
s2="axbd#c#c"  #axbc

def backspacedString(s):
    result = []
    for i in s:
        if i != '#':
            result.append(i)
        elif i == '#':
            result.pop()   

    return ''.join(result)

print(backspacedString(s1))
print(backspacedString(s2))



# for i in s1:
#     if i=="#":
#         ans1.pop()
#     elif i!="#":
#         ans1.append(i)

# ans1="".join(ans1)
# print(ans1)

# for i in s2:
#     if i=="#":
#         ans2.pop()
#     elif i!="#":
#         ans2.append(i)

# ans2="".join(ans2)
# print(ans2)

# if ans1==ans2:
#     print("1")
# elif ans1!=ans2:
#     print("0")