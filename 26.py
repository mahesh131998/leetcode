

def removeDuplicates(self, nums):
    n= len(nums)
    print(n)
    k=n
    count=0

    for i in range(n):
        for j in range(i+1,n):
            if nums[i]== nums[j]:
                count= count+1
                print("count=",count)
                print("nums i=",nums[i])
                print("nums j=",nums[j])
            # else:
            #     s= i+1
            #     p=j
            #     print("s =",s)
            #     print("p =",p)
            #     while p!=k:
            #         nums[s] = nums[p]
            #         s= s+1
            #         p=p+1
                
            #     k=k-count
            #     count=0

    return nums

nums = [0,0,1,1,1,2,2,3,3,3,4]
g=removeDuplicates(0,nums)
# print(g)
