# do again ! 

def solution(nums):
    buy = 0
    sell = 1
    fin = 0

    while sell < len(nums):
        
        curr = nums[sell] - nums[buy]
        
        if nums[buy] < nums[sell]:
            fin = max( curr , fin )
            sell += 1
        else:
            buy = sell
            sell += 1
    return fin 
        



arr = [7,1,5,3,6,4]


print(solution(arr))
