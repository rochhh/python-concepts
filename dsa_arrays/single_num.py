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


'''
https://leetcode.com/problems/single-number/solutions/3528463/python-code-using-dictionary-explained-with-approach-and-time-complexity/


def soln(nums):
    
    dic = {}
    
    for num in nums:
        if num not in dic:
            dic[num] = True
        
        else:
            dic[num] = False
        
    for key , value in dic.items():
        if value == True:
            return key
    
nums= [2]

print(soln(nums))

'''