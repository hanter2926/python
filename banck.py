class BankAccount:
    def _init_(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Updated Balance:", self.balance)

apple = BankAccount(1)
acc = BankAccount(1000)