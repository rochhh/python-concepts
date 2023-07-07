def helper(arr):
    
    nums = [0]* (len(arr)+1)

    for i in arr:
        nums[ i ] += 1
    
    for idx, n in enumerate(nums):
        if n == 0:
            return idx


arr = [0,1,2,3,4,6]

print(helper( arr))

