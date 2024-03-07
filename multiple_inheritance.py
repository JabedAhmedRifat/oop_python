#---------------------------MULTIPLE INHERITANCE--------------------------------



class Phone:
    def __init__(self, price, brand):
        print ("inside phone constructor")
        self.price = price
        self.brand = brand

    def buy(self):
        print ("buying phone")

class Product:
    def review(self):
        print("customer review")


class SmartPhone(Phone, Product): # multiple inheritance *******************************
    # here in this class there are no constructor so it will go to Phone first , if in phone class any constructor then it will execute if no then in next class Product's constructor will execute
    pass     

    def buy(self):
        print ("buying smartphone ")


s = SmartPhone(2000, "Apple")

s.buy()
s.review()



#--------------------------MRO Method resulation Order --------------------------------------

class Phone:
    def __init__(self, price, brand):
        print ("inside phone constructor")
        self.price = price
        self.brand = brand

    def buy(self):
        print ("buying phone")

class Product:

    def buy(self):
        print ("product buy method")



class SmartPhone(Product,Phone): # excute will be priority wise this called MRO
    pass     




s = SmartPhone(2000, "Apple")

s.buy()


# which buy method will be execute ?
# in which class name is first will execute that class's method, so here Product class in first queue 
# if Phone class is in first queue then buying phone will be executed

# => product buy method



