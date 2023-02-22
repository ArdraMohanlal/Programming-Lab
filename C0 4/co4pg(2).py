#2.  Create a Bank account with members account number, name, type of account and balance.
#Write constructor and methods to deposit at the bank and withdraw an amount from the bank
class bank:
    def __init__(self):
        self.name=str(input("enter the name:"))
        self.accountnumber=int(input("enter the account number:"))
        self.balance=0
        self.typeofaccount=str(input("enter the type of account savings/current:"))
    def deposite (self):
        deposite=int(input("enter the amount to be deposited:"))
        self.balance=self.balance+deposite
        
       
    def withdraw (self):
        wdamount=int(input("enter the withdrawamount:"))
        if self.balance>=wdamount:
            self.balance=self.balance-wdamount
            
        else:
            print("insufficcient balance")
    def display(self):
        print("the net balance",self.balance)
object=bank()
while(True):
    print("\n 1.Deposite money \n 2.withdraw money\n 3.display balance\n4exit(0)")
    ch=int(input("enter the choice:"))
    if(ch==1):
        object.deposite()
        object.display()
    elif(ch==2):
       object.withdraw()
       object.display()
    elif(ch==3):
       object.display()
    else:
        exit(0)

  
        
        
    