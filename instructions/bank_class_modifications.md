# Bank Class Modifications

Modify the `Bank` class defined in the [bank.py](/bank_system/bank.py) file as follows:

1. Add `create_account:  Define a method called `create_account` that takes 6 arguments - `account_type`, `account_number`, `account_holder_name`, `balance`, `interest_rate` and `overdraft_limit`.  Inside the `create_account method`, check the `account_type` parameter to determine which type of account to create. If account_type is 'SavingsAccount', create a new SavingsAccount object with the given parameters. If account_type is 'CheckingAccount', create a new CheckingAccount object with the given parameters. If the provided account_type is neither of the two valid options, print an error message saying "Invalid account type." and return from the method without creating an account.  Finally, add the newly created account object to the `accounts` list of the Bank class.

    **Note**: `interest_rate` is an optional argument for a SavingsAccount and overdraft_limit is an optional argument for a CheckingAccount.
