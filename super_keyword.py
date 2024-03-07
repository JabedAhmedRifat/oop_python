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


#----------------------------------------------------------------------------------------------

# here common attributes using parent's constructor 
# and uncommon attributes using child's constructor

class Phone:

    def __init__(self, price,brand):
        print("inside phone constructor")
        self.__price = price
        self.brand = brand 

    


class SmartPhone(Phone):

    def __init__(self, price, brand, os, ram):
        print("first come here")
        super().__init__(price, brand) # this price and brand pass to parent's constructor
        self.os = os
        self.ram = ram 
        print ("inside smart phone constructor")



s = SmartPhone(20000, "Apple", "Android", 2)

print(s.os)
print(s.brand)

# =>first come here
# =>inside phone constructor
# =>inside smart phone constructor
# =>Andriod
# => Apple

#-----------------------------------------------------------------------------------------------


class Parent:

    def __init__(self, num):
        self.__num = num

    def get_num(self):
        return self.__num
    
class Child(Parent):

    def __init__(self, num, val):
        super().__init__(num)

        self.__val = val 

    
    
    def get_val(self):
        return self.__val


son = Child(100,200)

print("parent: num:" , son.get_num()) 
print("child: num:" , son.get_val())

# => 100
# => 200



#--------------------------------------------------------------------------------------------------

#obj can call parent attribute 

class Parent:

    def __init__(self, num):
        self.num = 100

 
class Child(Parent):

    def __init__(self):
        super().__init__()
        self.var = 200
    
    def show(self):
        print(self.num) # self is nothing but son which is obj of Child
        print(self.var)


son = Child()
son.show()

# => 100
# => 200