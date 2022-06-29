s=input()
c=0
v="aeiouAEIOU"
for i in range(len(s)):
    if s[i] in v:
        c+=1
print(c)        