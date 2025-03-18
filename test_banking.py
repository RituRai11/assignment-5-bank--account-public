import unittest
from banking import BankAccount

class TestBankAccount(unittest.TestCase):
    def setUp(self):
        """Create a sample bank account for testing."""
        self.account = BankAccount("Alice", 500)

    def test_initial_balance(self):
        """Test if the initial balance is set correctly."""
        self.assertEqual(self.account.balance, 500)

    def test_deposit(self):
        """Test depositing money into the account."""
        self.assertEqual(self.account.deposit(100), "Deposited $100. New balance: $600")
        self.assertEqual(self.account.deposit(-10), "Deposit amount must be positive.")

    def test_withdraw(self):
        """Test withdrawing money from the account."""
        self.assertEqual(self.account.withdraw(200), "Withdrew $200. New balance: $300")
        self.assertEqual(self.account.withdraw(1000), "Insufficient funds.")
        self.assertEqual(self.account.withdraw(-50), "Withdrawal amount must be positive.")

    def test_get_balance(self):
        """Test retrieving the account balance."""
        self.account.deposit(50)
        self.assertEqual(self.account.get_balance(), "Current balance: $550")

if __name__ == "__main__":
    unittest.main()
