from person import Person
import account 

class Client(Person):
    def __init__(self, name: str, age:int):
        super().__init__(name, age)
        self.account: account.Account | None = None

    def __repr__(self):
        return f'Name: {self.name}, Age: {self.age}'
    
    

if __name__ == '__main__':
    c1 = Client('Pedro', 34)
    c1.account = account.Checking_account(123,100)
    c1.account.withdraw(110)
    print(vars(c1))

    c2 = Client('Maria', 28)
    c2.account = account.Savings_account(321,200)
    c2.account.deposit(19.20)
    print(vars(c2))
 

    
