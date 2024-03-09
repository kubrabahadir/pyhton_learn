**Bank Account Management System**

This Python script manages bank accounts with functionalities like withdrawing money, depositing money, and displaying account details.
Features:

Withdraw Money: Allows users to withdraw money from their account.
Deposit Money: Facilitates depositing money into either the main account or the additional account.
Show Account Details: Displays the balance of either the main account or the additional account.

How to Use:

Input Information: When prompted, input your name, surname, account number, account state, and additional account state.
Withdraw Money: Use the withdrawMoney function to withdraw money from the account. If the account balance is sufficient, the withdrawal is processed. If not, it checks if the additional account can cover the deficit.
Deposit Money: Use the depositMoney function to deposit money into the account. Choose between adding to the main account balance or the additional account balance.
Show Account Details: Use the showAccount function to display the balance of either the main account or the additional account.

Functions:

withdrawMoney(account, quantity): Allows withdrawing money from the account.
depositMoney(account, quantity): Facilitates depositing money into the account.
showAccount(account): Displays the balance of the account.

Example Usage:

python

    withdrawMoney(AccountS, 3000)
    withdrawMoney(AccountA, 3000)
    depositMoney(AccountS, 3000)
    depositMoney(AccountA, 3000)
    showAccount(AccountS)
    showAccount(AccountA)

Note:

Ensure to input valid data to avoid errors.
Additional functionalities such as error handling and data validation can be added for robustness.
