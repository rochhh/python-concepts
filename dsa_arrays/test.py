'''
To do -
twosum
missingNo

Successful - 
contains Duplicate 
rev arr 
anagram 
max , min no in an array 

'''


def solution(nums):

    ''' best time to sell stock '''
    
    buy = 0
    sell = 1
    curr = 0 
    fin = 0

    while sell < len(nums):
        curr = nums[sell] - nums[buy]

        if nums[buy] > nums[sell]:
            buy = sell
            # sell += 1
        
        fin = max(fin,curr)
        sell += 1

    return fin 

# nums = [7,1,5,3,6,4] # ans -> 5 [ buy 1 , sell 6 ]     
nums = [2,1,4]

print(solution(nums))