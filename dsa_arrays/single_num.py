def solution(nums):
    arr = [0]*len(nums)
    # if more than a single number missing 
    # missing_list = [] # if more than a single number missing 
    for n in nums:
        arr[n] += 1 

    for i , _ in enumerate(arr):
        if arr[i] == 1:
            return i 
            # missing_list.append(i) # if more than a single number missing 
    # return missing_list # if more than a single number missing 
    
nums = [1]

print(solution(nums))