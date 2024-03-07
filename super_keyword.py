#-----------------using Super() keyword to involve parent's methods and constructors---------------------- 
# using super only can access parent's methods and constructors
# can not access parent's attributes or data or variables 

class Phone:

    def __init__(self, price,brand):
        print("inside phone constructor")
        self.__price = price
        self.brand = brand 

    def buy(self):
        print("Buying a phone")


class SmartPhone(Phone):

    def buy(self):
        print("Buying a smart phone")
        super().buy() #calling parent's method using super 


s = SmartPhone(20000, "Apple", 13)

s.buy()

# s.super().buy() # can not call super outside of a child class


# => Buying a smart phone
# => Buying a phone

