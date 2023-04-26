from banking_system import SavingsAccount, CheckingAccount

class Bank:
    """A class representing a bank with various account types."""

    def __init__(self):
        self.accounts = []

    # todo: Add the following method(s):
    #       create_account
    
    def create_account(self, account_type, account_number, account_holder_name, balance, interest_rate = 0.0, overdraft_limit = 0):
        # Check the account_type parameter to determine which type of account to create
        if account_type == "SavingsAccount":
            # Create a new SavingsAccount instance with the provided account number, account holder name, balance, and interest rate
            account = SavingsAccount(account_number, account_holder_name, balance, interest_rate)
        elif account_type == "CheckingAccount":
            # Create a new CheckingAccount instance with the provided account number, account holder name, balance, and overdraft limit
            account = CheckingAccount(account_number, account_holder_name, balance, overdraft_limit)
        else: 
            # If the account_type parameter is not valid, print an error message and return
            print("Invalid account type")
            return
        # Add the new account to the list of accounts in the Bank instance
        self.accounts.append(account)
        

    def delete_account(self, account_number):
        """Deletes an account with the given account number.

        Args:
            account_number (str): The account number of the account to delete.
        """
        for account in self.accounts:
            if account.account_number == account_number:
                self.accounts.remove(account)
                return
        print("Account not found.")

    def find_account(self, account_number):
        """Finds an account with the given account number.

        Args:
            account_number (str): The account number to search for.

        Returns:
            Account or None: Returns the account if found, otherwise None.
        """
        for account in self.accounts:
            if account.account_number == account_number:
                return account
        print("Account not found.")
        return None

    def list_accounts(self):
        """Displays the details of all accounts."""
        for account in self.accounts:
            account.display()
            print()
