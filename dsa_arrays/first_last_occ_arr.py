def bin_search(nums,target,left_bias):
    
    start = 0
    end = len(nums)-1
    i = -1

    while start <= end:

        mid = (start+end)//2

        if target > nums[mid]:
            start = mid + 1
        
        if target < nums[mid]:
            end = mid - 1

        if target == nums[mid]:
            i = mid
            if left_bias:
                end = mid - 1
            else:
                start = mid + 1
    return i


def soln(nums,target):
    left = bin_search(nums,target,True)
    right = bin_search(nums,target,False)
    return [left,right]


nums = []
target = 8
print(soln(nums,target))