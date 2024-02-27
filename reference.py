class Customer:
    def __init__(self, name):
        self.name = name


cust = Customer('Jabed')
print(cust.name)


def greet(customer):
    print("hello", customer.name)


greet(cust)

