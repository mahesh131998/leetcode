def isValid(self, s):
    n= len(s)
    stack= list()
    for i in range(n):
        if not stack:
            if s[i]==')'or s[i]=='}' or s[i]==']':
                return False

        if s[i]=='('or s[i]=='{' or s[i]=='[':
            stack.append(s[i])
            
        
        if s[i] ==')':
            if stack[-1]=='(':
                stack.pop()
            else :
                return False
                
                

        if s[i] =='}':
            if stack[-1]=='{':
                stack.pop()
            else :
                return False
                
        
        if s[i] ==']':
            if stack[-1]=='[':
                stack.pop() 
            else :
                return False
                
    print(stack)
    if not stack:
        return True
    else:
        return False

        









s= "(])"
f= isValid(0,s)
print(f)
