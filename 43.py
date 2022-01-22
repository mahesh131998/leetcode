def multiply(self, num1, num2):
    list1=list()
    list2=list()
    num3=0
    carry=0
    f=""
    if len(num1)< len(num2):
        temp= num1
        num1=num2
        num2= temp
    if 1> len(num1) and len(num2)>200:
        return 0
    if len(num1) and len(num2)>=2:
        if num1[0]=="0" or num2[0]=="0":
            return 0
    if num1=="0" or num2=="0":
        return 0
    if len(num1) and len(num2)==1:
        sig= int(num1)* int(num2)
        return str(sig)
    else:
        for char in num1:
            if char.isdigit():
                continue
            else:
                return 0
        for char in num2:
            if char.isdigit():
                continue
            else:
                return 0

        for char in num1:
            list1.append(int(char))
        for char in num2:
            num= int(char)
            num3= num3*10 + num
        j= len(list1)-1
        while j>=0:
            if j== len(list1)-1:
                s= list1[j]
                mul= s* num3
                rem= mul%10
                list2.append(rem)
                carry=int(mul/10) 
                j= j-1
            
            if j==0:
                s= list1[j]
                mul= s* num3
                last= mul + carry
                list2.append(last)
                j=j-1
            else:
                s= list1[j]
                mul= s* num3
                mul= mul +carry
                rem= mul%10
                list2.append(rem)
                carry=int(mul/10) 
                j= j-1

    for k in list2:
        f=  str(k) +f
    return f




b=multiply(any,"80","75")

print(b)
    