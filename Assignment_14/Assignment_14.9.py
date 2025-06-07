class product :
    def __init__(self,A,B):
        self.name=A
        self.price=B
    def __eq__(pahilaobject,dusraobject): 
        if isinstance(dusraobject,product): # for checking ye wala object tere product class se belong he kya?
            if pahilaobject.price==dusraobject.price:
                return True
            else:
                return False  
        else:
            print("this object is not from class you have mentioned ")
def main():            
    obj1=product("plate",100)
    obj2=product("chamcha",100)  

    print("are they equal obj1 and obj2 price ? : ",(obj1==obj2))
if __name__=="__main__":
    main()  