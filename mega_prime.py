n=int(input())
c=0
for i in range(2,int((n**0.5)+1)):
    if n%i==0:
        print('Not Mega Prime')
        break
else:
    while(n):
        d=n%10
        n=n//10
        for i in range(2,int((d**0.5)+1)):
            if(d%i==0):
                c+=1
                break
        if(d==1):
            c+=1
            break
    if(c==0):
        print('Mega Prime')
    else:
        print('Not Mega Prime')