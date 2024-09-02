# longest substring without repeating characters
s = "pwwkew"
ans = ""
max_length = 0

for i in range(len(s)):
    ans = s[i]
    for j in range(i + 1, len(s)):
        if s[j] not in ans:
            ans += s[j]
        else:
            break
    max_length = max(max_length, len(ans))

print(max_length)
