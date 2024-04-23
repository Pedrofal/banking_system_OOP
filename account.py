from abc import ABC, abstractmethod
import random

class Account(ABC):
    def __init__(self, agency: int, balance: float):
        self.agency = agency
        self.number = self.account_number()  
        self.balance = balance

    def account_number(self) -> int:
        return random.randint(100, 999)  

    def deposit(self, deposit_value: float) -> float:
        self.balance += deposit_value
        print(f'\nYou just deposit ${round(deposit_value, 3)} in your account,\n your new balance is ${round(self.balance, 3)}\n')
        return self.balance

    @abstractmethod
    def withdraw(self,  withdraw_value:float) -> float:
        pass
       
class Savings_account(Account):
    def withdraw(self, withdraw_value:float) -> float:
        if self.balance > withdraw_value:
            self.balance -=  withdraw_value
            print(f'\nYou just withdraw ${round(withdraw_value, 3)} from your account,\nYour new balance is ${round(self.balance, 3)}\n')
            return self.balance
        else:
            print(f'\nYour balance is insufficient to withdraw ${round(withdraw_value, 3)}.\nCurrent balance: ${round(self.balance, 3)}\n')
            return self.balance

    def __repr__(self):
        return f"Savings Account - Agency: {self.agency}, Account Number: {self.number}, Balance: ${round(self.balance, 3)}"

class Checking_account(Account):
    def __init__(self, agency:int,balance:float):
        super().__init__(agency,balance)
        self._extra_limit = 200
        self._total_balance = self.balance + self.extra_limit
        self.extra_limit_used = 0
        
    @property
    def extra_limit(self):
        return self._extra_limit
    
    @extra_limit.setter
    def extra_limit(self, extra_limit: float):
        self._extra_limit += extra_limit
    
    def withdraw(self, withdraw_value: float) -> float:
            self.extra_limit_used = 0
            
            if self.balance > withdraw_value:
                self.balance -=  withdraw_value
                self._total_balance -= withdraw_value
                print(f'\nYou just withdraw ${round(withdraw_value, 3)} from your account,\nYour new balance is ${round(self.balance, 3)}\n')
                return self._total_balance
            elif self._total_balance < withdraw_value :
                print(f'\nYour balance is insufficient.\nCurrent balance: {round(self.balance, 3)}\nExtra limit: ${round(self.extra_limit, 3)}\n')

                self.extra_limit_used = min(withdraw_value - self.balance, self._total_balance)
                self.balance -= (withdraw_value - self.extra_limit_used)
                self._total_balance -= withdraw_value
                return self._total_balance
               
            else:
                self.extra_limit_used = withdraw_value - self.balance
                self.balance -= (withdraw_value - self.extra_limit_used)
                self._total_balance -= withdraw_value
                print(f'\nYou just withdraw ${round(withdraw_value,3)} from your account.\nYou used ${round(self.extra_limit_used,3)} from your extra limit.\nYour new balance is ${round((self.balance - self.extra_limit_used), 3)}\nYour remaning extra limit is ${round((self._extra_limit - self.extra_limit_used),3)}\n')
                return self._total_balance
    
    def __repr__(self):
        return f"Checking Account - Agency: {self.agency}, Account Number: {self.number}, Balance: ${round((self.balance - self.extra_limit_used), 3)}, Extra Limit: ${round((self._extra_limit - self.extra_limit_used),3)}"    
            
            
       
                


               

   


