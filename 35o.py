def searchInsert(self, nums, target):
    n= len(nums)
    for i in range(n):
        if nums[i]== target:
            return i
        if nums[i]> target:
            return i
        if i== n-1 and nums[n-1]< target:
            return i+1



nums = [1,3,5,6]
target = 7
f=searchInsert(0, nums, target)
print(f)
