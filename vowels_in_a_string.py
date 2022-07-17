n=input()
m=input()
c=0
for i in n:
    for i in m:
        if i in "aeiou":
            c+=1
if(c!=0):
    print("True")
    print(n.index(i))
else:
    print("False")
        
        
        