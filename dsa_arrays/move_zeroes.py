def solution(nums):
    slow = 0

    for fast in range(len(nums)):
        if nums[fast] != 0:
            nums[slow] , nums[fast] = nums[fast] , nums[slow]
            slow += 1
    print(nums)

arr = [0,1,0,3,12,0,24,0,0,2]

print(solution(arr))