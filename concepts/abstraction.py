from abc import ABC , abstractmethod

class BankApp(ABC):

    def transaction(self):
        return "done"
    
    @abstractmethod
    def abs_method(self):
        return "in abs method"

class MobileApp(BankApp):
 
 def idk(self):
    return "idk"

obj = MobileApp()

print ( obj.idk() )