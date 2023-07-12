def solution(num):
    arr = [ True for i in range(num+1) ]
    
    p = 2 

    while p*p < len(arr):
        # arr[p] = False
        if arr[p] == True:

            for i in range(p*p, len(arr) , p ):
                arr[i] = False
        
        p +=1
    
    return helper(arr)

def helper(arr):
    for i in range(2,len(arr)):
        if arr[i] == True:
            print(i)


num = 30

print(solution(num))
