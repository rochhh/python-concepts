def func(n):
    
    if n > 0 :

        return n + func(n-1)
    if n == 0:
        return 0


print(func(5))