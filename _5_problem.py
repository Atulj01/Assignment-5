# Handling a Bank Account


from re import T


class Account:
    def __init__(self,title):
        self.title = "Ashish"
        self.balance = 0
        print("The Account is created of \n", "Account holder name :",title)

    def deposit(self,amount):
        amount = float(input("enter the amount to be deposit : "))
        self.balance = self.balance + amount
        print("Deposit is successful and the balance in the account is : ",self.balance )

    def withdrawal(self,amount):
        amount = float(input("enter the amount to be withdrawa : "))
        if (self.balance >= amount):
            self.balance = self.balance - amount
            print ("The withdrawal is successfull and balance id : ",self.balance)
        else:
            print("insuficient fund ")


    def getBalance(self):
        print("Balance in the account is %f"% self.balance)


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
Account_obj = Account(title="Ashish")
Account_obj.deposit(1)
Account_obj.withdrawal(1)
Account_obj.getBalance()
SavingAccount_obj=SavingAccount(balance=0,interestrate=0)
SavingAccount_obj.interestrate(4)