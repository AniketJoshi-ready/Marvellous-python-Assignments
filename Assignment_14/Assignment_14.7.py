class person :
    def __init__(self,A,B) :
        self.name=A
        self.age=B
    def display(self):
        print(" from person class : name =",self.name)
        print(" from person  class : age =",self.age)    
        #print(" from person class : subject =",self.subject)   NOT POSSIBLE ONLY DERIVE CAN HAVE ACCESS OF PARENT 
        #print(" from person class : salary =",self.salary)     NOT POSSIBLE PARENT DONT ACCESS CHILD
class teacher (person):
    def __init__(self,A,B,C,D):
        super().__init__(A,B)
        self.subject=C
        self.salary=D
    def display(self):
        print(" from derive class : name =",self.name)
        print(" from derive class : age =",self.age)
        print(" from derive class : subject =",self.subject)
        print(" from derive class : salary =",self.salary)
def main():
    obj1=teacher("aniket",23,"python programming ",30000)  # by using derive teacher class print display 
    obj1.display()  

    print()
    obj2=person("aniket",23)  # parent class print display
    obj2.display()
    
if __name__=="__main__":   
    main() 