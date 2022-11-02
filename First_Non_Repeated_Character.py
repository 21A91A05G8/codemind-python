n=int(input())
for i in range(n):
    k=int(input())
    s=input()
    for i in range(k):
        if(s.count(s[i])==1):
            print(s[i])
            break
    else:
        print(-1)
    
