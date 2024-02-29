class Customer:

    def __init__(self, name, age):
        self.name = name 
        self.age = age

    def intro(self):
        print("I am", self.name, "And I am", self.age)


c1 = Customer("Jabed" , 23)
c2 = Customer("Ahmed" , 22)
c3 = Customer("Rifat" , 26)

L = [c1,c2,c3]

for i in L:
    print("my name is " , i.name, "And age is", i.age)

for i in L:
    i.intro()