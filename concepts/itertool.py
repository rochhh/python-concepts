from itertools import permutations , accumulate
import operator

ls = [1,2,3,8,6,7,5]

# p = permutations(ls)

# print(list(p))

acc = accumulate(ls , func=max)

print(list(acc)) # 1,3,6
print(list(acc)) # [1, 2, 3, 8, 8, 8, 8] for func=max


