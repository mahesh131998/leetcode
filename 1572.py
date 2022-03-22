def diagonalSum(self, mat):
    row= len(mat)
    coloumn= len(mat[0])
    i=0
    sum=0
    k=0
    j=0
    l= coloumn-1
    while(i <= row-1 and j<=coloumn-1 and k <=row-1 and l>= 0):
        if i == k and j ==l:
            sum= sum + mat[i][j]
        else:
            sum= sum + mat[i][j] + mat[k][l]  

        i= i+1
        j=j+1
        k=k+1
        l=l-1
    return sum


mat = [[1,2,3],[4,5,6],[7,8,9]]
g=diagonalSum(0, mat)
print(g)