**README.md**

# Bank Management System

This project implements a simple Bank Management System in Python. It consists of classes representing clients, different types of accounts (checking and savings), and a bank.

## Usage

To use this system, you can run the `main.py` file. This file creates instances of clients, accounts, and a bank, demonstrating the functionalities of the system.

## Classes

### `Person`

Represents a person with a name and an age.

### `Client`

Inherits from `Person`. Represents a bank client. Each client can have a single account associated with it.

### `Account`

Abstract base class representing a bank account. Contains common properties and methods for both checking and savings accounts.

#### `Checking_account`

Inherits from `Account`. Represents a checking account with additional features such as an extra limit.

#### `Savings_account`

Inherits from `Account`. Represents a savings account.

### `Bank`

Represents a bank, containing lists of clients, accounts, and agency numbers.

## Functionality

- **Deposit**: Allows depositing money into an account.
- **Withdraw**: Allows withdrawing money from an account, with proper handling for overdrafts and extra limits (in checking accounts).
- **Representation**: Provides a human-readable representation of clients, accounts, and the bank itself.

## Example

```python
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
```

## Notes

- This project is a simplified version of a real bank management system and does not cover all possible scenarios or error handling.
- The classes and methods are designed for educational purposes and may require further refinement for production use.
- Feel free to explore and extend the functionalities according to your needs.

