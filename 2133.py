from itertools import count


def checkValid(self, matrix):
    row= len(matrix)
    coloumn=len(matrix[0])
    countrow=[-1]*row
    countcoloumn=[-1]*coloumn
    counter=0
    for i in range(row):
        for j in range(coloumn):
            p=matrix[i][j]
            p=p-1
            if countrow[p]==-1:
                countrow[p]=p
            else:
                counter=1
        countrow=[-1]*row
    
    if counter ==1:
        return False
    
    for i in range(coloumn):
        for j in range(row):
            p=matrix[j][i]
            p=p-1
            if countcoloumn[p]==-1:
                countcoloumn[p]=p
            else:
                counter=1
        countcoloumn=[-1]*coloumn
    
    if counter ==1:
        return False 
    else:
        return True      



matrix = [[1,2,3],[3,1,2],[2,3,1]]
boo=checkValid(0, matrix)
print(boo)