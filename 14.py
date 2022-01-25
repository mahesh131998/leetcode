

def dog(d, p):
    n= len(d)
    m= len(p)
    k=0
    r=0   
    results="" 
    while k<= n-1 and r <=m-1:
        if d[k]!= p[r]:
            break
        else:
            results= results + p[r]
            k= k+1
            r= r+1
            print(k,r)
    return results

def longestCommonPrefix(self, strs):
    strs.sort()
    print(strs)
    n= len(strs)
    result=strs[0]
    for i in range(1,n):
        result= dog(result, strs[i])
        print("i=",i)
    return result
        
        


        



strs = ["flower","flow","flight"]
o=longestCommonPrefix(0, strs)
print(o)