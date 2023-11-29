
class BankAccount:
    def __init__(self,balance,account):
        self.__balance= balance
        self.__account= account
                
    def disply_account(self):
        print(self.__balance)
                      
        
    def deposit(self,dep):
        self.__balance+=dep
        print(self.__balance)
            

    def Withdrawal(self, withd):
        self.__balance-=withd
        print(self.__balance)
        
                          
d1=BankAccount(10,100)
d1.deposit(10)
d1.Withdrawal(10)