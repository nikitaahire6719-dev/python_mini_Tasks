class BankAccount:
    def __init__(self, acc_no, name, balance, transactions):
        self.acc_no = acc_no
        self.name = name
        self.balance = balance
        self.transactions = transactions

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"Deposited: {amount}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
            return
        self.balance -= amount
        self.transactions.append(f"Withdrawn: {amount}")

    def mini_statement(self):
        print("\n--- Mini Statement ---")
        for t in self.transactions[-5:]:
            print(t)
        print("Current Balance:", self.balance)
