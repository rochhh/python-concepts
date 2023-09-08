def func(m,n):
    
    # if n == 1 or n == 0:
        # return m
# both are fine edge conditions
    # if n == 0:
        # return 1

    return m * func(m , n-1)


# print(func(2,5))


def optimial(m,n):

    if n == 0 : 
        return 1 
    
    if n % 2 == 0 :
        return optimial(m*m , n/2)
    
    else:
        return m * optimial(m*m , (n-1)/2 )
    

print(optimial(3,4))

# the explanation for this is - eg: 2^9 == 2 * (2^2) * (8) == (2*2) * (9-1/2) , basic maths   