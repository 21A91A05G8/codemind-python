s1=input().lower()
s2=input().lower()
k=[]
for i in s1:
    if i not in s2:
        k.append(i)
for i in s2:
    if i not in s1:
        k.append(i)
for i in sorted(set(k)):
    if i!=' ':
        print(i,end='')