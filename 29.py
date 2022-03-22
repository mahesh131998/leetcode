def divide(self, dividend, divisor):
    i=1
    count=0
    if divisor and dividend<0:
        divisor= divisor*-1
        dividend= dividend*-1
        count=0
    if divisor <0:
        divisor= divisor*-1
        count=1
    if  dividend <0:
        dividend= dividend*-1
        count=1
    if (-2**31) >= dividend and divisor >= (2**31) - 1:
        return 0
    
    if divisor==0:
        return 0
    
    while True:
            
        m= i * divisor
        if m > dividend:
            break
        else:
            i=i+1
    
    i=i-1
    if count==1:
        return -i
    else:
        return i


        











dividend = -2147483648

divisor = -1
f=divide(0, dividend, divisor)
print(f)