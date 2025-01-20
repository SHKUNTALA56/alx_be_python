class BankAccount:
    def __init__(self, initial_balance=0):
        """
        Initialize the BankAccount with an optional starting balance.
        :param initial_balance: The starting balance for the account (default is 0).
        """
        self.__account_balance = initial_balance

    def deposit(self, amount):
        """
        Deposit a specified amount into the account.
        :param amount: The amount to deposit (must be positive).
        """
        if amount > 0:
            self.__account_balance += amount
        else:
            print("Error: Deposit amount must be positive.")

    def withdraw(self, amount):
        """
        Withdraw a specified amount from the account if funds are sufficient.
        :param amount: The amount to withdraw (must be positive).
        :return: True if the withdrawal was successful, False otherwise.
        """
        if amount > 0 and amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        elif amount <= 0:
            print("Error: Withdrawal amount must be positive.")
        else:
            print("Error: Insufficient funds.")
        return False

    def display_balance(self):
        """
        Display the current account balance.
        """
        print(f"Current Balance: ${self.__account_balance:.2f}")