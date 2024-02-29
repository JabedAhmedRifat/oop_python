class Customer:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender 


cust = Customer('Jabed', 'male')


def greet(customer):
    if customer.gender == 'male':
        print("hello", customer.name, "sir")
    else:
        print("hello", customer.name, "Ma'am")

    cust2 = Customer('Rijbi', 'Female')
    return cust2

new = greet(cust)
print(new.name)
