#--------------------------Polymorphism-----------------------------------
# ------------------------means multiple phases------------------------------


#------------------------------- overriding ------------------------
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

# concept (method overriding) --> concept form polymorphism 
# when child and parents has same method with same name , when call with child object, then child method will be called
#not the parent's method, that called overriding 



#----------------------------------Over loading-------------------------------------------------
# if giving different variables to same method , will behave differently for different solutions thats called overloading 
# Techically there is nothing overloading in python
# but using logic can use overloading 

class Geometric:

    def area(self,a, b=0):
        if b == 0:
            print("Circle area", ":", 3.14 * a * a)

        else:

            print ("Rectangle area", ":", a * b)


obj = Geometric()
obj.area(4)
obj.area(4,5)


#--------------------------------operator overloading---------------------------------------


# when changing operator's default behaviour to another behaviour it will called operator overloading, can use magic method to do that 

