class Account:
    def __init__(self):
        self.balance = 0

    def deposit(self,n):
        self.balance += n

    def withdraw(self,n):
        self.balance -= n



dharun = Account()
deenoo = Account()


print(deenoo.balance)
deenoo.deposit(100)
deenoo.withdraw(50)
print(deenoo.balance)

print(dharun.balance)
dharun.deposit(10)
dharun.withdraw(5)
print(dharun.balance)
