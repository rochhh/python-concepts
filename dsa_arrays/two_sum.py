arr = [2,1,5,3]
target = 4

def two_sum(arr ,target):
    
    hashmap = {} # {k,v} pair in the hashmap will be in the { value , index  } format

    for i , n in enumerate(arr):

        diff = target - n 

        if diff in hashmap:
            return [ hashmap[diff] , i ]
        hashmap[n] = i  
    
print( two_sum(arr, target) )


'''

Done again ! 


def soln(nums,target):
    
    hashmap = {}

    for i in range(len(nums)):

        diff = target - nums[i]

        if target - diff in hashmap:
            return [hashmap[target - diff] , i]
        else:
            hashmap[diff] = i
    
    return [-1,-1]


nums= [3,3]
target = 6
print(soln(nums,target))


'''