class bankaccount :
    bankname="SBI Branch Pune :  "
    
    def __init__(self,A,B,C):
        self.__accountnumber=A
        self.name=B
        self.balance=C
    def deposit(self,amt):
        self.balance=self.balance  +amt
        return self.balance
    def withdrawal(self,WITH):
        self.balance=self.balance-WITH
        return self.balance
    def display(self):
        print("account balance : ",self.balance)
def main():
    obj1=bankaccount(101112,"aniket",1000)
    
    obj1.deposit(5000)
    print("before withdrawal :")
    obj1.display()
    obj1.withdrawal(500)
    print("after withdrawal :")
    obj1.display()
    #print("account balance : ",obj1.deposit(5000))

    #print("after withdrawal account balance : ",obj1.withdrawal(500))
if __name__=="__main__":
    main()