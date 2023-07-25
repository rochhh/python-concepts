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



''' 

other solutions - 


def soln(nums):
    
    buy = 0
    sell = 1
    curr_profit = 0
    max_profit = -1000

    while sell < len(nums):

        curr_profit = nums[sell] - nums[buy]
        max_profit = max(max_profit , curr_profit)

        if curr_profit < 0 :
            max_profit = 0
            buy +=1
            sell +=1
        else:
            sell +=1
    
    return max_profit


nums = [7,1,5,3,6,4]
print(soln(nums))


# ####### # 

    buy = 0
    sell = 1
    max_profit = 0

    while sell < len(prices):
        curr_profit = prices[sell] - prices[buy]

        if prices[sell] > prices[buy]:
            max_profit = max(max_profit , curr_profit )
        else:
            buy = sell 
        sell += 1

    return max_profit






'''