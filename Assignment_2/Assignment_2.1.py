import arithmatic as a

def main():
    print("enter two nubers : ")
    no1=int(input("first number : "))
    no2=int(input("second number : "))


    
    result1=a.add(no1,no2)
    result2=a.subtraction(no1,no2)
    result3=a.multiplication(no1,no2)
    result4=a.division(no1,no2)

    print(" addition of two numbers is = ",result1)
    print(" subtraction of two numbers is = ",result2)
    print(" multiplication of two numbers is = ",result3)
    print(" division of two numbers is = ",result4)




if __name__=="__main__":
    main()




