from bank_account import BankAccount

account1=BankAccount("1234", 47.65)
print(account1)
account1.deposit(105.68)
account1.withdraw(56.78)
print(account1.get_balance())

account2=BankAccount("4321", 4600.69)
account2.withdraw(56.78)
print(account2.get_balance())

