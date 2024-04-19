menu = ("""
[d] Deposit
[s] Withdraw
[e] Statement
[q] Quit
""")

money_in_account = 0
withdrawals_made = 0
WITHDRAWAL_LIMIT = 3
WITHDRAWAL_AMOUNT_LIMIT = 500.0
statement = "" 

def deposit(deposit_amount):
    global money_in_account
    global statement

    if deposit_amount <= 0:
        print("Invalid provided value")
    else:
        money_in_account += deposit_amount
        statement += f"Function: Deposit  |  Amount: {deposit_amount}\n"
        print(f"Successful deposit | Amount: {deposit_amount}")
        
def withdraw(withdraw_amount):
    global WITHDRAWAL_LIMIT
    global WITHDRAWAL_AMOUNT_LIMIT
    global withdrawals_made
    global statement
    global money_in_account

    if withdraw_amount <= 0:
        print("Invalid withdrawal amount")
    elif withdraw_amount > money_in_account:
        print("Withdrawal amount greater than balance.")
    elif withdrawals_made == WITHDRAWAL_LIMIT:
        print("Withdrawal limit reached.")
    elif withdraw_amount > WITHDRAWAL_AMOUNT_LIMIT:
        print("Requested withdrawal amount exceeds the withdrawal limit.")
    else:
        money_in_account -= withdraw_amount
        statement += f"Function: Withdraw  |  Amount: {withdraw_amount}\n"
        print(f"Successful withdrawal | Amount: {withdraw_amount}")
        withdrawals_made += 1 
        

while True:
    print("-" * 10)
    print_choice = input(menu)
    print("-" * 10)

    if print_choice == "d":
        deposit_amount = float(input("Enter the amount to Deposit: "))
        deposit(deposit_amount)
        
    elif print_choice == "s":
        withdraw_amount = float(input("Enter the amount to withdraw: "))
        withdraw(withdraw_amount)
        
    elif print_choice == "e":
        print(statement)
        print(f"Balance: {money_in_account}")

    elif print_choice == "q":
        break

    else:
        print("Invalid operation")
