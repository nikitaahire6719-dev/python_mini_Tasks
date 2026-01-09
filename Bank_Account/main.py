from account import BankAccount
from storage import load_account, save_account

data = load_account()

if data:
    acc_no, name, balance, transactions = data
    account = BankAccount(acc_no, name, balance, transactions)
else:
    acc_no = input("Enter Account Number: ")
    name = input("Enter Account Holder Name: ")
    account = BankAccount(acc_no, name, 0.0, [])
    save_account(acc_no, name, 0.0, [])

while True:
    print("\n--- Bank Account Simulator ---")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Mini Statement")
    print("4. Exit")

    choice = input("Enter choice: ")

    match choice:
        case "1":
            amt = float(input("Enter amount: "))
            account.deposit(amt)

        case "2":
            amt = float(input("Enter amount: "))
            account.withdraw(amt)

        case "3":
            account.mini_statement()

        case "4":
            save_account(
                account.acc_no,
                account.name,
                account.balance,
                account.transactions
            )
            print("Thank you for banking.")
            break

        case _:
            print("Invalid choice")
