def factorial(n):

    if n == 0 :
        return 1
    
    return n * factorial(n-1)


def ncr(n , r):

    if r == 0 or n == r :
        return 1
    
    # numerator = factorial(n)
    # denominator = factorial(r) * factorial(n-r)

    return ncr(n-1 , r-1) + ncr(n-1 , r) # pascals triangle logic 

    # return numerator/denominator


print(ncr(5,3))