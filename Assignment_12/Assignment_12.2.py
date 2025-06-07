class circle : 
    PI = 3.14
    def __init__(self):
        self.radius=0.0
        self.area=0.0
        self.circumference=0.0
    def Accept(self):
         self.radius=float(input("enter the radius = "))
       # print("eneter the radius : ",self.radius)

    def calculate_Area(self):
        self.area=circle.PI * (self.radius **2)

    def calculate_circumference(self):
        self.circumference = circle.PI    *   2*self.radius    

    def display(self):
        print("when radius of circle =  ",self.radius)
        print("area of circle =  ",self.area)
        print("circumference of circle =  ",self.circumference)

def main():

    obj1=circle()
    obj2=circle()
    obj3=circle()
    obj4=circle()
    obj5=circle()



    obj1.Accept()
    


    print()  # thoda to gap dikhana chahiye 
    obj1.calculate_Area()
    obj1.calculate_circumference()
    obj1.display()

    print()
    obj2.Accept()
    print()
    obj2.calculate_Area()
    obj2.calculate_circumference()
    obj2.display()
            

    print()
    obj3.Accept()
    print()
    obj3.calculate_Area()
    obj3.calculate_circumference()
    obj3.display()


    print()
    obj4.Accept()
    print()
    obj4.calculate_Area()
    obj4.calculate_circumference()
    obj4.display()


    print()
    obj5.Accept()
    print()
    obj5.calculate_Area()
    obj5.calculate_circumference()
    obj5.display()

if __name__=="__main__":
    main()