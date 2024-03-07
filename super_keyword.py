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
        super().buy()


s = SmartPhone(20000, "Apple", 13)

s.buy()