class bank_account : 
    ROI=10.5
    def __init__(self):
        self.name="MR ANIKET "
        self.amount=0
    def Deposit(self):
        self.dep_amount=float(input("please enter the amount you are going to deposit "))
        self.amount=self.amount+self.dep_amount
        return self.amount 
        
    def Withdrawal(self):
        self.withdrwal_amt=float(input("please enter the amount you are going to withdrawal from your deposit :"))    
        self.amount=self.amount-self.withdrwal_amt
        return self.amount
    
    def CalculateIntrest(self):
        self.amount=self.amount + ((bank_account.ROI/100) * self.amount)
        return self.amount
    
    def Display(self):
        #self.name=" hello MR ANIKET "
        print(self.name)
        print("your bank amount currently with intrest of 10.5 is ",self.amount)

def main():

    obj1=bank_account()

    obj1.Deposit()
    obj1.Withdrawal()
    obj1.CalculateIntrest()
    obj1.Display()


    print()
    obj2=bank_account()

    obj2.Deposit()
    obj2.Withdrawal()
    obj2.CalculateIntrest()
    obj2.Display()


    print()
    obj3=bank_account()

    obj3.Deposit()
    obj3.Withdrawal()
    obj3.CalculateIntrest()
    obj3.Display()


if __name__=="__main__":
    main()