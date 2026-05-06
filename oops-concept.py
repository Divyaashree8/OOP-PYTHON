class BankAccount:
  def __init__(self,account_holder,account_number,balance):
    self.account_holder=account_holder
    self.account_number=account_number
    self.__balance=balance #private variable
  def get_balance(self):
    return self.__balance
  def deposite(self,amount):
     if amount>0:
        self.__balance +=amount
        print(f"${amount} deposited successfully.")
     else:
       print("Invaild amount! Deposite must be positive.")
  
  def display_details(self):
     print("Account Details)
     print(f"Account Holder:{self.account_holder}")
     print(f"Account Number:{self.account_number}")
     print(f"Balance:${self.__balance}")
  # child class
  class SavingsAccount(Account):
    MIN_Balance=1000
    def withdraw(self,amount):
    if amount <=0:
      print("Invalid amount! withdrawal must be positive")
    elif self.__balance - amount<self.MIM_Balance:
      print("Cannot withdraw minimum balance must be maintained.")
    elif amount> self.__balance:
      print("Insufficient balance")  
    else:
      self.__balance-=amount
      print(f"${amount}withdrawn successfully.")
# child class 2
class CurrentAccount(Account):
    Overdraft_limit=5000
    def withdraw(self,amount):
    if amount <=0:
      print("Invalid amount! withdrawal must be positive")
    elif amount> self.__balance + self.Overdraft_limit:
      print("Overdraft limit exceeded!")  
    else:
      self.__balance-=amount
      print(f"${amount}withdrawn successfully.")
acc1=SavingsAccount("Divya",12345,500000)
acc2=CurrentAccount("Shree",67895,500000)
acc1.display_details()
acc2.display_details()
acc1.deposite(2000)
acc1.withdraw(1000)

print("Current Balance:",acc1.get_balance())
  

  
