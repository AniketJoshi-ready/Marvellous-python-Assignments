class demo :
    value="i am class variable "
    def __init__(self,A,B):
        self.no1=A
        self.no2=B
    def fun(self):
        print("in fun function :")
        print("first num = ",self.no1)
        print("second num = ",self.no2)
    def gun(self):
        print("in gun function : ")
        print("first num = ",self.no1)
        print("second num = ",self.no2)  

def main():
    print("look who is this ? : "+demo.value)

    obj1=demo(11,21)
    obj2=demo(51,101)

    obj1.fun()
    obj2.fun()
    obj1.gun()
    obj2.gun()

if __name__=="__main__":
    main()    