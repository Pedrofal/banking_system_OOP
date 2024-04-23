import person
import client
import account
from bank import Bank

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