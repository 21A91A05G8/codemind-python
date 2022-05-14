t=int(input())
for i in range(t):
    n,a,b,k=map(int,input().split( ))
    c1=((n-a)//a)+1
    c2=((n-b)//b)+1
    c3=((n-(a*b))//(a*b))+1
    if(c1+c2-c3>k):
        print("Win")
    else:
        print("Lose")