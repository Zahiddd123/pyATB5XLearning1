# In Encapsulation we can access private instance variable or private func
# outside the class only using a public function.

#
class Bank:

    def __init__(self, account_number, balance):
        self.balance = balance #public instance variable
        self.__account_number=account_number #private instance variable

    def check_balance(self):
        print("Current balance of my account -> ",self.balance)


    def deposit(self, amount):
        self.balance= self.balance+amount
        print("deosited amount ",amount)

    def show_me_account_number(self, is_auth): # Use this method to access the
             if is_auth == True:               # private instnace variable out of the class
                print(self.__account_number)
             else:
                 print("Not allowed")

PNB= Bank(2121121212121, 200)
PNB.deposit(300)
PNB.check_balance()
# print(PNB.__account_number) # cannot access the private
                            # instance variable outside the class directly

PNB.show_me_account_number(False)

