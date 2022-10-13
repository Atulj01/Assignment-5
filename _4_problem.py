# Implement a Banking Accountn  

class Account:
    def __init__(self,title):
        self.balance = int(5000)
        print("The Account is created of \n", "Account holder name :",title)
        pass
        

    def display(self):
        print("\n Net Available Balance =", self.balance)
        pass    
   

class SavingAccount(Account):
    def __init__(self,balance,interestrate):
        super().__init__(balance)
        self.interestRate = interestrate

    def interestrate(self,interestrate,p=0,t=0,r=0):
        p = float(input("enter the balance in account :"))
        t = int(input("enter the time period to keep :"))
        r = float(input("enter the interestrate :"))
        print("The principle amount is :",p)
        print("The time period in year is :", t)
        print("The rate of interest : ",r)

        interestrate = (p * t * r)/100
        print("interestamount is :",interestrate)
        pass

Account_obj = Account(title = "Ashish")
Account_obj.display()
SavingAccount_obj=SavingAccount(balance=0,interestrate=0)
SavingAccount_obj.interestrate(4)