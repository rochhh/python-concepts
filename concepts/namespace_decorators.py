''' 
this will break as LEGB rule the 
the built-in print func get overridden and hence the error 
'''

# def print():
#     return "oog"

# print("hello")

''' print result: inner -> outer -> main '''

def outer():

    def inner():          
        return "inner function -> local scope"
            
    print(inner())

    return "outer function -> enclosing scope"
    
print(outer())

print('main program -> global scope')

# outer() -> inner() -> _ifls_ -> 11 -> _ofgs_ -> main

#  just like global we have nonlocal (for enclosed n inner func just like a func and global )

l = [1,2,3]
print( "max is the value ->" , max(l)) # prints fine 

def max():
    print("salut")

print(max(l)) # throws err