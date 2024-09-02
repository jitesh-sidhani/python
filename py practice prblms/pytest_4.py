# ans1=""
# ans2=""
# ans3=""

# text="an extremely dangerous dog is barking"
# print("original:-",text)

# ans1=text.replace('ing','')
# ans2=ans1.replace('ed','')
# ans3=ans2.replace('ly','')

# print(ans3)

# for i in ans3:
#     if len(i)>8:
#         ans3=i[:8]
# print(ans3)

# #remove- ed ly ing
# for i in text:
#     for j in i:
#         if j=="ed":
#             new.append(j[0:4])

# print(new)
text = "an extremely dangerous dog is barking"
text = text.split()
result= []
for word in text:
    if word.endswith(('ed', 'ly')):
        word = word[:-2]
    elif word.endswith(('ing')):
        word = word[:-3]
    if len(word) > 8:
        word = word[:8]
    result.append(word)

print(' '.join(result))










# t="dangerous"

# print(t[0:5])