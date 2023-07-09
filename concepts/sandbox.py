# # palindrome string check       naman , 5


# s = "naman"


# def palindrome(string,s,e):
    
#     if len(string) == 1:
#         return True
    
#     checker = palindrome(string,s+1 , e-1)

#     if checker == string:
#         return True
#     return False


# print( palindrome(s , 0, len(s)-1 ) )


def palindrome(string):
    # if len(string) == 1:
    #     return True
    s = 0
    e = len(string)-1

    while s <= e:
        if string[s] != string[e]:
            return False
        s +=1
        e -=1
        return True
    

print(palindrome("ab"))


