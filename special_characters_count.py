str=input()
c=0
v="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
b=' '
for i in str:
    if i not in v and i not in b:
        c+=1
print(c)