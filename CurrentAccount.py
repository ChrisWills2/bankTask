from BankAccount import BankAccount

class CurrentAccount(BankAccount):

    def __init__(self, customerName, initialBalance, overdraftLimit):
        super().__init__(customerName, initialBalance)
        self.overdraftLimit = overdraftLimit

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if self._balance - amount < -self.overdraftLimit:
            raise ValueError("Withdrawal would exceed overdraft limit.")
        self._balance = round(self._balance - amount, 2)