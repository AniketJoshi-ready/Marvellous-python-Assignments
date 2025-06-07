class Arithmatic : 
    PI = 3.14
    def __init__(self):
        self.value1=0
        self.value2=0
    def Accept(self):
         self.value1=int(input("enter 1st number  = "))
         self.value2=int(input("eneter 2 nd number = "))
       

    def addition(self):
        ans=0
        ans=self.value1 + self.value2
        return ans

    def subtraction(self):
        ans=0
        ans=self.value1 - self.value2
        return ans  
    

    def multiplication(self):
        ans=0
        ans=self.value1 * self.value2
        return ans 
    
    def division(self):
        ans=0
        try :
          ans=self.value1 / self.value2
        except ZeroDivisionError :
            print("bhiduuu 0 se divide mat kar value2 =0 not applicable ")
        return ans     
         

 

def main():
        
    obj1=Arithmatic()
    obj2=Arithmatic()
    obj3=Arithmatic()
    obj4=Arithmatic()
    obj5=Arithmatic()

    print()  # thoda to gap dikhana chahiye 

    obj1.Accept()

    r1=obj1.addition()
    r2=obj1.subtraction()
    r3=obj1.multiplication()
    r4=obj1.division()

    print("addition= ",r1)
    print("subtraction = ",r2)
    print("multiplication = ",r3)
    print("division = ",r4)


    print()

    obj2.Accept()

    r1=obj2.addition()
    r2=obj2.subtraction()
    r3=obj2.multiplication()
    r4=obj2.division()
            

    print("addition= ",r1)
    print("subtraction = ",r2)
    print("multiplication = ",r3)
    print("division = ",r4)


    print()

    obj3.Accept()


    r1=obj3.addition()
    r2=obj3.subtraction()
    r3=obj3.multiplication()
    r4=obj3.division()
            

    print("addition= ",r1)
    print("subtraction = ",r2)
    print("multiplication = ",r3)
    print("division = ",r4)

    print()

    obj4.Accept()

    r1=obj4.addition()
    r2=obj4.subtraction()
    r3=obj4.multiplication()
    r4=obj4.division()
            

    print("addition= ",r1)
    print("subtraction = ",r2)
    print("multiplication = ",r3)
    print("division = ",r4)

    print()

    obj5.Accept()

    r1=obj5.addition()
    r2=obj5.subtraction()
    r3=obj5.multiplication()
    r4=obj5.division()
            

    print("addition= ",r1)
    print("subtraction = ",r2)
    print("multiplication = ",r3)
    print("division = ",r4)

if __name__=="__main__":
    main()