class DiffDeviceException(Exception):
    def _init_(self , message ):
        self.msg = message
        self.logoutfunc = Google.logout(self)

    def helper_func(self):
        return f" DIff devException -> {self.msg} "

class Google:

    def _init_(self,email_id,device):
        self.email = email_id
        self.device = device


    def login(self , device ):

        if device != self.device: 
            raise DiffDeviceException (f"The device is not the device you logged in from before which was --> {self.device} <-- and now you're logging in from --> {device} <-- ")
        
        return f" {self.email} logged in successfully "


    def logout(self):
        return "logged out this is the Google logout method "




# class DiffDeviceException(Exception , Google ):
#     def _init_(self , message  ):
#         self.msg = message
#         self.logoutfunc = Google.logout(self)

#     def helper_func(self):
#         # print(self.logoutfunc)
#         return f" DIff devException -> {self.msg} "


try:
    obj = Google("abc@gmail.com" , "windows" )
    obj.login("androif")


except DiffDeviceException as dde :
    print(dde.helper_func())
    print(dde.logoutfunc)

# finally:
#     print("finally block")