import pickle

class Person:

    def _init_(self , name , age):
        self.name =name
        self.age = age

    def fu(self):
        return "ahhahahah"

p = Person("roch" , 22)


def helper_fun(obj):

    ''' Helpful for JSON !pickle  '''

    if isinstance(obj , Person):
        return f"the name is {obj.name} and age is {obj.age} " 


# with open ("C:/Users/Rochishnu Paliwal/Documents/pythong/ds/tf/person.pkl" , "wb") as f:

#     pickle.dump(p , f )

with open ("C:/Users/Rochishnu Paliwal/Documents/pythong/ds/tf/person.pkl" , "rb") as f:


    msg = pickle.load( f )
     
print( msg.fu() )

# test commit