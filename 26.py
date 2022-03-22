

def removeDuplicates(self, nums):
    n= len(nums)
    i=1
    j=0
    if 0 >= len(nums) >= 3*(10**4):
        return 0
    if n==0:
        return 0
    while j != n-1:
        if nums[j]!=nums[j+1]:
            nums[i]=nums[j+1]
            i=i+1
            
        j=j+1
    print(nums)
    print(i)

    return i,nums

nums =[]
g=removeDuplicates(0,nums)
print(g)
