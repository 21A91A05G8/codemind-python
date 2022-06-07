n=int(input())
c=0
k=0
a=list(map(int,input().split()))
for i in range(len(a)):
    c=0
    for j in range(i+1,len(a),+1):
        if(a[i]==a[j]):
            c+=1
    k=k+c%2
print(k)    