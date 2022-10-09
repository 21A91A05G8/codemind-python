s=input()
c=0
for i in sorted(set(s)):
    if(i>='a' and i<='z'):
        print(i,end='')