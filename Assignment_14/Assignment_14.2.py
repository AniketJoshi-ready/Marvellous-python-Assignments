class Rectangle : 
    def __init__(self,A,B):
        self.l=A
        self.b=B
    def calc(self):
        area=self.l*self.b
        perimeter= (self.l +self.b) * 2
        print("Area : ",area,", perimeter : ",perimeter)

def main():
    obj1=Rectangle(5,10)
    obj1.calc()
if __name__=="__main__":
    main()  