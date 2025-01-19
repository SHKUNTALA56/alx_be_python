class BankAccount:
    def __init__(self, initial_balance=0):
        """
        Initialize the bank account with an optional initial balance.
        :param initial_balance: Initial balance for the account (default is 0)
        """
        self.__account_balance = initial_balance

    def deposit(self, amount):
        """
        Deposit a specified amount to the account balance.
        :param amount: The amount to deposit
        """
        if amount > 0:
            self.__account_balance += amount

    def withdraw(self, amount):
        """
        Withdraw a specified amount from the account balance.
        :param amount: The amount to withdraw
        :return: True if the withdrawal is successful, False if insufficient funds
        """
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        return False

    def display_balance(self):
        """
        Display the current account balance in a user-friendly format.
        """
        print(f"Current balance: ${self.__account_balance:.2f}")

