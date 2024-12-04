class BankAccount:
    def __init__(self, account_holder):
        """
        Initialize the bank account with the account holder's name and a zero balance.
        """
        self.account_holder = account_holder
        self.balance = 0.0

    def deposit(self, amount):
        """
        Add the specified amount to the balance.
        """
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """
        Subtract the specified amount from the balance if sufficient funds are available.
        """
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    def view_balance(self):
        """
        Display the current balance.
        """
        print(f"Account Holder: {self.account_holder}")
        print(f"Current Balance: ${self.balance:.2f}")


# Example Usage
account = BankAccount("Alice")

# Deposit money
account.deposit(500)

# View balance
account.view_balance()

# Withdraw money
account.withdraw(200)

# View balance again
account.view_balance()

# Try to withdraw more than the balance
account.withdraw(400)

# View balance
account.view_balance()
