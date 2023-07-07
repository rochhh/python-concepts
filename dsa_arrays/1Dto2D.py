''' Review once again!!!! '''

def solution(arr,row,col):
    n = len(arr)

    if n != row*col:
        return []
    
    ans = []

    for i in range(row):
        ans.append( arr[ i *col : i * col + col ] )
    return ans

arr = [1,2,3,4]

print( solution( arr , 2 , 2 ) )