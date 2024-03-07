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

#--------------------------Polymorphism-----------------------------------


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

# => Inside phone constructor
# => Buying a smartphone 

# concept (method overridding) --> concept form polymorphism 
# when child and parents has same method with same name , when call with child object, then child method will be called

#-----------------------------------------------------------------------------------


class Parent:

    def __init__(self, num):
        self.__num = num

    def get_num(self):
        return self.__num
    
class Child(Parent):
    
    def show(self):
        print("this is child class")


son = Child(100)
print(son.get_num())
son.show()

# => 100
# => this is child class 


#-----------------------------------------------------------------


class Parent:

    def __init__(self, num):
        self.__num = num

    def get_num(self):
        return self.__num
    
class Child(Parent):

    def __init__(self, val, num):
        self.__val = val 

    
    
    def get_val(self):
        return self.__val


son = Child(100,1)

print("parent: num:" , son.get_num()) # got error cause , when child constructor got triggered , parent's constructor wont triggered because child already has constructor
print("child: num:" , son.get_val())


#--------------------------------------------------------

class A:

    def __init__(self):
        self.var1 = 100

    def display(self, var1):
        print("class A:", self.var1)

class B:

    def display2(self, var1):
        print("class B:", self.var1)
        
obj = B()
obj.display1(200)

# => class A: 100 # cause print("class A:", self.var1) this is not in use or replaced 




