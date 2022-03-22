def removeElement(self, nums, val):
    n= len(nums)
    count=0
    for i in range(n):
        if nums[i]!= val:
            nums[count]= nums[i]
            count= count+1
    return count













nums = [0,1,2,2,3,0,4,2]
val = 2
g= removeElement(0, nums, val)
print(g)