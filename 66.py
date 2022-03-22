def plusOne(self, digits):
    n= len(digits)
    go= list()
    h=0
    for i in range(n):
        h= h*10 + digits[i]
    
    h= h+1
    print(h)
    
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

digits = [9]
j=plusOne(0, digits)
print(j)
