s='dddsssddddksj'
p = ""
for i in range(len(s)):
    for j in range(i, len(s)):
        sub = s[i:j + 1]
        if sub == sub[::-1] and len(sub) > len(p):
            p = sub
print(p)