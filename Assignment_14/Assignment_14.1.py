class employee :
    def __init__ (self,A,B,C):
        self.name=A
        self.emp_id=B
        self.salary=C

      
    def display(self):
        print("Name : ",self.name,end=", ")
        print("ID : ",self.emp_id,end=", ")
        print("Salary : ",self.salary)
        
    
def main():
    obj1=employee("Rohit",101,50000)
    obj1.display()
if __name__=="__main__":
    main()    