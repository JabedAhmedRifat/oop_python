class Phone:
    def __init__(self, price, brand):
        print ("inside phone constructor")
        self.price = price
        self.brand = brand


class SmartPhone(Phone):
    pass

s = SmartPhone(2000, "Apple")
print(s.brand)

# concept if class B inherit from class A 
# if there are no constructor on class B --> but when create class B object then class A constructor will be called 

# if ther are no constructor of child class thern parents class constructor will be called 

#-----------------------------------------------------------------

#private member cannot be called 

class Phone:
    def __init__(self, price, brand):
        print ("inside phone constructor")
        self.price = price
        self.__brand = brand


class SmartPhone(Phone):
    pass

s = SmartPhone(2000, "Apple")
print(s.__brand)

# concept : child class cannot call parnets class's hidden member /data 

#-------------------------------------------------------------


class Phone:
    def __init__(self, price, brand):
        print ("inside phone constructor")
        self.price = price
        self.brand = brand

    def buy(self):
        print ("buying phone")


class SmartPhone(Phone):
    

    def buy(self):
        print ("buying smartphone ")


s = SmartPhone(2000, "Apple")

s.buy()

# concept (method overridding) --> concept form polymorphism 
# when child and parents has same method with same name , when call with child object, then child method will be called

