class Book :
    def __init__(self,A,):
        self.__price=A
    def get(self)  :
        return self.__price
    
    def set(self,new):
        if self.__price>0 :
            self.__price=new
        else:
            pass
        return self.__price
def main():
    obj1=Book(60)
    print("old price = ",obj1.get())   


    print("new price = ",obj1.set(200))
    
if __name__=="__main__":
    main()   