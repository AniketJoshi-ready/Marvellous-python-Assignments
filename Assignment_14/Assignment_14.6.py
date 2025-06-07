class calculator :
    def __init__(self,A,B):
        self.value1=A
        self.value2=B

    def add(self):
        r=self.value1+self.value2
        return r
    def sub(self):
        r=self.value1 - self.value2
        return r
    def mul(self):
        r=self.value1 * self.value2
        return r
    
    def div(self):
        r=self.value1 / self.value2
        return r
            
    
def main():
    
    number1=int(input("enter 1st number : "))
    number2=int(input("enter 2nd number : "))
    
    obj1=calculator(number1,number2)
    print("Addition of numbers = ",obj1.add())
    print("Subtraction of numbers = ",obj1.sub())
    print("Multiplication of numbers = ",obj1.mul())
    print("Division of numbers = ",obj1.div())
if __name__=="__main__":
    main()   