def func(n):

    if n > 0:
        print(n)
        func(n-1)
        print("i will be called after 3 2 1 ..." , n)

    else:
        print("outside the if block and n -> " ,n)
        # n = n + 1 does not execute
    
    return 

print(func(3))