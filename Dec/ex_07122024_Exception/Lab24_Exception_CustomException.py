
# Custom exception

# class LowBalanceExceptionCustom(Exception):
#     def __init__(self, message):
#         self.message= message
#         super().__init__(message)
#
# balance= 1000
# withdraw= int(input("Enter the  amount yo want to withdraw\n"))
# if withdraw > balance:
#     raise LowBalanceExceptionCustom("Balance is low ")
# else:
#     print("Remaining balance is:",(balance-withdraw))

#practice
class LowBalanceCustomException(Exception):
    def __init__(self, message):
        self.message= message
        super().__init__(message)

balance= 1000
withdraw= int(input("Enter the withdraw balance\n"))
if withdraw > balance:
    raise LowBalanceCustomException("Balance is low")
else:
    print("Remaining balance is:-",balance-withdraw)
