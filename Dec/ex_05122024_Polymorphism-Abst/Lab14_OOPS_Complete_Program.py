from abc import  ABC, abstractmethod


class BankAccount:

    def __init__(self, balance, account_number):
        self.__balance= balance
        self.account_number= account_number

    def show_me_balance(self):
        print(self.__balance)

class ICICBank(BankAccount):

    def withdraw(self):
        print("Yes")

    @abstractmethod
    def loan(self):
        pass

    @staticmethod
    def call_customer_care():
        print("call customer care on 101 ")

class CustomerAccountDetail(ICICBank):

    def loan(self):
        print("1 lakh of loan is taken")
        ICICBank.call_customer_care()
        BankAccount.show_me_balance(self)






obj_ICIC= CustomerAccountDetail(1110,11111111111)
obj_ICIC.loan()



