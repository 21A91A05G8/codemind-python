a=input()
b=""
for i in a:
    if i in"aeiou":
        if i not in b:
            b=b+i
if(len(b)==5):
    print("True")
else:
    print("False")