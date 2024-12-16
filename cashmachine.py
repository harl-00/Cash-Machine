balance = 0.0
transaction_history = []
attempts = 3
accountpin = 3324
#FIX TRANSACTION HISTORY#########
#FIX TRANSACTION HISTORY#########
#FIX TRANSACTION HISTORY#########
def verify():
    global attempts
    while attempts > 0:
        Pin = int(input("Enter PIN: "))
        if Pin == accountpin:
            print("Verification successful.")
            return True
        else:
            attempts -= 1
            print(f"Incorrect. {attempts} attempts left.")
    return False

def check_balance():
    print(f"Balance: £{balance:.2f}")

def deposit():
    global balance
    amount = float(input("amount depositing: "))
    if amount > 0:
        balance += amount
        transaction_history.append(f"Deposited: £{amount}")
        print("Successful Deposit")
    else:
        print("Incorrect, Ensure the number you inputted is above 0")

def withdraw():
    global balance
    amount = float(input("amount withdrawing: "))
    if amount > balance:
        print("Insufficient Funds.")
    elif amount > 0:
        balance -= amount
        transaction_history.append(f"Withdrew: £{amount}")
        print("Successful Withdrawal.")
    else:
        print("Error occured")

def history():
    for transaction in transaction_history:
        print(transaction)
        
if verify():
    while True:
        print("1. check balance\n2. deposit\n3. withdraw\n4. view transaction history")
        option = input("Select a choice: ")

        if option == "1":
            check_balance()
        elif option == "2":
            deposit()
        elif option == "3":
            withdraw()
        elif option == "4":
            history()
        else:
            print("invalid option. Choose a number 1-4")
