import account
import client


class Bank:
    def __init__(
        self,
        agency: list[int] | None = None,
        clients: list[client.Client] | None = None,
        accounts: list[account.Account] | None = None,
    ):
        self.agency = agency or []
        self.clients = clients or []
        self.accounts = accounts or []

  

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agency!r}, {self.clients!r}, {self.accounts!r})'
        return f'{class_name}{attrs}'

if __name__ == '__main__':
    c1 = client.Client('Luiz', 30)
    cc1 = account.Checking_account(111, 1000)
    c1.account = cc1
    c2 = client.Client('Maria', 18)
    cp1 = account.Savings_account(112, 100)
    c2.account = cp1
    bank = Bank()
    bank.clients.extend([c1, c2])
    bank.accounts.extend([cc1, cp1])
    bank.agency.extend([111, 222])

    print(bank)

   
