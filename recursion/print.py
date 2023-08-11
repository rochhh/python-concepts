def func(n):

    if n > 0:
        print(n)
        return func(n-1)
    # return 

print(func(3))