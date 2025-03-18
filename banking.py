class BankAccount:
    def __init__(self, owner, balance=0.0):
        """Initialize the bank account with an owner and an optional balance."""
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        """Deposit money into the account."""
        if amount > 0:
            self.balance += amount
            return f"Deposited ${amount}. New balance: ${self.balance}"
        return "Deposit amount must be positive."

    def withdraw(self, amount):
        """Withdraw money from the account if funds are available."""
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.balance}"
        elif amount > self.balance:
            return "Insufficient funds."
        return "Withdrawal amount must be positive."

    def get_balance(self):
        """Check the current balance."""
        return f"Current balance: ${self.balance}"

    def __str__(self):
        """String representation of the account."""
        return f"Bank Account of {self.owner} - Balance: ${self.balance}"


# Example Usage (Remove this before submitting if needed)
if __name__ == "__main__":
    account = BankAccount("John Doe", 100)
    print(account.deposit(50))
    print(account.withdraw(30))
    print(account.get_balance())
    print(account.withdraw(200))  # Should show "Insufficient funds."
