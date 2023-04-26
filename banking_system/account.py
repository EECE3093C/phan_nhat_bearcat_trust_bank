class Account:
    """A class representing a bank account."""

    # todo: Add the following methods:
    #       __init__
    #       deposit
    #       withdraw
            
    def __init__(self, account_number, account_holder_name, balance):
        # Initialize the account number attribute with the provided account number parameter
        self.account_number = account_number
    
        # Initialize the account holder name attribute with the provided account holder name parameter
        self.account_holder_name = account_holder_name
    
        # Initialize the balance attribute with the provided balance parameter
        self.balance = balance
        
    def deposit(self, amount):
        # Add the provided amount to the current balance
        self.balance += amount
        
    def withdraw(self, amount):
        # Check if the requested withdrawal amount is less than or equal to the current balance
        if amount <= self.balance:
         # If so, subtract the amount from the current balance
            self.balance -= amount
        else:
        # If not, print an error message indicating there are insufficient funds to withdraw
            print("There are insufficient funds to withdraw.")    
            
    def get_balance(self):
        """Return the current balance of the account."""
        return self.balance

    def display(self):
        """Display the account information."""
        print(f"Account Number: {self.account_number}\nAccount Holder: {self.account_holder_name}\nBalance: ${self.balance}")


class SavingsAccount(Account):
    """A class representing a savings account."""

    # todo: Add the following method(s):
    #       __init__
    
    def __init__(self, account_number, account_holder_name, balance, interest_rate = 0.0):
        # Call the parent class initializer with the provided account number, account holder name, and balance
        super().__init__(account_number, account_holder_name, balance)
        
        # Initialize the interest rate attribute with the provided interest rate parameter (or the default value of 0.0 if no parameter is provided)
        self.interest_rate = interest_rate
        
    def calculate_interest(self):
        """Calculate and return the interest on the account balance."""
        return self.balance * (self.interest_rate / 100)

    def display(self):
        """Display the savings account information including the interest rate."""
        super().display()
        print(f"Interest Rate: {self.interest_rate}%")


class CheckingAccount(Account):
    """A class representing a checking account."""

    # todo: Add the following methods:
    #       __init__
    
    def __init__(self, account_number, account_holder_name, balance, overdraft_limit = 0):
        # Call the parent class initializer with the provided account number, account holder name, and balance
        super().__init__(account_number, account_holder_name, balance)
        
        # Initialize the overdraft limit attribute with the provided overdraft limit parameter (or the default value of 0 if no parameter is provided)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        """Withdraw the given amount from the account if it doesn't exceed the overdraft limit."""
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
        else:
            print("Overdraft limit exceeded.")

    def display(self):
        """Display the checking account information including the overdraft limit."""
        super().display()
        print(f"Overdraft Limit: ${self.overdraft_limit}")
