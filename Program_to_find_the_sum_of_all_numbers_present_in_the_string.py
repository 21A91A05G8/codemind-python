import math
s=input()
sum=0
for i in s:
    if i.isdigit():
        sum=sum+int(i)
print(sum)    