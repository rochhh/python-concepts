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