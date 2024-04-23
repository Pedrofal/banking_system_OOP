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



   
