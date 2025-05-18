from functools import reduce
import MarvellousNum as m
def main():
    countnum=int(input("give me count of numbers wanted in list  N :"))
    
    data=list()

    print("enter the  numbers  : ")
    for i in range(countnum):
        num=int(input())
        data.append(num)
    print("list of given number = ",data)


    sum=0
    sum=reduce(lambda a,b: a+b ,data) 
    print("sum of numbers  in given  list ",sum)  

    
    def listprime():   # bhidduu this fn will print prime list  and their addition
        list_prime=[]
        for ele in data:
          if m.chkprime(ele)==True:
              list_prime.append(ele)

        print("prime number list : ",list_prime) 

        sum=0
        sum=reduce(lambda a,b: a+b ,list_prime) 
        print("sum of numbers  in prime number  list ",sum)  

      
              
    listprime()


if __name__=="__main__":
    main()