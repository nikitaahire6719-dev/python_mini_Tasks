FILENAME = "account.txt"

def load_account():
    try:
        with open(FILENAME, "r") as file:
            lines = file.readlines()
            acc_no = lines[0].strip()
            name = lines[1].strip()
            balance = float(lines[2].strip())
            transactions = [t.strip() for t in lines[3:]]
            return acc_no, name, balance, transactions
    except FileNotFoundError:
        return None


def save_account(acc_no, name, balance, transactions):
    with open(FILENAME, "w") as file:
        file.write(acc_no + "\n")
        file.write(name + "\n")
        file.write(str(balance) + "\n")
        for t in transactions:
            file.write(t + "\n")
