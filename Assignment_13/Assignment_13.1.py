class Bookstore : 
    NoOfBooks=0

    def __init__ (self,A,B):
    
        self.Name=A
        self.Auther=B
        Bookstore.NoOfBooks=Bookstore.NoOfBooks+1

    def display(self):
       print(self.Name," by ",self.Auther,"  No of books : ",Bookstore.NoOfBooks)
       ''' print("name of book : "+self.Name)
        print("auther of book : "+self.Auther)    
        print("number of books : ",Bookstore.NoOfBooks)'''
        

def main():

    obj1=Bookstore("Linux System Programming ","Robert Love .")
    obj1.display() 

    obj2=Bookstore("C Programming Language ","anni . ")
    obj2.display() 

    

if __name__=="__main__":
    main()