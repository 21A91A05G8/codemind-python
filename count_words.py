s=input().split()
#s=list(s.split())
c=0

for i in s:
    if(i[0] in 'aeiouAEIOU' and i[len(i)-1] in 'qwrtypsdfghjklmnbvcxzQWSRDTFYGHJKPLMNBVCXZ'):
        c+=1
print(c)