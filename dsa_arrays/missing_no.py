def helper(arr):
    
    nums = [0]* (len(arr)+1)

    for i in arr:
        nums[ i ] += 1
    
    for idx, n in enumerate(nums):
        if n == 0:
            return idx


arr = [0,1,2,3,4,6]

# print(helper( arr))


def sol2(arr):
    len_n = len(arr)
    res = len_n

    for i in range(len_n):
        res = res + i - arr[i]
    return res

print(sol2( arr))


def sol3(arr):

    n = len(arr)

    total = ( n * (n-1) ) // 2

    for i in arr:

        total = total - i

    return total