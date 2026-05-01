
class BankAccount:
  def __init__(self,account_holder,account_number,balance):
    self.account_holder=account_holder
    self.account_number=account_number
    self.balance=balance
  def display_details(self):
     print("Account Details)
     print(f"Account Holder:{self.account_holder}")
     print(f"Account Number:{self.account_number}")
     print(f"Balance:${self.balance}")
acc1=BankAccount("Divya"12345,500000)
acc2=BankAccount("Shree",67895,500000)
acc1.display_details()
acc2.display_details()
  
