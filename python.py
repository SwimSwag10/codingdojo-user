class User:
  def __init__(self, name, money):
      self.name = name
      self.money = money

  def make_withdraw(self, withdraw=0):
    self.money -= withdraw
    return self.money

  def make_deposit(self, amount=0):
    self.money += amount
    return self.money

  def display_user_balance(self):
    return self.make_deposit() + self.make_withdraw()
  
  def transfer_money(self, other_user, amount):
    self.money += amount
    other_user.money -= amount

guido = User("Guido van Rossum", 1000)
guido.make_deposit(10)
monty = User("Monty Python", 10000)
monty.make_withdraw(100)
adrien = User("Adrien", 100)
adrien.make_withdraw(800)
nibbles = User("Mr. Nibbles", 50)
nibbles.make_withdraw(1000)
print(f"User: {guido.name}, Balance: {guido.money}")
print(f"User: {monty.name}, Balance: {monty.money}")
print(f"User: {adrien.name}, Balance: {adrien.money}")
print(f"User: {nibbles.name}, Balance: {nibbles.money}")

print("transfering money...")
guido.transfer_money(monty, 100) # monty is the one that is transfering 100$ to the other person specified when printing.
print(f"User: {guido.name}, Balance: {guido.money}")
print(f"User: {monty.name}, Balance: {monty.money}")

# first try:
# class User:
#   def __init__(self, name, account_balance):
#     self.name = name
#     self.account_balance = display_current_balance
  
#   def make_withdrawl(self, withdraw):
#     self.account_balance -= withdraw
  
#   def make_deposit(self, amount):
#     self.account_balance += amount

#   def display_user_balance(self, withdraw, deposit):
#     final = withdraw + deposit
#     return self.account_balance
  
#   # def transfer_money(self, other_user, amount):
#   #   pass

# guido = User("Guido van Rossum")
# monty = User("Monty Python")

# guido.make_deposit(100)
# guido.make_deposit(70)
# guido.make_deposit(15)
# print(f"current balance: ${monty.account_balance}")
# withdraw = int(input("Make a withdraw: $"))
# guido.make_withdrawl(withdraw)
# print(f"current balance: ${monty.account_balance}")


# TRYING TO ADD THE TRANSFER INPUT FUNCTIONALITY
# guido.transfer_money(monty, guido)
# print(f"User: {guido.name}, Balance: {guido.money}")
# print(f"User: {monty.name}, Balance: {monty.money}")

# class User:
#   def __init__(self, name, money):
#       self.name = name
#       self.money = money

#   def make_withdraw(self, withdraw=0):
#     self.money -= withdraw
#     return self.money

#   def make_deposit(self, amount=0):
#     self.money += amount
#     return self.money

#   def display_user_balance(self):
#     return self.make_deposit() + self.make_withdraw()
  
#   def transfer_money(self, other_user, yes_no, amount=0):
#     yes_no = input("Do you wish to transfer money?")
#     if yes_no.upper() == "YES" or "Y":
#       amount = input("Okay, how much money do you wish to transfer: ")
#       if int(amount) > 0:
#         self.money += amount
#         other_user.money -= amount

# guido = User("Guido van Rossum", 1000)
# guido.make_deposit(10)
# monty = User("Monty Python", 10000)
# monty.make_withdraw(100)
# adrien = User("Adrien", 100)
# adrien.make_withdraw(800)
# nibbles = User("Mr. Nibbles", 50)
# nibbles.make_withdraw(1000)
# print(f"User: {guido.name}, Balance: {guido.money}")
# print(f"User: {monty.name}, Balance: {monty.money}")
# print(f"User: {adrien.name}, Balance: {adrien.money}")
# print(f"User: {nibbles.name}, Balance: {nibbles.money}")

# guido.transfer_money(monty, guido)
# print(f"User: {guido.name}, Balance: {guido.money}")
# print(f"User: {monty.name}, Balance: {monty.money}")