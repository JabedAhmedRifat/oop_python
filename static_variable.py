class Atm:

    #static/ class variable
    __counter = 1


    def __init__(self):
        self.pin = ''
        self.balance = 0
        self.sno = Atm.__counter
        Atm.__counter = Atm.__counter + 1

        self.menu()


    @staticmethod
    def get_counter():
        return Atm.__counter
    

    @staticmethod
    def set_counter(new):
        if type(new) == int:
            Atm.__counter = new
        else:
            print("not method")

    
    def menu(self):
        user_input = input("""
            1. Create a new pin
            2. Deposit
            3. withdraw
            4. check balance
            5.exit              
        """)
        
    
        if user_input == '1':
            self.create_pin()
        elif user_input == '2':
            self.deposit()
        elif user_input == '3':
            self.withdraw()
        elif user_input == '4':
            self.check_balance()
        else:
            print('Exit')

    
    def create_pin(self):
        self.pin = input("Create Pin")
        print("pin successfully created")
        self.menu()

    
    def deposit(self):
        temp_pin = input("Enter your pin")
        if temp_pin == self.pin:
            amount = int(input("Amount to deposit"))
            self.balance = self.balance + amount 
            print("amount deposit successfully")
            self.menu()
        else:
            print("invalid pin")

    def withdraw(self):
        temp_pin = input("enter your pin")

        if temp_pin == self.pin:
            amount = int(input("Amount to withdraw"))
            if amount < self.balance:
                self.balance = self.balance - amount 
                print ("amount withdraw successfully")
                self.menu()
            else:
                print("insufficient balance")

        else:
            print("invvalid pin")


    
    def check_balance(self):
        temp = input("Enter your pin")
        if temp == self.pin:
            print(self.balance)
            self.menu()
        else:
            print("invalid pin")
    
    
