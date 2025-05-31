import multiprocessing


def factorial(num):
    fact=1
    for i in range(num):
        fact=fact*num
        num=num-1
    return fact   
       
def main():
    #data=[1,2,3,4,5,6]
    data=[]
    size=int(input("size of list : "))
    print("enter the numbers : ")
    for i in range(size):
        num=int(input())
        data.append(num)
    print("given list by you : ",data)    

    p=multiprocessing.Pool()
    result=p.map(factorial,data)
    print("factorial of each element in list given in another list : ",result)
    
    

if __name__=="__main__":
    main()   