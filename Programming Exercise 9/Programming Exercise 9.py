class BankAcct:
    """
    BankAcct class represents a simple bank account.

    Attributes:
        name (str): Account holder's name
        account_number (str): Account number
        amount (float): Current balance
        interest_rate (float): Annual interest rate (as a decimal)
    """

    def __init__(self, name, account_number, amount, interest_rate):
        """
        Initializes the BankAcct object with provided values.
        """
        self.name = name
        self.account_number = account_number
        self.amount = amount
        self.interest_rate = interest_rate


    def adjust_interest_rate(self, new_rate):
        """
        Adjusts the interest rate.
        """
        self.interest_rate = new_rate


    def deposit(self, amount):
        """
        Deposits money into the account.
        """
        if amount > 0:
            self.amount += amount
            print(f"Deposited ${amount:.2f}")
        else:
            print("Deposit amount must be positive.")


    def withdraw(self, amount):
        """
        Withdraws money from the account if funds are available.
        """
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.amount:
            print("Insufficient funds.")
        else:
            self.amount -= amount
            print(f"Withdrew ${amount:.2f}")


    def get_balance(self):
        """
        Returns the current account balance.
        """
        return self.amount


    def calculate_interest(self, days):
        """
        Calculates interest based on number of days.

        Formula:
            Interest = Balance * Rate * (Days / 365)
        """
        interest = self.amount * self.interest_rate * (days / 365)
        return interest


    def __str__(self):
        """
        Returns a formatted string of account details.
        """
        return (f"Account Holder: {self.name}\n"
                f"Account Number: {self.account_number}\n"
                f"Balance: ${self.amount:.2f}\n"
                f"Interest Rate: {self.interest_rate * 100:.2f}%")


def test_bank_account():
    """
    Tests the BankAcct class methods with sample data.
    """

    # Create account
    account = BankAcct("Jeff Aries", "123456789", 1000.00, 0.05)

    print("\n--- Initial Account Info ---")
    print(account)

    # Deposit money
    print("\n--- Deposit ---")
    account.deposit(500)
    print(f"New Balance: ${account.get_balance():.2f}")

    # Withdraw money
    print("\n--- Withdraw ---")
    account.withdraw(300)
    print(f"New Balance: ${account.get_balance():.2f}")

    # Adjust interest rate
    print("\n--- Adjust Interest Rate ---")
    account.adjust_interest_rate(0.06)
    print(account)

    # Calculate interest
    print("\n--- Interest Calculation (30 days) ---")
    interest = account.calculate_interest(30)
    print(f"Interest Earned: ${interest:.2f}")

    # Final account display
    print("\n--- Final Account Info ---")
    print(account)


if __name__ == "__main__":
    test_bank_account()