pro=int(input())
flag=0
for i in range(1,pro+1):
    if(i*(i+1)==pro):
        flag=1
        break
if(flag==1):
    print("YES")
else:
    print("NO")