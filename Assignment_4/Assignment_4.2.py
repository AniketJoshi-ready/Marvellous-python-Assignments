def main():
    no1=int(input("enter 1st number :"))
    no2=int(input("eneter 2nd number : "))

    multiplication=lambda x,y: x*y 
    result=multiplication(no1,no2)
    print("multiplication of these two numbers is : ",result)


if __name__=="__main__":
    main()    