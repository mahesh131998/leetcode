s="()"
list=[]
j=0
d= len(s)
print(d)

for i in range(d):
    if s[i]=='(' or s[i]=='[' or s[i]=='{':
        list[j]= s[i]
        j= j+1
    elif s[i]==')' or s[i]==']' or s[i]=='}':
        if list[j]=='(':
            list= list.pop(j)
            j= j-1
        if list[j]=='[':
            list= list.pop(j)
            j=j-1
        if list[j]=='{':
            list= list.pop(j)
            j=j-1
    else:
        continue

f= len(list)
if f ==0:
    print( " balanced ")
else:
    print(" not Balanced ")



