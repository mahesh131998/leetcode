def addStrings(self, num1, num2):
    n1= len(num1)
    n2= len(num2)
    h1=0
    h2=0
    for i in range(n1):
        h1= h1*10 + int(num1[i])
    for i in range(n2):
        h2= h2*10 + int(num2[i])

    su= str(h1+h2)
    return su










num1 = "11"
num2 = "123"
h=addStrings(0, num1, num2)
print(h)