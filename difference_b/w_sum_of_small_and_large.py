s=input().split()
s1=0
s2=0
for i in s:
    s1+=ord(min(i))
    s2+=ord(max(i))
print(s2-s1)