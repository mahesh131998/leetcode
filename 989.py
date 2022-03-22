def addToArrayForm(self, num, k):
    n= len(num)
    h=0
    go= list()
    for i in range(n):
        h= h*10 + num[i]
    
    h= h+ k
    while True:
        if h%10==0:
            go.append(0)
            h= int(h/10) 
        else:
            if 0<= h<=9:
                go.append(h)
                break
            else:
                b= h%10
                go.append(b)
                h= int(h/10)
    
    go.reverse()
    return go










num = [2,7,4]
k = 181
h= addToArrayForm(0, num, k)
print(h)