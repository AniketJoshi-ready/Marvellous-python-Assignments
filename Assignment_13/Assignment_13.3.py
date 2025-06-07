class Numbers :
    sum=0
    def __init__(self,A):
        self.value=A
    def chkprime(self):
        print("given number : ",self.value)
        
        if self.value ==0 or self.value==1 :
            print("sorry beta 0 and 1 are not consider as prime numbers ")
        else:
            for i in range(2,self.value):
                if self.value % i == 0:
                    return False
                else:
                    return True
        #return True or False        

    def factors(self):
        print("factors of given number  are : ",end=" ")
        for i in range (1,self.value):
            if self.value % i == 0:
               print(i,end=" ")
            else:
                pass
    def sumfactors(self):

        for i in range (1,self.value):   # for value 0 it doesnot work proper
            if self.value % i == 0:
                Numbers.sum=Numbers.sum+i
            else:
                pass          
        return Numbers.sum
    
    def chkperfect(self):
        if Numbers.sum == self.value :
            return True
        else:
            return False


def main():

    obj1=Numbers(4)
    r1=obj1.chkprime()
    print("The given number is prime number :",r1)

    r2=obj1.factors()
    #print("The given number  factors are  :",r)

    print()
    r3=obj1.sumfactors()
    print("sum of the factors of the given number  is  :",r3)

    r4=obj1.chkperfect()
    print("The given number is perfect number :",r4)




    print()

    obj2=Numbers(11)
    r1=obj2.chkprime()
    print("The given number is prime number :",r1)

    r2=obj2.factors()
    #print("The given number  factors are  :",r)

    print()
    r3=obj2.sumfactors()
    print("sum of the factors of the given number  is  :",r3)

    r4=obj2.chkperfect()
    print("The given number is perfect number :",r4)



    print()

    obj3=Numbers(40)
    r1=obj3.chkprime()
    print("The given number is prime number :",r1)

    r2=obj3.factors()
    #print("The given number  factors are  :",r)

    print()
    r3=obj3.sumfactors()
    print("sum of the factors of the given number  is  :",r3)

    r4=obj3.chkperfect()
    print("The given number is perfect number :",r4)

                    
    print()

    obj4=Numbers(0)
    r1=obj4.chkprime()
    print("The given number is prime number :",r1)

    r2=obj4.factors()
    #print("The given number  factors are  :",r)

    print()
    r3=obj4.sumfactors()
    print("sum of the factors of the given number  is  :",r3)

    r4=obj4.chkperfect()
    print("The given number is perfect number :",r4)






    print()

    obj5=Numbers(6)
    r1=obj5.chkprime()
    print("The given number is prime number :",r1)

    r2=obj5.factors()
    #print("The given number  factors are  :",r)

    print()
    r3=obj5.sumfactors()
    print("sum of the factors of the given number  is  :",r3)

    r4=obj5.chkperfect()
    print("The given number is perfect number :",r4)


if __name__=="__main__":
    main()