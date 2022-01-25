#brut force
def maxArea1(self, height):
    n= len(height)
    maxi=0
    if 2 > n > 10**5:
        return 0
    
    for i in range(n):
        j=i+1
        if 0 > height[i] > 10**4:
            return 0
        for j in range(n):
            maxi= max(maxi, min(height[i], height[j]) * (j-i))
    return maxi

#divide and conqure
def maxArea(self, height):
    l=0
    r= len(height)-1
    maxi=0
    while l<r :
        maxi= max(maxi, min(height[l], height[r]) * (r-l))
    
        if height[l]<height[r]:
            l= l+1
        else:
            r=r-1
    
    return maxi




height = [4,2,0,3,2,5]
p= maxArea(0, height)
print(p)