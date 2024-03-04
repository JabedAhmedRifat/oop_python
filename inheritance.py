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

