class BankAccount:
    _nextAccountNumber = 100000

    def __init__(self, customerName, initialBalance):
        self.customerName = customerName
        self._accountNumber = BankAccount._nextAccountNumber
        BankAccount._nextAccountNumber += 1
        self._balance = round(initialBalance,2)

    def getCustomerName(self):
        return self.customerName
    
    def getAccountNumber(self):
        return self._accountNumber
    
    def getBalance(self):
        return self._balance
    
    def withdraw(self,amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive and above 0.")
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance = round(self._balance - amount,2)

    def deposit(self,amount):
        if amount <= 0:
            raise ValueError("deposit must be positive.")
        self._balance = round(self._balance + amount, 2)

