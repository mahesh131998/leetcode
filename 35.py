def search(start, end,nums, target):
        avg= int((start+end)/2)
        if (end== start) and nums[avg]!= target:
            avg =avg+1
            print(avg)
            return avg
        elif nums[avg]== target:
            print(avg)
            return avg
        elif nums[avg]< target :
            search(avg+1, end, nums, target)
        elif nums[avg]> target:
            search(start, avg-1, nums, target)


def searchInsert(self, nums, target):
    n= len(nums)
    start=0
    end= n
    # def search(start, end,nums, target):
    #     avg= int((start+end)/2)
    #     if (end== start) and nums[avg]!= target:
    #         avg =avg+1
    #         return avg
    #     elif nums[avg]== target:
    #         print(avg)
    #         return avg
    #     elif nums[avg]< target :
    #         search(avg+1, end, nums, target)
    #     elif nums[avg]> target:
    #         search(start, avg-1, nums, target)
        



    d=search( start, end,nums, target)
    print(d)
    return d
            







nums = [1,3,5,6,7,10,12]
target = 2
p=searchInsert(0, nums, target)
print(p)
