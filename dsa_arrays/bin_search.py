def solution(nums,target):
    
    low = 0
    high = len(nums)-1
    mid = (high+low)//2

    while low < high:

        if target > nums[mid]:
            low = mid + 1
            mid = (high+low)//2
        
        if target < nums[mid]:
            high = mid - 1
            mid = (high+low)//2

        if target == nums[mid]:
            return mid
    return -1


nums = [1,2,3,4,5,6,7,8,9]
target = 2

print(solution(nums,target))