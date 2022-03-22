def findMaximumXOR(self, nums):
    n= len(nums)
    maxi=0
    
    for i in range(n):
        j=i+1
        for j in range(n):
            maxi= max(maxi,nums[i]^nums[j])

    return maxi











nums = [3,10,5,25,2,8]
d=   findMaximumXOR(0, nums)
print(d)   