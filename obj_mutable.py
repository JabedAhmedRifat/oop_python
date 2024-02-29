class Customer:
    def __init__(self, name):
        self.name = name


def greet(customer):
    print(id(customer))
    customer.name = "Ahmed"
    print(customer.name)
    print(id(customer))


cust = Customer("Jabed")
print(id(cust))

greet(cust)
print(cust.name)