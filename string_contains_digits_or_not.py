t=int(input())
c=0
for i in range(t):
    s=input()
    c=0
    for j in s:
        if j.isdigit():
            c+=1
    if c!=0:
        print("Yes")
    else:
        print("No")