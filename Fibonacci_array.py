n=int(input())
l=list(map(int,input().split()))
if l[n-1]!=l[n-2]+l[n-3]:
    print('no')
else:
    for i in range(n-2):
        if l[i]+l[i+1]!=l[i+2]:
            print('no')
            break
    else:
        print('yes')