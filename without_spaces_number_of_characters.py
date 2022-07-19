k=input()
c=0
for i in range(0,len(k)):
    if(ord(k[i])!=32):
        c+=1
print(c)