def validMountainArray(self, arr):
    n= len(arr)
    j= n-1
    i=0
    while i != j:
        if arr[i]< arr[i+1]:
            i=i+1
        else:
            return False
        
        







arr = [0,3,2,1]
d=validMountainArray(0, arr)
print(d)