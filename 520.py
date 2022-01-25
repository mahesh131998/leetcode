def detectCapitalUse(self, word):
    n= len(word)
    match1= True
    match2= True
    match3= True
    for i in range(n):
        if not word[i].isupper():
            match1= False
            break

    
    for i in range(n):
        if not word[i].islower():
        # if word[i].isupper():
            match2=False
            break
        

    if not word[0].isupper() :
        match3=False
    if match3:
        for i in range (1,n):
            if  word[i].isupper() :
                match3= False
                break
            
    
    
    if match1:
        return True
    if match2:
        return True
    if match3:
        return True
    
    return False




word ="Leetcode"
d= detectCapitalUse(0, word)
print(d)