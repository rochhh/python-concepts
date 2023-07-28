def soln(nums,target):
    
    start=0
    end = len(nums)-1

    while start <= end:
        mid = (start+end)//2

        if target == nums[mid]:
            return mid 
        
        if nums[mid] >= nums[start] and target < nums[end]:
            if nums[start] == target:
                return start
            start = mid + 1
            

        if nums[mid] >= nums[start] and target > nums[start]:
            if nums[end] == target:
                return end
            end = mid - 1

        else:
            return -1

        

nums = [4,5,6,7,0,1,2]
target = 0

print(soln(nums,target))