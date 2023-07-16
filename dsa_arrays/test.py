'''
To do -
twosum
missingNo
moveZeroes


Successful - 
contains Duplicate 
rev arr 
anagram 
max , min no in an array 
chocolate distribution 


'''


def solution(nums):
    i = 0
    j = 1

    while j < len(nums):

        if nums[i] == 0:
            nums[i] , nums[j] = nums[j] , nums[i]
            i+=1
            j+=1
            if j >= len(nums):
                return nums
        
        if nums[i] == 0 and nums[j] == 0:
            j+=1
        
        if nums[j] == 0:
            nums[i] , nums[j] = nums[j] , nums[i]
            i+=1
        else:
            i+=1
            j+=1
    return nums 

nums = [1,0] 


print(solution(nums))