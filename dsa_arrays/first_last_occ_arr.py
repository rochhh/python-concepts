def soln(nums,target):
    
    start = 0
    end = len(nums)-1
    
    smallest = 0
    largest = 0
    
    while start < end:

        mid = (start+end)//2

        if target == nums[mid] and smallest == 0:
            smallest = mid

        if target == nums[mid] and largest == 0:
            largest = mid 
        
        if target > nums[mid]:
            start = mid + 1

            if nums[start] == target:
                smallest = start

        if target < nums[mid]:
            end = mid - 1

            if nums[end] == target:
                largest = end

    return [-1,-1]


nums = [5,7,7,8,8,10]
target = 8
print(soln(nums,target))