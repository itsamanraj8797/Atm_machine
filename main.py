import sys


class Atm:
    def __init__(self):
        self.pin = ''
        self.balance = 11000

        self.menu()

    def menu(self):
        print('Welcome to Python Bank !!')
        print("""
        Enter option number:
                1. Enter 1 to create pin
                2. Enter 2 to deposit
                3. Enter 3 to withdraw
                4. Enter 4 to check Balance
                5. Enter 5 to Exit """)
        option = input()
        if option == '1':
            print('You chose to create pin : ')
            self.create_pin()

        elif option == '2':
            print('You chose to deposit Money  : ')
            self.deposit()

        elif option == '3':
            print('You chose to withdraw Money  : ')
            self.withdraw()

        elif option == '4':
            print('You chose to Check ur account balance  : ')
            self.checkbalance()

        elif option == '5':
            print('You chose to Exit option : ')
            self.exitbank()

    def create_pin(self):
        self.pin = input("Enter New Pin: ")
        print("Process Completed")
        self.menu()

    def deposit(self):
        temp_pin = input('Enter pin = ')
        if temp_pin == self.pin:
            print('Correct Pin')
            amount = int(input('Enter the Amount to be deposit : '))
            self.balance += amount
            print('Amount Added --> Done !!')
            self.menu()
        else:
            print('Invalid pin !! Try again ')
            self.menu()

    def withdraw(self):
        temp_pin = input('Enter pin = ')
        if temp_pin == self.pin:
            print('Correct Pin')
            print(f'Your available balance in the Account : {self.balance}')
            amount = int(input('Enter the Amount to be withdrawn : '))
            if amount <= self.balance:
                self.balance -= amount
                print('Amount Deducted : --> Collect your Money and Card ')
                self.menu()
            else:
                print('Insufficient Balance !! Try again')
                self.menu()
        else:
            print('Invalid Pin ')
            self.menu()

    def checkbalance(self):
        temp_pin = input('Enter pin = ')
        if temp_pin == self.pin:
            print('Correct Pin')
            print(f'Your available balance in the Account : {self.balance}')
            choice = input("Do you want to withdraw : [Y/N] : ")
            if choice == 'Y':
                self.withdraw()
            else:
                print('OK !! Thank you ')
            self.menu()
        else:
            print('Invalid Pin !! Try again ')
            self.menu()

    @staticmethod
    def exitbank():
        print('Thank you for your Service !!')
        sys.exit(0)


customer1 = Atm()

customer1.menu()
