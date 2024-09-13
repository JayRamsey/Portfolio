
class account:
    def __init__(self, Account_number, Balance):
        self._Account_number = Account_number
        self._Balance = Balance

    def Deposit(self, amount):
        self._Balance += amount

    def Withdraw(self, amount):
        if amount <= self._Balance:
            self._Balance -= amount
        else:
            print("Insufficient funds")

    def Get_balance(self):
        return self._Balance
    
accounts = []

def create_account(Account_number, Balance):
    accounts.append(account(Account_number, Balance))

def main():
    create_account("1261", 0.0)
    create_account("3534", 0.0)

    while True:
        entered_num = input("Enter account number: ")
        for account in accounts:
            if account._Account_number == entered_num:
                print("This account has £" + str(account.Get_balance()) + ".")

                account.Deposit(float(input("Enter amount to deposit: ")))
                account.Withdraw(float(input("Enter amount to withdraw: ")))

                print("This account now has £" + str(account.Get_balance()) + ".")
main()