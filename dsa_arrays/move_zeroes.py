def solution(nums):
    slow = 0

    for fast in range(len(nums)):
        if nums[fast] != 0:
            nums[slow] , nums[fast] = nums[fast] , nums[slow]
            slow += 1
    print(nums)

arr = [0,1,0,3,12,0,24,0,0,2]

print(solution(arr))



def another(nums : list[int]):
    i=0
    while i<len(nums):
        if nums[i] == 0:
            nums.append(0)
            nums.remove(0)
        i+=1
    return nums

print(another(arr))