from functools import reduce
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
    print("sum of numbers  in list ",sum)   



if __name__=="__main__":
    main()